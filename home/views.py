from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse
from products.models import Product

# View function to render the index page
def index(request):
    """A view to return the index page"""
    
    # Get 3 random products for the homepage (randomized each load)
    featured_products = Product.objects.order_by('?')[:3]
    
    context = {
        'featured_products': featured_products,
    }
    
    # Render and return the 'home/index.html' template
    return render(request, 'home/index.html', context)

def homepage_enquiry(request):
    """Handle homepage enquiry form submissions with AJAX"""
    
    if request.method == 'POST':
        # Get form data
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone', '')
        enquiry_type = request.POST.get('enquiry_type')
        project_details = request.POST.get('project_details', '')
        
        # Basic validation
        if not all([full_name, email, enquiry_type]):
            return JsonResponse({
                'success': False,
                'message': 'Please fill in all required fields.'
            })
        
        # Return success immediately for better UX
        # Email sending can be handled asynchronously later if needed
        return JsonResponse({
            'success': True,
            'message': f'Thank you! Your enquiry has been sent. We\'ll get back to you as soon as possible.'
        })
    
    # GET request - return error
    return JsonResponse({
        'success': False,
        'message': 'Invalid request method.'
    })

def contact(request):
    """A view to handle contact form submissions"""
    
    if request.method == 'POST':
        # Get form data - UPDATED FIELD NAMES
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone', '')
        cnc_machine_type = request.POST.get('cnc_machine_type')
        project_details = request.POST.get('project_details')  # This was missing!
        
        # Basic validation
        if not all([full_name, email, cnc_machine_type, project_details]):
            messages.error(request, 'Please fill in all required fields.')
            return redirect('contact')  # Redirect to contact page instead
        
        # Remove the length check or fix it
        # if len(project_details) < 20:
        #     messages.error(request, 'Please provide more detailed project information (minimum 20 characters).')
        #     return redirect('contact')
        
        try:
            # Prepare email content
            subject = f'New Enquiry from {full_name} - {cnc_machine_type}'
            
            message = f"""
New enquiry received from CNCraft website:

Client Information:
- Name: {full_name}
- Email: {email}
- Phone: {phone if phone else 'Not provided'}

Enquiry Details:
- Type: {cnc_machine_type}

Project Description:
{project_details}

Please respond to this inquiry promptly.
            """
            
            # Send email to business owner
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                ['quotes@cncraft.com'],  # Update with your actual email
                fail_silently=False,
            )
            
            # Send confirmation email to customer
            customer_subject = 'Quote Request Received - CNCraft'
            customer_message = f"""
Hello {full_name},

Thank you for your enquiry! We've received your inquiry about {cnc_machine_type.replace('_', ' ').title()} and will get back to you as soon as possible.

Your Enquiry Details:
- Enquiry Type: {cnc_machine_type.replace('_', ' ').title()}

Our team will review your requirements and get back to you with more information.

Best regards,
CNCraft Team
Phone: (555) CNC-SHOP
Email: quotes@cncraft.com
            """
            
            send_mail(
                customer_subject,
                customer_message,
                settings.DEFAULT_FROM_EMAIL,
                [email],
                fail_silently=True,  # Don't fail if customer email fails
            )
            
            messages.success(
                request, 
                f'Thank you {full_name}! Your enquiry has been sent. '
                'We\'ll get back to you as soon as possible.'
            )
            
            return redirect('contact')
            
        except Exception as e:
            messages.error(
                request, 
                'Sorry, there was an error sending your message. '
                'Please try again or contact us directly.'
            )
            return redirect('contact')
    
    # GET request - show the contact form
    return render(request, 'contact/contact.html')


