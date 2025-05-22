from django.db import models
from django.urls import reverse

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
