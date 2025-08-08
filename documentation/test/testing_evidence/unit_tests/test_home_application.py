from django.test import TestCase, Client
from django.urls import reverse
from django.core import mail
from django.contrib.messages import get_messages
from products.models import Product, Category
from unittest.mock import patch
import json

class HomeViewTestSuite(TestCase):
    """Test suite for home page functionality"""
    
    def setUp(self):
        """Initialize test client and create test products"""
        self.client = Client()
        
        # Create test category and products for featured products display
        self.category = Category.objects.create(
            name="test_category",
            friendly_name="Test Category"
        )
        
        # Create multiple products to test random selection
        for i in range(6):
            Product.objects.create(
                category=self.category,
                name=f"Test Product {i}",
                price=99.99 + i
            )
    
    def test_home_page_loads(self):
        """Test that home page loads correctly"""
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "CNCraft")  # Check for site name
    
    def test_home_page_template(self):
        """Test that correct template is used"""
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'home/index.html')
    
    def test_home_page_featured_products(self):
        """Test that featured products are displayed on home page"""
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        
        # Check that featured_products context variable exists
        self.assertIn('featured_products', response.context)
        
        # Check that we get up to 4 products (or less if fewer exist)
        featured_products = response.context['featured_products']
        self.assertLessEqual(len(featured_products), 4)
        
        # Verify products are actually Product instances
        for product in featured_products:
            self.assertIsInstance(product, Product)


class HomepageEnquiryTestSuite(TestCase):
    """Test suite for homepage enquiry AJAX functionality"""
    
    def setUp(self):
        """Initialize test client"""
        self.client = Client()
    
    def test_homepage_enquiry_post_valid_data(self):
        """Test homepage enquiry with valid data"""
        response = self.client.post(reverse('homepage_enquiry'), {
            'full_name': 'John Doe',
            'email': 'john@example.com',
            'phone': '1234567890',
            'enquiry_type': 'general',
            'project_details': 'Test project details'
        })
        
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data['success'])
        self.assertIn('Thank you', data['message'])
    
    def test_homepage_enquiry_post_missing_required_fields(self):
        """Test homepage enquiry with missing required fields"""
        # Test missing full_name
        response = self.client.post(reverse('homepage_enquiry'), {
            'email': 'john@example.com',
            'enquiry_type': 'general',
        })
        
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertFalse(data['success'])
        self.assertIn('required fields', data['message'])
        
        # Test missing email
        response = self.client.post(reverse('homepage_enquiry'), {
            'full_name': 'John Doe',
            'enquiry_type': 'general',
        })
        
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertFalse(data['success'])
        self.assertIn('required fields', data['message'])
        
        # Test missing enquiry_type
        response = self.client.post(reverse('homepage_enquiry'), {
            'full_name': 'John Doe',
            'email': 'john@example.com',
        })
        
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertFalse(data['success'])
        self.assertIn('required fields', data['message'])
    
    def test_homepage_enquiry_get_request(self):
        """Test homepage enquiry with GET request (should return error)"""
        response = self.client.get(reverse('homepage_enquiry'))
        
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertFalse(data['success'])
        self.assertIn('Invalid request method', data['message'])
    
    def test_homepage_enquiry_with_optional_fields(self):
        """Test homepage enquiry with optional fields included"""
        response = self.client.post(reverse('homepage_enquiry'), {
            'full_name': 'Jane Smith',
            'email': 'jane@example.com',
            'phone': '0987654321',
            'enquiry_type': 'custom_machining',
            'project_details': 'Detailed project description here'
        })
        
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data['success'])
        self.assertIn('Thank you', data['message'])


