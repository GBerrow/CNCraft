from django.db import models
from django.urls import reverse
import os
from django.conf import settings

class Category(models.Model):
    """
    Model for product categories.
    """
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='category_images/', null=True, blank=True)
    
    class Meta:
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name
    
    def get_friendly_name(self):
        return self.friendly_name
    
    def get_absolute_url(self):
        return reverse('products_by_category', args=[self.id])


class Product(models.Model):
    """
    Model for CNC products with detailed specifications.
    """
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)
    
    # CNC-specific fields
    dimensions = models.CharField(max_length=100, null=True, blank=True, help_text="Format: LxWxH in mm")
    weight = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True, help_text="Weight in kg")
    material = models.CharField(max_length=100, null=True, blank=True)
    
    # Technical specifications
    power_requirement = models.CharField(max_length=100, null=True, blank=True)
    working_area = models.CharField(max_length=100, null=True, blank=True)
    spindle_speed = models.CharField(max_length=100, null=True, blank=True)
    
    # Stock and rating information
    rating = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    in_stock = models.BooleanField(default=True)
    stock_qty = models.IntegerField(default=0)
    featured = models.BooleanField(default=False)
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('product_detail', args=[self.id])
    
    def get_display_price(self):
        """Returns the discount price if available, otherwise the regular price"""
        if self.discount_price:
            return self.discount_price
        return self.price
    
    def is_on_sale(self):
        """Check if the product is currently on sale"""
        return self.discount_price is not None and self.discount_price < self.price
    
    def get_product_images(self):
        """
        Get all available images for this product from static directory.
        Returns a list of image paths that exist.
        """
        images = []
        
        # Map product names to their specific image files
        product_image_mappings = {
            # CNC Mills - each product gets only its specific images
            'Desktop CNC Mill 2418': [
                'images/products/cnc-mills/Desktop_CNC_Mill_2418_1.jpg',
                'images/products/cnc-mills/Desktop_CNC_Mill_2418_2.jpg'
            ],
            'Professional CNC Router 3020': [
                'images/products/cnc-mills/Professional_CNC_Router_3020_1.jpg',
                'images/products/cnc-mills/Professional_CNC_Router_3020_2.jpg',
                'images/products/cnc-mills/Professional_CNC_Router_3020_3.jpg'
            ],
            'Industrial CNC Mill 4030': [
                'images/products/cnc-mills/Industrial_CNC_Mill_4030_1.jpg',
                'images/products/cnc-mills/Industrial_CNC_Mill_4030_2.jpg'
            ],
            'CNC Machining Center 6040': [
                'images/products/cnc-mills/CNC_Machining_Center_6040_1.jpg',
                'images/products/cnc-mills/CNC_Machining_Center_6040_2.jpg'
            ],
            
            # CNC Lathes - each product gets only its specific images
            'Mini CNC Lathe 0618': [
                'images/products/cnc-lathes/Mini_CNC_Lathe_0618_1.jpg',
                'images/products/cnc-lathes/Mini_CNC_Lathe_0618_2.jpg'
            ],
            'CNC Turning Center 0925': [
                'images/products/cnc-lathes/CNC_Turning_Center_0925_1.jpg',
                'images/products/cnc-lathes/CNC_Turning_Center_0925_2.jpg'
            ],
            
            # CNC Routers - each product gets only its specific images
            'CNC Wood Router 1325': [
                'images/products/cnc-routers/CNC_Wood_Router_1325_1.jpg',
                'images/products/cnc-routers/CNC_Wood_Router_1325_2.jpg'
            ],
            'CNC Router 6090': [
                'images/products/cnc-routers/CNC_Router_6090_1.jpg',
                'images/products/cnc-routers/CNC_Router_6090_2.jpg'
            ],
            
            # Cutting Tools - each product gets only its specific images
            'Carbide End Mill Set (20pc)': [
                'images/products/tools/End_Mill_Set_1.jpg',
                'images/products/tools/End_Mill_Set_2.jpg'
            ],
            'HSS Drill Bit Set (50pc)': [
                'images/products/tools/Drill_Bit_Set.jpg'
            ],
            '6mm 4-Flute End Mill': [
                'images/products/tools/6mm_4-Flute_End_Mill_1.jpg'
            ],
            'Face Mill Cutter Set (10pc)': [
                'images/products/tools/Face_Mill_Cutter_Set_1.jpg',
                'images/products/tools/Face_Mill_Cutter_Set_2.jpg'
            ],
            
            # Workholding - each product gets only its specific images
            '4" Precision Machine Vise': [
                'images/products/workholding/Precision_Machine_Vise_1.jpg',
                'images/products/workholding/Precision_Machine_Vise_2.jpg'
            ],
            'T-Slot Clamp Set (12pc)': [
                'images/products/workholding/T-Slot_Clamp_Set_1.jpg',
                'images/products/workholding/T-Slot_Clamp_Set_2.jpg'
            ],
            '6" 3-Jaw Chuck': [
                'images/products/workholding/3-Jaw_Lathe_Chuck_1.jpg',
                'images/products/workholding/3-Jaw_Lathe_Chuck_2.jpg',
                'images/products/workholding/3-Jaw_Lathe_Chuck_3.jpg'
            ],
            
            # Accessories - each product gets only its specific images
            'CNC Coolant System': [
                'images/products/accessories/CNC_Coolant_System_1.jpg',
                'images/products/accessories/CNC_Coolant_System_2.jpg'
            ],
            'Wireless Touch Probe System': [
                'images/products/accessories/Wireless_Touch_Probe_System_1.jpg',
                'images/products/accessories/Wireless_Touch_Probe_System_2.jpg'
            ],
            'Automatic Tool Setter': [
                'images/products/accessories/Automatic_Tool_Setter_1.jpg'
            ],
        }
        
        # Get the specific images for this product
        product_images = product_image_mappings.get(self.name, [])
        
        # Check which images actually exist and add them to the list
        for image_path in product_images:
            full_path = os.path.join(settings.BASE_DIR, 'static', image_path)
            if os.path.exists(full_path):
                images.append(image_path)
        
        # Sort images to ensure consistent order
        images.sort()
        return images
    
    def _image_belongs_to_product(self, filename, patterns):
        """
        This method is no longer used with the new precise mapping system.
        Kept for backward compatibility but not called.
        """
        return False
    
    def get_main_image(self):
        """
        Get the main/primary image for this product.
        Returns the first available image or a default.
        """
        images = self.get_product_images()
        if images:
            return images[0]
        return 'images/no-image.png'


class ProductImage(models.Model):
    """
    Model for additional product images.
    """
    product = models.ForeignKey(Product, related_name='additional_images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images/')
    alt_text = models.CharField(max_length=254, null=True, blank=True)
    is_feature = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Image for {self.product.name}"
