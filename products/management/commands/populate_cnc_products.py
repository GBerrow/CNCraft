from django.core.management.base import BaseCommand
from products.models import Category, Product

class Command(BaseCommand):
    help = 'Populate the database with CNC equipment and categories'

    def handle(self, *args, **options):
        self.stdout.write('Populating CNC products and categories...')

        # Clear existing data (optional - comment out if you want to keep existing data)
        # Product.objects.all().delete()
        # Category.objects.all().delete()

        # Create Categories
        categories_data = [
            {
                'name': 'cnc_machines',
                'friendly_name': 'CNC Machines',
                'description': 'Professional CNC milling machines and machining centers for precision manufacturing'
            },
            {
                'name': 'cnc_lathes',
                'friendly_name': 'CNC Lathes',
                'description': 'CNC turning centers and lathes for precision cylindrical parts manufacturing'
            },
            {
                'name': 'cnc_routers',
                'friendly_name': 'CNC Routers',
                'description': 'CNC routers for woodworking, sign making, and material cutting applications'
            },
            {
                'name': 'cutting_tools',
                'friendly_name': 'Cutting Tools',
                'description': 'End mills, drill bits, and cutting tool sets for CNC machining'
            },
            {
                'name': 'workholding',
                'friendly_name': 'Workholding',
                'description': 'Vises, clamps, and workholding solutions for secure part fixturing'
            },
            {
                'name': 'accessories',
                'friendly_name': 'Accessories',
                'description': 'CNC accessories, tooling, and support equipment'
            }
        ]

        # Create or get categories
        category_objects = {}
        for cat_data in categories_data:
            category, created = Category.objects.get_or_create(
                name=cat_data['name'],
                defaults={
                    'friendly_name': cat_data['friendly_name'],
                    'description': cat_data['description']
                }
            )
            category_objects[cat_data['name']] = category
            if created:
                self.stdout.write(f'Created category: {category.friendly_name}')
            else:
                self.stdout.write(f'Category already exists: {category.friendly_name}')

        # Create Products
        products_data = [
            # CNC MACHINES
            {
                'category': category_objects['cnc_machines'],
                'sku': 'CNC-MILL-2418',
                'name': 'Desktop CNC Mill 2418',
                'description': 'Compact desktop CNC mill ideal for small parts machining, prototyping, and educational use. Features precision ball screws and stepper motors for accurate positioning. Perfect for hobbyists and small workshops.',
                'price': 2499.99,
                'dimensions': '600x450x350mm',
                'weight': 85.00,
                'material': 'Cast Iron Frame',
                'power_requirement': '220V, 800W Spindle',
                'working_area': '240x180x100mm',
                'spindle_speed': '0-8000 RPM',
                'rating': 4.2,
                'in_stock': True,
                'stock_qty': 15,
                'featured': True
            },
            {
                'category': category_objects['cnc_machines'],
                'sku': 'CNC-MILL-3020',
                'name': 'Professional CNC Router 3020',
                'description': 'High-precision CNC router perfect for professional woodworking, plastic cutting, and light metal work. Features advanced DSP controller and automatic tool length sensor.',
                'price': 3299.99,
                'discount_price': 2999.99,
                'dimensions': '650x520x400mm',
                'weight': 120.00,
                'material': 'Aluminum Frame',
                'power_requirement': '220V, 1.5kW Spindle',
                'working_area': '300x200x100mm',
                'spindle_speed': '0-24000 RPM',
                'rating': 4.5,
                'in_stock': True,
                'stock_qty': 8,
                'featured': True
            },
            {
                'category': category_objects['cnc_machines'],
                'sku': 'CNC-MILL-4030',
                'name': 'Industrial CNC Mill 4030',
                'description': 'Heavy-duty industrial CNC milling machine for professional manufacturing. Rigid cast iron construction with high-precision linear guides and servo motors.',
                'price': 12999.99,
                'dimensions': '1200x800x600mm',
                'weight': 450.00,
                'material': 'Cast Iron & Steel Construction',
                'power_requirement': '380V, 5kW Spindle',
                'working_area': '400x300x200mm',
                'spindle_speed': '0-12000 RPM',
                'rating': 4.8,
                'in_stock': True,
                'stock_qty': 3,
                'featured': True
            },
            {
                'category': category_objects['cnc_machines'],
                'sku': 'CNC-MILL-6040',
                'name': 'CNC Machining Center 6040',
                'description': 'Advanced CNC machining center with 20-tool automatic tool changer and flood coolant system. Perfect for high-volume production environments.',
                'price': 24999.99,
                'dimensions': '1800x1200x800mm',
                'weight': 850.00,
                'material': 'Cast Iron Base with Steel Column',
                'power_requirement': '380V, 7.5kW Spindle',
                'working_area': '600x400x300mm',
                'spindle_speed': '0-15000 RPM',
                'rating': 4.9,
                'in_stock': True,
                'stock_qty': 2
            },

            # CNC LATHES
            {
                'category': category_objects['cnc_lathes'],
                'sku': 'CNC-LATHE-0618',
                'name': 'Mini CNC Lathe 0618',
                'description': 'Compact CNC lathe perfect for small turning operations, jewelry making, and precision parts. Easy to operate and maintain with user-friendly control system.',
                'price': 1899.99,
                'dimensions': '800x400x350mm',
                'weight': 75.00,
                'material': 'Cast Iron Bed',
                'power_requirement': '220V, 550W Motor',
                'working_area': '150x300mm (Swing x Length)',
                'spindle_speed': '50-2500 RPM',
                'rating': 4.1,
                'in_stock': True,
                'stock_qty': 12
            },
            {
                'category': category_objects['cnc_lathes'],
                'sku': 'CNC-LATHE-0925',
                'name': 'CNC Turning Center 0925',
                'description': 'Professional CNC lathe with live tooling capability and C-axis functionality. Ideal for complex turning operations and complete part machining.',
                'price': 18999.99,
                'discount_price': 16999.99,
                'dimensions': '2200x1000x600mm',
                'weight': 1200.00,
                'material': 'Cast Iron Construction',
                'power_requirement': '380V, 11kW Main Motor',
                'working_area': '250x500mm (Swing x Length)',
                'spindle_speed': '50-4000 RPM',
                'rating': 4.7,
                'in_stock': True,
                'stock_qty': 4,
                'featured': True
            },

            # CNC ROUTERS
            {
                'category': category_objects['cnc_routers'],
                'sku': 'CNC-RTR-1325',
                'name': 'CNC Wood Router 1325',
                'description': 'Large format CNC router designed for woodworking, sign making, and furniture production. Includes dust collection system and vacuum table.',
                'price': 8999.99,
                'dimensions': '2800x1800x600mm',
                'weight': 380.00,
                'material': 'Welded Steel Frame',
                'power_requirement': '220V, 3kW Water-Cooled Spindle',
                'working_area': '1300x2500x200mm',
                'spindle_speed': '0-18000 RPM',
                'rating': 4.4,
                'in_stock': True,
                'stock_qty': 6
            },
            {
                'category': category_objects['cnc_routers'],
                'sku': 'CNC-RTR-6090',
                'name': 'CNC Router 6090',
                'description': 'Mid-size CNC router perfect for prototyping and small production runs. Suitable for wood, plastic, aluminum, and composite materials.',
                'price': 4599.99,
                'dimensions': '1800x1200x500mm',
                'weight': 220.00,
                'material': 'Aluminum & Steel Frame',
                'power_requirement': '220V, 2.2kW Air-Cooled Spindle',
                'working_area': '600x900x100mm',
                'spindle_speed': '0-24000 RPM',
                'rating': 4.3,
                'in_stock': True,
                'stock_qty': 9
            },

            # CUTTING TOOLS
            {
                'category': category_objects['cutting_tools'],
                'sku': 'CT-EM-SET-20',
                'name': 'Carbide End Mill Set (20pc)',
                'description': 'Professional carbide end mill set for CNC machining. Includes 2, 4, 6, 8, 10, 12mm sizes with various flute counts and coatings for different materials.',
                'price': 299.99,
                'dimensions': '200x150x50mm',
                'weight': 2.50,
                'material': 'Solid Carbide with TiAlN Coating',
                'rating': 4.6,
                'in_stock': True,
                'stock_qty': 45,
                'featured': True
            },
            {
                'category': category_objects['cutting_tools'],
                'sku': 'CT-DR-SET-HSS',
                'name': 'HSS Drill Bit Set (50pc)',
                'description': 'High-speed steel drill bit set for general purpose drilling in steel, aluminum, and plastic. Sizes from 1mm to 10mm in 0.1mm increments.',
                'price': 89.99,
                'dimensions': '300x200x30mm',
                'weight': 1.20,
                'material': 'High Speed Steel (HSS)',
                'rating': 4.2,
                'in_stock': True,
                'stock_qty': 67
            },
            {
                'category': category_objects['cutting_tools'],
                'sku': 'CT-EM-6MM-4FL',
                'name': '6mm 4-Flute End Mill',
                'description': 'Premium 6mm 4-flute carbide end mill for aluminum and steel machining. Uncoated carbide for excellent surface finish and long tool life.',
                'price': 24.99,
                'dimensions': '75x6x6mm',
                'weight': 0.05,
                'material': 'Solid Carbide (Uncoated)',
                'rating': 4.8,
                'in_stock': True,
                'stock_qty': 120
            },
            {
                'category': category_objects['cutting_tools'],
                'sku': 'CT-FB-SET-10',
                'name': 'Face Mill Cutter Set (10pc)',
                'description': 'Indexable face mill cutter set with carbide inserts. Perfect for large surface machining and heavy material removal operations.',
                'price': 449.99,
                'discount_price': 399.99,
                'dimensions': '150x100x80mm',
                'weight': 3.20,
                'material': 'Steel Body with Carbide Inserts',
                'rating': 4.5,
                'in_stock': True,
                'stock_qty': 22
            },

            # WORKHOLDING
            {
                'category': category_objects['workholding'],
                'sku': 'WH-VISE-4IN',
                'name': '4" Precision Machine Vise',
                'description': 'High-precision machine vise for CNC applications. Hardened and ground jaws with 0.0002" accuracy for reliable workholding.',
                'price': 189.99,
                'dimensions': '200x100x80mm',
                'weight': 8.50,
                'material': 'Cast Iron with Hardened Steel Jaws',
                'rating': 4.5,
                'in_stock': True,
                'stock_qty': 28
            },
            {
                'category': category_objects['workholding'],
                'sku': 'WH-CLAMP-SET',
                'name': 'T-Slot Clamp Set (12pc)',
                'description': 'Complete T-slot clamping set for securing workpieces on CNC machine tables. Includes step clamps, studs, nuts, and washers.',
                'price': 149.99,
                'dimensions': '300x200x100mm',
                'weight': 5.20,
                'material': 'Hardened Steel',
                'rating': 4.4,
                'in_stock': True,
                'stock_qty': 33
            },
            {
                'category': category_objects['workholding'],
                'sku': 'WH-CHUCK-6IN',
                'name': '6" 3-Jaw Chuck',
                'description': 'Self-centering 3-jaw chuck for CNC lathe applications. Hardened jaws with excellent repeatability for round stock.',
                'price': 299.99,
                'dimensions': '150x150x80mm',
                'weight': 12.00,
                'material': 'Cast Iron with Steel Jaws',
                'rating': 4.6,
                'in_stock': True,
                'stock_qty': 15
            },

            # ACCESSORIES
            {
                'category': category_objects['accessories'],
                'sku': 'ACC-COOLANT-SYS',
                'name': 'CNC Coolant System',
                'description': 'Professional flood coolant system for CNC machines. Includes centrifugal pump, 20L tank, filtration system, and adjustable nozzles.',
                'price': 599.99,
                'dimensions': '400x300x500mm',
                'weight': 25.00,
                'material': 'Stainless Steel Tank',
                'power_requirement': '220V, 0.5kW Pump Motor',
                'rating': 4.3,
                'in_stock': True,
                'stock_qty': 15
            },
            {
                'category': category_objects['accessories'],
                'sku': 'ACC-PROBE-TOUCH',
                'name': 'Wireless Touch Probe System',
                'description': 'High-precision wireless touch probe for automated part setup and in-process measurement. Battery powered with LED status indicators.',
                'price': 1299.99,
                'dimensions': '50x50x100mm',
                'weight': 0.25,
                'material': 'Stainless Steel Probe with Electronics',
                'rating': 4.7,
                'in_stock': True,
                'stock_qty': 8
            },
            {
                'category': category_objects['accessories'],
                'sku': 'ACC-TOOL-SETTER',
                'name': 'Automatic Tool Setter',
                'description': 'Precision tool setter for automatic tool length measurement and compensation. Compatible with most CNC controllers.',
                'price': 899.99,
                'dimensions': '100x100x150mm',
                'weight': 2.50,
                'material': 'Hardened Steel Base',
                'power_requirement': '24V DC',
                'rating': 4.4,
                'in_stock': True,
                'stock_qty': 12
            }
        ]

        # Create products
        created_count = 0
        for product_data in products_data:
            product, created = Product.objects.get_or_create(
                sku=product_data['sku'],
                defaults=product_data
            )
            if created:
                self.stdout.write(f'Created product: {product.name}')
                created_count += 1
            else:
                self.stdout.write(f'Product already exists: {product.name}')

        self.stdout.write(
            self.style.SUCCESS(
                f'Successfully processed {len(categories_data)} categories and created {created_count} new products'
            )
        ) 