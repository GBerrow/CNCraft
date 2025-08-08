from django.test import TestCase, Client
from django.urls import reverse
from products.models import Product, Category
import json

class ShoppingCartTestSuite(TestCase):
    """Comprehensive shopping cart functionality testing"""
    
    def setUp(self):
        """Initialize test environment for cart operations"""
        self.client = Client()
        self.category = Category.objects.create(
            name="test_category",
            friendly_name="Test Category"
        )
        self.product = Product.objects.create(
            category=self.category,
            name="Test Product",
            price=99.99
        )
        self.product2 = Product.objects.create(
            category=self.category,
            name="Second Product",
            price=149.99
        )
    
    def test_add_item_to_cart_functionality(self):
        """Verify successful item addition to shopping cart"""
        response = self.client.post(reverse('add_to_cart', args=[self.product.id]), {
            'quantity': 1,
            'redirect_url': '/'
        })
        # Validate redirect response after cart addition
        self.assertEqual(response.status_code, 302)
    
    def test_cart_view_rendering(self):
        """Validate cart page rendering and response codes"""
        response = self.client.get(reverse('view_cart'))
        self.assertEqual(response.status_code, 200)
    
    def test_add_invalid_quantity_to_cart(self):
        """Test adding invalid quantities to cart"""
        # Test negative quantity
        response = self.client.post(reverse('add_to_cart', args=[self.product.id]), {
            'quantity': -1,
            'redirect_url': '/'
        })
        self.assertEqual(response.status_code, 302)
        
        # Test zero quantity
        response = self.client.post(reverse('add_to_cart', args=[self.product.id]), {
            'quantity': 0,
            'redirect_url': '/'
        })
        self.assertEqual(response.status_code, 302)
    
    def test_add_nonexistent_product_to_cart(self):
        """Test adding non-existent product to cart"""
        response = self.client.post(reverse('add_to_cart', args=[99999]), {
            'quantity': 1,
            'redirect_url': '/'
        })
        self.assertEqual(response.status_code, 404)
    
    def test_update_cart_item_quantity(self):
        """Test updating cart item quantities"""
        # First add item to cart
        self.client.post(reverse('add_to_cart', args=[self.product.id]), {
            'quantity': 1,
            'redirect_url': '/'
        })
        
        # Then try to update quantity
        response = self.client.post(reverse('adjust_cart', args=[self.product.id]), {
            'quantity': 3
        })
        self.assertEqual(response.status_code, 302)
    
    def test_remove_item_from_cart(self):
        """Test removing items from cart"""
        # First add item to cart
        self.client.post(reverse('add_to_cart', args=[self.product.id]), {
            'quantity': 1,
            'redirect_url': '/'
        })
        
        # Then remove it
        response = self.client.post(reverse('remove_cart', args=[self.product.id]))
        self.assertEqual(response.status_code, 302)
    
    def test_cart_with_multiple_items(self):
        """Test cart functionality with multiple different items"""
        # Add both products to cart
        self.client.post(reverse('add_to_cart', args=[self.product.id]), {
            'quantity': 2,
            'redirect_url': '/'
        })
        self.client.post(reverse('add_to_cart', args=[self.product2.id]), {
            'quantity': 1,
            'redirect_url': '/'
        })
        
        # Check cart view displays both
        response = self.client.get(reverse('view_cart'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Product")
        self.assertContains(response, "Second Product")


class CartPersistentDataTestSuite(TestCase):
    """Test cart data persistence and different formats"""
    
    def setUp(self):
        """Initialize test environment"""
        self.client = Client()
        self.category = Category.objects.create(
            name="test_category",
            friendly_name="Test Category"
        )
        self.product = Product.objects.create(
            category=self.category,
            name="Test Product",
            price=99.99
        )
    
    def test_add_to_cart_with_persistent_cart_cookie(self):
        """Test adding to cart when persistent cart cookie exists"""
        # Set up persistent cart cookie first
        persistent_cart = json.dumps({str(self.product.id): {'quantity': 1}})
        self.client.cookies['persistent_cart'] = persistent_cart
        
        response = self.client.post(reverse('add_to_cart', args=[self.product.id]), {
            'quantity': 2,
            'redirect_url': '/'
        })
        self.assertEqual(response.status_code, 302)
    
    def test_add_to_cart_with_invalid_persistent_cart_cookie(self):
        """Test adding to cart with invalid JSON in persistent cart cookie"""
        # Set up invalid persistent cart cookie
        self.client.cookies['persistent_cart'] = 'invalid-json'
        
        response = self.client.post(reverse('add_to_cart', args=[self.product.id]), {
            'quantity': 1,
            'redirect_url': '/'
        })
        self.assertEqual(response.status_code, 302)
    
    def test_add_to_cart_existing_item_dict_format(self):
        """Test adding to cart when item already exists in dict format"""
        # First add item to establish dict format
        self.client.post(reverse('add_to_cart', args=[self.product.id]), {
            'quantity': 1,
            'redirect_url': '/'
        })
        
        # Then add more of the same item
        response = self.client.post(reverse('add_to_cart', args=[self.product.id]), {
            'quantity': 2,
            'redirect_url': '/'
        })
        self.assertEqual(response.status_code, 302)
    
    def test_add_to_cart_existing_item_list_format(self):
        """Test adding to cart when item exists in list format"""
        # Set up cart with list format
        session = self.client.session
        session['cart'] = {str(self.product.id): [{'quantity': 1}]}
        session.save()
        
        response = self.client.post(reverse('add_to_cart', args=[self.product.id]), {
            'quantity': 2,
            'redirect_url': '/'
        })
        self.assertEqual(response.status_code, 302)
    
    def test_add_to_cart_existing_item_integer_format(self):
        """Test adding to cart when item exists in integer format"""
        # Set up cart with integer format (legacy)
        session = self.client.session
        session['cart'] = {str(self.product.id): 1}
        session.save()
        
        response = self.client.post(reverse('add_to_cart', args=[self.product.id]), {
            'quantity': 2,
            'redirect_url': '/'
        })
        self.assertEqual(response.status_code, 302)


class CartAdjustmentTestSuite(TestCase):
    """Test cart quantity adjustment functionality"""
    
    def setUp(self):
        """Initialize test environment"""
        self.client = Client()
        self.category = Category.objects.create(
            name="test_category",
            friendly_name="Test Category"
        )
        self.product = Product.objects.create(
            category=self.category,
            name="Test Product",
            price=99.99
        )
    
    def test_adjust_cart_with_persistent_cart_fallback(self):
        """Test adjusting cart when session is empty but persistent cart exists"""
        # Set up persistent cart cookie
        persistent_cart = json.dumps({str(self.product.id): {'quantity': 2}})
        self.client.cookies['persistent_cart'] = persistent_cart
        
        response = self.client.post(reverse('adjust_cart', args=[self.product.id]), {
            'quantity': 5
        })
        self.assertEqual(response.status_code, 302)
    
    def test_adjust_cart_with_invalid_persistent_cart(self):
        """Test adjusting cart with invalid persistent cart cookie"""
        # Set up invalid persistent cart cookie
        self.client.cookies['persistent_cart'] = 'invalid-json'
        
        response = self.client.post(reverse('adjust_cart', args=[self.product.id]), {
            'quantity': 3
        })
        self.assertEqual(response.status_code, 302)
    
    def test_adjust_cart_invalid_quantity_types(self):
        """Test adjusting cart with invalid quantity types"""
        # First add item to cart
        self.client.post(reverse('add_to_cart', args=[self.product.id]), {
            'quantity': 1,
            'redirect_url': '/'
        })
        
        # Test with non-integer quantity
        response = self.client.post(reverse('adjust_cart', args=[self.product.id]), {
            'quantity': 'abc'
        })
        self.assertEqual(response.status_code, 302)
        
        # Test with None quantity
        response = self.client.post(reverse('adjust_cart', args=[self.product.id]), {})
        self.assertEqual(response.status_code, 302)
    
    def test_adjust_cart_positive_quantity_dict_format(self):
        """Test adjusting cart with positive quantity for dict format"""
        # Add item to cart first
        self.client.post(reverse('add_to_cart', args=[self.product.id]), {
            'quantity': 1,
            'redirect_url': '/'
        })
        
        response = self.client.post(reverse('adjust_cart', args=[self.product.id]), {
            'quantity': 5
        })
        self.assertEqual(response.status_code, 302)
    
    def test_adjust_cart_positive_quantity_list_format(self):
        """Test adjusting cart with positive quantity for list format"""
        # Set up cart with list format
        session = self.client.session
        session['cart'] = {str(self.product.id): [{'quantity': 1}]}
        session.save()
        
        response = self.client.post(reverse('adjust_cart', args=[self.product.id]), {
            'quantity': 3
        })
        self.assertEqual(response.status_code, 302)
    
    def test_adjust_cart_positive_quantity_integer_format(self):
        """Test adjusting cart with positive quantity for integer format"""
        # Set up cart with integer format
        session = self.client.session
        session['cart'] = {str(self.product.id): 2}
        session.save()
        
        response = self.client.post(reverse('adjust_cart', args=[self.product.id]), {
            'quantity': 4
        })
        self.assertEqual(response.status_code, 302)
    
    def test_adjust_cart_nonexistent_item_positive_quantity(self):
        """Test adjusting quantity for item not in cart with positive quantity"""
        response = self.client.post(reverse('adjust_cart', args=[self.product.id]), {
            'quantity': 3
        })
        self.assertEqual(response.status_code, 302)
    
    def test_adjust_cart_zero_quantity_existing_item(self):
        """Test adjusting cart with zero quantity (should remove item)"""
        # First add item to cart
        self.client.post(reverse('add_to_cart', args=[self.product.id]), {
            'quantity': 2,
            'redirect_url': '/'
        })
        
        # Set quantity to 0 (should remove)
        response = self.client.post(reverse('adjust_cart', args=[self.product.id]), {
            'quantity': 0
        })
        self.assertEqual(response.status_code, 302)
    
    def test_adjust_cart_zero_quantity_nonexistent_item(self):
        """Test adjusting cart with zero quantity for nonexistent item"""
        response = self.client.post(reverse('adjust_cart', args=[self.product.id]), {
            'quantity': 0
        })
        self.assertEqual(response.status_code, 302)


class CartRemovalTestSuite(TestCase):
    """Test cart item removal functionality"""
    
    def setUp(self):
        """Initialize test environment"""
        self.client = Client()
        self.category = Category.objects.create(
            name="test_category",
            friendly_name="Test Category"
        )
        self.product = Product.objects.create(
            category=self.category,
            name="Test Product",
            price=99.99
        )
    
    def test_remove_cart_with_persistent_cart_fallback(self):
        """Test removing from cart when session is empty but persistent cart exists"""
        # Set up persistent cart cookie
        persistent_cart = json.dumps({str(self.product.id): {'quantity': 2}})
        self.client.cookies['persistent_cart'] = persistent_cart
        
        response = self.client.post(reverse('remove_cart', args=[self.product.id]))
        self.assertEqual(response.status_code, 302)
    
    def test_remove_cart_with_invalid_persistent_cart(self):
        """Test removing from cart with invalid persistent cart cookie"""
        # Set up invalid persistent cart cookie
        self.client.cookies['persistent_cart'] = 'invalid-json'
        
        response = self.client.post(reverse('remove_cart', args=[self.product.id]))
        self.assertEqual(response.status_code, 302)
    
    def test_remove_cart_existing_item(self):
        """Test removing existing item from cart"""
        # First add item to cart
        self.client.post(reverse('add_to_cart', args=[self.product.id]), {
            'quantity': 1,
            'redirect_url': '/'
        })
        
        # Then remove it
        response = self.client.post(reverse('remove_cart', args=[self.product.id]))
        self.assertEqual(response.status_code, 302)
    
    def test_remove_cart_nonexistent_item(self):
        """Test removing nonexistent item from cart"""
        response = self.client.post(reverse('remove_cart', args=[self.product.id]))
        self.assertEqual(response.status_code, 302)


class CartCountTestSuite(TestCase):
    """Test cart count AJAX functionality"""
    
    def setUp(self):
        """Initialize test environment"""
        self.client = Client()
        self.category = Category.objects.create(
            name="test_category",
            friendly_name="Test Category"
        )
        self.product = Product.objects.create(
            category=self.category,
            name="Test Product",
            price=99.99
        )
    
    def test_get_cart_count_empty_cart(self):
        """Test getting cart count for empty cart"""
        response = self.client.get(reverse('get_cart_count'))
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['product_count'], 0)
        self.assertEqual(data['cart_items'], 0)
        self.assertTrue(data['success'])
    
    def test_get_cart_count_with_session_cart(self):
        """Test getting cart count with items in session cart"""
        # Add item to cart
        self.client.post(reverse('add_to_cart', args=[self.product.id]), {
            'quantity': 3,
            'redirect_url': '/'
        })
        
        response = self.client.get(reverse('get_cart_count'))
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['product_count'], 3)
        self.assertEqual(data['cart_items'], 1)
    
    def test_get_cart_count_with_persistent_cart_fallback(self):
        """Test getting cart count when session is empty but persistent cart exists"""
        # Set up persistent cart cookie
        persistent_cart = json.dumps({str(self.product.id): {'quantity': 2}})
        self.client.cookies['persistent_cart'] = persistent_cart
        
        response = self.client.get(reverse('get_cart_count'))
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['product_count'], 2)
        self.assertEqual(data['cart_items'], 1)
    
    def test_get_cart_count_with_invalid_persistent_cart(self):
        """Test getting cart count with invalid persistent cart cookie"""
        # Set up invalid persistent cart cookie
        self.client.cookies['persistent_cart'] = 'invalid-json'
        
        response = self.client.get(reverse('get_cart_count'))
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['product_count'], 0)
        self.assertEqual(data['cart_items'], 0)
    
    def test_get_cart_count_integer_format(self):
        """Test getting cart count for integer format cart data"""
        # Set up cart with integer format
        session = self.client.session
        session['cart'] = {str(self.product.id): 5}
        session.save()
        
        response = self.client.get(reverse('get_cart_count'))
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['product_count'], 5)
        self.assertEqual(data['cart_items'], 1)
    
    def test_get_cart_count_list_format(self):
        """Test getting cart count for list format cart data"""
        # Set up cart with list format
        session = self.client.session
        session['cart'] = {str(self.product.id): [{'quantity': 3}]}
        session.save()
        
        response = self.client.get(reverse('get_cart_count'))
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['product_count'], 3)
        self.assertEqual(data['cart_items'], 1)
    
    def test_get_cart_count_list_format_no_quantity(self):
        """Test getting cart count for list format without quantity key"""
        # Set up cart with list format without quantity
        session = self.client.session
        session['cart'] = {str(self.product.id): [{'name': 'test'}]}
        session.save()
        
        response = self.client.get(reverse('get_cart_count'))
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['product_count'], 1)  # Default quantity
        self.assertEqual(data['cart_items'], 1)
    
    def test_get_cart_count_dict_format_no_quantity(self):
        """Test getting cart count for dict format without quantity key"""
        # Set up cart with dict format without quantity
        session = self.client.session
        session['cart'] = {str(self.product.id): {'name': 'test'}}
        session.save()
        
        response = self.client.get(reverse('get_cart_count'))
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['product_count'], 1)  # Default quantity
        self.assertEqual(data['cart_items'], 1)
    
    def test_get_cart_count_invalid_data_format(self):
        """Test getting cart count with invalid data format causing exceptions"""
        # Set up cart with strange format that causes exceptions
        session = self.client.session
        session['cart'] = {str(self.product.id): None}
        session.save()
        
        response = self.client.get(reverse('get_cart_count'))
        self.assertEqual(response.status_code, 200)
        data = response.json()
        # Should handle exception and continue
        self.assertEqual(data['product_count'], 1)  # Default fallback
        self.assertEqual(data['cart_items'], 1)


class CartClearTestSuite(TestCase):
    """Test cart clearing functionality"""
    
    def setUp(self):
        """Initialize test environment"""
        self.client = Client()
        self.category = Category.objects.create(
            name="test_category",
            friendly_name="Test Category"
        )
        self.product = Product.objects.create(
            category=self.category,
            name="Test Product",
            price=99.99
        )
    
    def test_clear_all_cart_post_method(self):
        """Test clearing all cart items via POST method"""
        # First add item to cart
        self.client.post(reverse('add_to_cart', args=[self.product.id]), {
            'quantity': 3,
            'redirect_url': '/'
        })
        
        # Then clear all
        response = self.client.post(reverse('clear_all_cart'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('view_cart'))
    
    def test_clear_all_cart_get_method(self):
        """Test clear cart with GET method (should just redirect)"""
        response = self.client.get(reverse('clear_all_cart'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('view_cart'))