class ContactFormTestSuite(TestCase):
    """Test suite for contact form functionality"""
    
    def setUp(self):
        """Initialize test client"""
        self.client = Client()
    
    def test_contact_form_get_request(self):
        """Test GET request to contact form"""
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact/contact.html')
    
    def test_contact_form_post_valid_data(self):
        """Test contact form submission with valid data"""
        response = self.client.post(reverse('contact'), {
            'full_name': 'John Doe',
            'email': 'john@example.com',
            'phone': '1234567890',
            'cnc_machine_type': 'cnc_router',
            'project_details': 'I need a custom CNC router for my workshop'
        })
        
        # Should redirect back to contact page with success message
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('contact'))
        
        # Check that emails were sent
        self.assertEqual(len(mail.outbox), 2)  # Business email + customer confirmation
        
        # Check business email
        business_email = mail.outbox[0]
        self.assertIn('John Doe', business_email.subject)
        self.assertIn('cnc_router', business_email.subject)
        self.assertIn('john@example.com', business_email.body)
        
        # Check customer confirmation email
        customer_email = mail.outbox[1]
        self.assertEqual(customer_email.to, ['john@example.com'])
        self.assertIn('Quote Request Received', customer_email.subject)
    
    def test_contact_form_post_missing_required_fields(self):
        """Test contact form with missing required fields"""
        # Test missing full_name
        response = self.client.post(reverse('contact'), {
            'email': 'john@example.com',
            'cnc_machine_type': 'cnc_router',
            'project_details': 'Test details'
        })
        
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('contact'))
        
        # Check error message
        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(any('required fields' in str(m) for m in messages))
        
        # Test missing email
        response = self.client.post(reverse('contact'), {
            'full_name': 'John Doe',
            'cnc_machine_type': 'cnc_router',
            'project_details': 'Test details'
        })
        
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('contact'))
        
        # Test missing cnc_machine_type
        response = self.client.post(reverse('contact'), {
            'full_name': 'John Doe',
            'email': 'john@example.com',
            'project_details': 'Test details'
        })
        
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('contact'))
        
        # Test missing project_details
        response = self.client.post(reverse('contact'), {
            'full_name': 'John Doe',
            'email': 'john@example.com',
            'cnc_machine_type': 'cnc_router'
        })
        
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('contact'))
    
    def test_contact_form_with_optional_phone(self):
        """Test contact form with optional phone number"""
        response = self.client.post(reverse('contact'), {
            'full_name': 'Jane Smith',
            'email': 'jane@example.com',
            # No phone number
            'cnc_machine_type': 'cnc_mill',
            'project_details': 'Need CNC milling services'
        })
        
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('contact'))
        
        # Should still send emails
        self.assertEqual(len(mail.outbox), 2)
        
        # Business email should indicate no phone provided
        business_email = mail.outbox[0]
        self.assertIn('Not provided', business_email.body)
    
    @patch('home.views.send_mail')
    def test_contact_form_email_sending_failure(self, mock_send_mail):
        """Test contact form when email sending fails"""
        # Make send_mail raise an exception
        mock_send_mail.side_effect = Exception('Email sending failed')
        
        response = self.client.post(reverse('contact'), {
            'full_name': 'John Doe',
            'email': 'john@example.com',
            'phone': '1234567890',
            'cnc_machine_type': 'cnc_router',
            'project_details': 'Test project details'
        })
        
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('contact'))
        
        # Check error message
        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(any('error sending' in str(m) for m in messages))
    
    def test_contact_form_email_content_formatting(self):
        """Test that contact form emails are properly formatted"""
        response = self.client.post(reverse('contact'), {
            'full_name': 'Test User',
            'email': 'test@example.com',
            'phone': '555-123-4567',
            'cnc_machine_type': 'plasma_cutter',
            'project_details': 'Custom plasma cutting project with specific requirements'
        })
        
        self.assertEqual(response.status_code, 302)
        self.assertEqual(len(mail.outbox), 2)
        
        # Check business email formatting
        business_email = mail.outbox[0]
        self.assertIn('Test User', business_email.body)
        self.assertIn('test@example.com', business_email.body)
        self.assertIn('555-123-4567', business_email.body)
        self.assertIn('plasma_cutter', business_email.body)
        self.assertIn('Custom plasma cutting', business_email.body)
        
        # Check customer email formatting
        customer_email = mail.outbox[1]
        self.assertIn('Test User', customer_email.body)
        self.assertIn('Plasma Cutter', customer_email.body)  # Should be title-cased
    
    def test_contact_form_cnc_machine_type_formatting(self):
        """Test that CNC machine types are properly formatted in emails"""
        machine_types = [
            ('cnc_router', 'Cnc Router'),
            ('cnc_mill', 'Cnc Mill'),
            ('laser_cutter', 'Laser Cutter'),
            ('plasma_cutter', 'Plasma Cutter')
        ]
        
        for machine_type, expected_format in machine_types:
            # Clear previous emails
            mail.outbox.clear()
            
            response = self.client.post(reverse('contact'), {
                'full_name': 'Test User',
                'email': 'test@example.com',
                'cnc_machine_type': machine_type,
                'project_details': f'Test project for {machine_type}'
            })
            
            self.assertEqual(response.status_code, 302)
            self.assertEqual(len(mail.outbox), 2)
            
            # Check customer email has properly formatted machine type
            customer_email = mail.outbox[1]
            self.assertIn(expected_format, customer_email.body)
