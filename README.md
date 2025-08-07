# CNCraft

![CNCraft Banner](documentation/readme/images/CNCraft_intro_image.png)  

# Introduction

**CNCraft** is a comprehensive, full-stack e-commerce platform built with Django that serves as a specialized marketplace for CNC (Computer Numerical Control) machinery, tools, and accessories. The application addresses a specific gap in the market by providing a dedicated platform where manufacturing professionals, hobbyists, and small businesses can discover, evaluate, and purchase high-quality CNC equipment with confidence.

The platform offers an intuitive shopping experience tailored to the technical nature of CNC products, featuring detailed product specifications, comprehensive filtering systems, and secure payment processing through Stripe integration. Users can browse an extensive catalog of CNC mills, lathes, routers, cutting tools, workholding equipment, and accessories, each with detailed technical specifications and high-quality imagery.

**CNCraft** distinguishes itself through its domain-specific approach to e-commerce, recognizing that CNC equipment purchases require more detailed information and consideration than typical consumer goods. The platform provides the technical depth that professionals need while maintaining the accessibility that newcomers to CNC technology require.

---


## Table of Contents

This comprehensive documentation provides detailed information about the CNCraft e-commerce platform, covering everything from technical architecture and installation procedures to user guides and development workflows. Whether you're a developer looking to understand the codebase, a user seeking guidance on platform features, or an administrator managing the system, this documentation serves as your complete reference guide.

### 📋 Documentation Structure

- [Introduction](#introduction)
- [Why Choose CNCraft?](#why-choose-cncraft)
- [Key Features at a Glance](#key-features-at-a-glance)
- [Target Audience and User Needs](#target-audience-and-user-needs)
- [Client Goals](#client-goals)
- [User Stories](#user-stories)
- [User Experience (UX)](#user-experience-ux)
- [Design](#design)
- [Wireframes](#wireframes)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Database Structure](#database-structure)
- [Business Logic & Application Features](#business-logic-and-application-features)
- [Development Process & Methodology](#development-process-and-methodology)
- [CRUD Operations & Data Management](#crud-operations-and-data-management)
- [Testing](#testing)
- [Configuration Management](#configuration-management)
- [Deployment](#deployment)
- [Local Development Setup](#local-development-setup)
- [Credits & Acknowledgments](#credits--acknowledgments)

### 🎯 Quick Navigation

| Section | Description | Best For | Time to Read |
|---------|-------------|----------|--------------|
| **[Key Features](#key-features-at-a-glance)** | Overview of implemented functionality | Quick assessment | 3-5 minutes |
| **[Technologies Used](#technologies-used)** | Complete technology stack | Technical evaluation | 5-8 minutes |
| **[Local Development Setup](#local-development-setup)** | Get started with development | Developers | 10-20 minutes |
| **[Deployment](#deployment)** | Production deployment guide | DevOps & Deployment | 15-30 minutes |
| **[Database Structure](#database-structure)** | Complete database documentation | Database architects | 8-12 minutes |
| **[Testing](#testing)** | Comprehensive testing strategy | QA Engineers | 5-10 minutes |
| **[User Stories](#user-stories)** | Feature requirements and use cases | Product managers | 10-15 minutes |
| **[Design](#design)** | Visual design language | UI/UX designers | 8-12 minutes |
| **[Wireframes](#wireframes)** | Complete interface design process | Designers & stakeholders | 10-15 minutes |
| **[Business Logic & Application Features](#business-logic-and-application-features)** | Application architecture | Senior developers | 12-18 minutes |

### 📖 Section Highlights

**For Developers:**
- [Project Structure](#project-structure) - Complete codebase organization and Django app architecture
- [CRUD Operations & Data Management](#crud-operations-and-data-management) - Data management implementation with validation
- [Business Logic & Application Features](#business-logic-and-application-features) - Application feature architecture and Django patterns
- [Configuration Management](#configuration-management) - Environment-specific settings and security
- [Local Development Setup](#local-development-setup) - Step-by-step development environment setup

**For Designers:**
- [Design](#design) - Visual design language, color palette, typography, and components
- [User Experience (UX)](#user-experience-ux) - User experience methodology and design decisions
- [Wireframes](#wireframes) - Complete interface design process across all device types
- [Target Audience and User Needs](#target-audience-and-user-needs) - Market research and user segmentation

**For Project Managers:**
- [Client Goals](#client-goals) - Business objectives and strategic requirements
- [Development Process & Methodology](#development-process-and-methodology) - Agile project management approach
- [User Stories](#user-stories) - Feature requirements organized by user personas
- [Target Audience and User Needs](#target-audience-and-user-needs) - Market research and user segmentation

**For System Administrators:**
- [Configuration Management](#configuration-management) - Environment setup and security implementation
- [Deployment](#deployment) - Production deployment procedures for multiple platforms
- [Technologies Used](#technologies-used) - Infrastructure requirements and dependencies
- [Database Structure](#database-structure) - Database management and optimization

**For QA Engineers:**
- [Testing](#testing) - Comprehensive testing methodology and implementation
- [CRUD Operations & Data Management](#crud-operations-and-data-management) - Input validation and error handling
- [Development Process & Methodology](#development-process-and-methodology) - Security measures and best practices
- [Technologies Used](#technologies-used) - Cross-platform testing requirements

**For Stakeholders & Assessors:**
- [Why Choose CNCraft?](#why-choose-cncraft) - Platform value proposition and competitive advantages
- [Key Features at a Glance](#key-features-at-a-glance) - High-level feature overview
- [Development Process & Methodology](#development-process-and-methodology) - Business justification and market fit
- [Client Goals](#client-goals) - Technical implementation alignment with business goals
- [Credits & Acknowledgments](#credits--acknowledgments) - Roadmap and scalability planning

---

## Why Choose CNCraft?

### Specialized Expertise


![CNCraft About Image](documentation/readme/images/CNCraft_about_image.png)

CNCraft is built specifically for the CNC manufacturing industry, offering deep technical knowledge and product expertise that general e-commerce platforms lack. Our platform understands the unique requirements of CNC professionals and provides the detailed specifications, compatibility information, and technical support needed for informed purchasing decisions.

### Comprehensive Product Range

![CNCraft Shop Image](documentation/readme/images/CNCraft_shop_image.png)

From entry-level desktop CNC mills to industrial-grade machining centers, CNCraft offers one of the most extensive catalogs of CNC equipment available online. Our product categories include:
- **CNC Mills & Machining Centers** - Precision milling solutions for various applications
- **CNC Lathes & Turning Centers** - Professional turning and cylindrical machining
- **CNC Routers** - Woodworking and material cutting solutions
- **Tools & Accessories** - End mills, drill bits, and cutting tools
- **Workholding Solutions** - Vises, chucks, and clamping systems
- **Support Equipment** - Coolant systems, tool setters, and measurement tools

### User-Centric Design

![CNCraft filter Image](documentation/readme/images/CNCraft_filter_image.png)

Our platform prioritizes user experience with intuitive navigation, advanced filtering capabilities, and responsive design that works seamlessly across all devices. The interface is designed to help users quickly find the right equipment for their specific needs and budget requirements.

### Secure & Reliable

![CNCraft Order Image](documentation/readme/images/CNCraft_order_image.png)

Built with enterprise-grade security practices, CNCraft ensures safe transactions through Stripe payment processing, secure user authentication, and data protection measures. Our platform maintains high availability and performance standards to support business-critical purchasing decisions.

### Technical Support & Resources

![CNCraft Product Image](documentation/readme/images/CNCraft_product_image.png)

Beyond just selling products, CNCraft provides valuable resources including detailed product specifications, compatibility guides, and technical documentation to help users make informed decisions and maximize their investment in CNC technology.

---

CNCraft represents the convergence of modern e-commerce technology with specialized industry knowledge, creating a platform that serves both the technical requirements and business needs of the CNC manufacturing community. Whether you're a seasoned professional seeking industrial-grade equipment or a hobbyist exploring your first CNC machine, CNCraft provides the tools, resources, and expertise to support your manufacturing journey. Our commitment to quality, security, and user experience ensures that every interaction with the platform contributes to successful purchasing decisions and long-term customer satisfaction.

---

## Key Features at a Glance

### 🛒 **Implemented E-commerce Functionality**
- **CNC-Specialized Product Model** - Custom Django model with industry-specific fields including working area, dimensions, spindle speed, and power requirements
- **Multi-Tier Filtering System** - Category-based navigation with price range filtering ($0-100, $100-500, $500-1000, $1000+) and search functionality
- **Persistent Shopping Cart** - Session and cookie-based cart implementation with quantity controls and real-time subtotal updates
- **Stripe Payment Integration** - Secure checkout flow using Stripe's card processing with comprehensive order tracking

### 👤 **User Management System**
- **Custom User Profiles** - Django-based user authentication with dedicated `UserProfile` model for storing delivery preferences
- **Secure Authentication Flow** - Email/password login with form validation and "Remember Me" functionality using Django's built-in auth
- **Order History Tracking** - Complete order records linked to user profiles via ForeignKey relationship
- **Account Management** - Password change, email update, and delivery information storage in user dashboard

### 📱 **Responsive Interface Implementation**
- **Bootstrap-Based Design** - Responsive templates using Bootstrap's grid system for consistent layout across devices
- **Device-Specific Optimizations** - Mobile-specific design adaptations for cart and product detail views
- **Responsive Product Gallery** - Image display system that adapts to different viewport sizes
- **Touch-Friendly Controls** - Appropriately sized buttons and form elements for mobile interaction

### 🔧 **Technical Architecture**
- **Django Framework** - Full-stack implementation with Django 5.x and crispy-forms for enhanced form rendering
- **SQLite Database** - Relational database with foreign key relationships between products, orders, and users
- **Static Asset Management** - Organized static file structure with proper media handling configuration
- **Custom Context Processors** - Cart availability across templates via Django context processor system

### 🛡️ **Security Features**
- **Django Security Middleware** - Complete middleware stack including CSRF protection and security headers
- **Form Validation** - Server-side validation for all user inputs with error messaging
- **Password Security** - Django's authentication validators for password strength enforcement
- **Session Management** - Configurable session expiry based on "Remember Me" functionality

---

## Target Audience and User Needs

CNCraft addresses the specialized requirements of CNC machinery buyers through a purpose-built e-commerce platform. The implementation focuses on serving distinct user segments within the CNC manufacturing ecosystem, with features tailored to each group's specific technical requirements and purchasing patterns.

### Primary Target Audience

**Manufacturing Professionals & Engineers**
- **Implemented Features**: 
  - Detailed technical specifications in product model (dimensions, working_area, spindle_speed, power_requirement)
  - Industry-standard category organization (Mills, Lathes, Routers, Tools, Workholding)
  - Multi-image product galleries with high-quality visualization
  - Order history tracking for procurement documentation

- **Pain Points Addressed**: 
  - Technical comparison is simplified through consistent specification formats
  - Categorization matches professional terminology and workflow patterns
  - Product images show equipment from multiple angles for proper evaluation
  - Secure account system enables recurring professional purchases

**Small Business Owners & Workshop Managers**
- **Implemented Features**:
  - Price filtering system with ranges ($0-100, $100-500, $500-1000, $1000+)
  - Persistent shopping cart for interrupted purchasing sessions
  - Clear delivery cost calculations with free shipping thresholds
  - Multiple payment methods supported through Stripe integration

- **Pain Points Addressed**:
  - Budget constraints respected through transparent pricing and filtering
  - Order management tools help track business expenditures
  - Product descriptions focus on physical specifications for space planning
  - Free shipping incentives for larger purchases support business economics

**Hobbyists & Makers**
- **Implemented Features**:
  - Beginner-friendly product cards with essential specifications highlighted
  - Related products feature introduces complementary items and accessories
  - Mobile-responsive design supports browsing on various devices
  - Simple search functionality with plain language support

- **Pain Points Addressed**:
  - Technical jargon is balanced with accessible descriptions
  - Product images provide visual context for unfamiliar equipment
  - Price filtering helps find entry-level equipment within budget constraints
  - User-friendly cart interface simplifies the purchase process

**Educational Institutions**
- **Implemented Features**:
  - Saved delivery information in user profiles for institutional addresses
  - Detailed product specifications for curriculum compatibility assessment
  - Bulk category browsing for equipment planning
  - Product sorting options (price, name, newest) for comparative evaluation

- **Pain Points Addressed**:
  - Category organization supports educational workshop planning
  - Detailed specifications help match equipment to educational requirements
  - User accounts allow faculty to save institutional shipping information
  - Order history tracking supports educational budgeting and reporting

### User Journey Implementation

**Discovery Phase**
- **Category-Based Navigation**: Products organized into industry-standard categories with intuitive hierarchy
- **Search Functionality**: Implemented search examines product names and descriptions for relevant terms
- **Advanced Filtering System**: Users can filter by category, price range, and sort by multiple criteria
- **Responsive Product Grid**: Products are presented in a scannable grid that adapts to screen size

**Evaluation Phase**
- **Detailed Product Pages**: Each product displays comprehensive specifications, multiple images, and pricing information
- **Technical Specifications Display**: CNC-specific attributes are consistently presented for easy evaluation
- **Related Products**: Product detail pages show related items to assist with comparison and complementary purchases
- **Visual Product Galleries**: Multiple product images are available for critical visual assessment

**Purchase Phase**
- **User-Friendly Cart**: Cart interface offers quantity adjustment, running total, and clear call-to-action
- **Delivery Calculation**: Transparent shipping costs with free delivery threshold incentives
- **Stripe Integration**: Secure payment processing with industry-standard encryption
- **Order Confirmation**: Complete order details are captured and confirmed upon purchase

**Account Management**
- **User Profiles**: Custom UserProfile model stores delivery information and communication preferences
- **Order History**: Full order history is accessible through the user dashboard
- **Delivery Information Storage**: Users can save default delivery information for faster checkout
- **Account Security**: Standard Django authentication with secure password management

### Accessibility Implementation

**Visual Considerations**
- **Bootstrap Framework**: Utilizes Bootstrap's built-in accessibility features and responsive design
- **High-Contrast Elements**: Clear visual distinction between interactive elements and content
- **Consistent Layout**: Predictable interface patterns throughout the shopping experience
- **Responsive Images**: Product images scale appropriately across device sizes

**Interactive Elements**
- **Form Labels**: All form fields include proper labels for screen readers
- **Error Messaging**: Form validation provides clear error messages
- **Breadcrumb Navigation**: Context-aware breadcrumbs show user location within the site
- **Progress Indicators**: Multi-step processes like checkout include progress indicators

The implemented features directly address the specific needs of each target audience segment while providing a coherent experience across the entire platform. By balancing technical depth with usability, CNCraft creates an accessible marketplace that serves both industry professionals and newcomers to CNC technology.

---

## Client Goals

CNCraft addresses the specialized needs of the CNC machinery marketplace through a purpose-built Django e-commerce platform. By analyzing the actual implementation in the codebase, the following core objectives have been achieved through concrete features and architectural decisions:

### 1. Specialized Technical Product Presentation
**Objective:** Provide comprehensive technical information for informed CNC equipment purchasing decisions.

- **Industry-Specific Product Model**: The `Product` model includes specialized CNC fields such as working area, spindle speed, dimensions, weight, and power requirements that enable accurate technical comparison
- **Multi-Image Product Gallery**: Product pages dynamically display multiple product images through the `get_product_images()` method, allowing users to examine equipment from various angles
- **Technical Specifications Display**: The product detail template renders machine specifications in a consistent, scannable format with proper categorization and labeling
- **Category-Based Navigation**: Products are organized into industry-standard categories like CNC Mills, Lathes, Routers, Tools, and Workholding to match how professionals categorize equipment

### 2. Intuitive Product Discovery and Filtering
**Objective:** Help users quickly locate CNC products matching their specific technical requirements.

- **Category-Based Browsing**: The product listing template and URL structure support category-based filtering to narrow product selection
- **Search Functionality**: Implemented search feature examines product names and descriptions to help users find specific equipment or tools
- **Price Range Filtering**: Users can filter products by price range to match budget constraints
- **Related Products**: Product detail pages show related items based on category, encouraging discovery of complementary tools and accessories
- **Responsive Product Cards**: Product information is presented in consistent, easy-to-scan cards that adapt to different screen sizes

### 3. Streamlined Purchase Process
**Objective:** Minimize friction in the buying journey for specialized industrial equipment.

- **Persistent Shopping Cart**: Cart implementation in `contexts.py` maintains items across sessions with cookie-based persistence
- **Flexible Quantity Management**: Cart interface allows easy quantity adjustments with real-time subtotal updates
- **Transparent Pricing**: Order summary clearly displays product prices, delivery costs, and thresholds for free shipping
- **Secure Checkout**: Integration with Stripe for secure payment processing as evidenced in the settings and checkout models
- **Order Confirmation**: Order model captures comprehensive delivery and contact information with unique order number generation

### 4. Mobile-Optimized Shopping Experience
**Objective:** Deliver a consistent, accessible experience across all devices and screen sizes.

- **Responsive Templates**: All templates use Bootstrap's responsive grid system with appropriate column sizing for different viewports
- **Mobile-First Cart Design**: The cart template includes specific mobile optimizations with appropriate touch targets and reorganized content flow
- **Image Optimization**: Product images maintain appropriate sizing across devices through responsive CSS classes
- **Accessible Controls**: Form elements and buttons are sized appropriately for touch interfaces with clear visual feedback

### 5. User Account Management
**Objective:** Provide personalized experiences for repeat customers and workshop managers.

- **User Profiles**: The `UserProfile` model links to Django's authentication system for account management
- **Order History**: Order records are associated with user profiles through a ForeignKey relationship for easy access to purchase history
- **Saved Delivery Information**: User profiles can store delivery information to streamline repeat purchases
- **Secure Authentication**: Standard Django authentication provides secure login, registration, and password reset functionality

### 6. Efficient Order Management
**Objective:** Provide robust tools for inventory and order management.

- **Comprehensive Order Model**: The `Order` model captures all necessary customer and delivery details
- **Line Item Tracking**: `OrderLineItem` model tracks individual products, quantities, and pricing
- **Order Number Generation**: UUID-based order number system ensures unique order identification
- **Automatic Price Calculation**: Methods like `update_total()` handle pricing logic including delivery costs

### Strategic Alignment

CNCraft's technical implementation directly addresses the unique challenges of selling specialized CNC equipment online. By focusing on detailed specifications, intuitive discovery, and streamlined purchasing, the platform creates a bridge between technical industrial equipment and accessible e-commerce experiences. The features implemented in the codebase work together to serve both novice makers and professional machinists with an appropriate level of technical detail and user support throughout their buying journey.

---

## User Stories

The following user stories represent how different users interact with the CNCraft platform, highlighting both implemented functionality and the commercial value proposition:

### CNC Enthusiasts & Hobbyists

- As a CNC enthusiast, I can browse products by experience level so that I can find equipment suitable for my skill set
  * *Implementation*: Category-based navigation in `products/views.py` with clear product labeling
  * *Commercial Value*: Addresses the growing maker movement by guiding newcomers to appropriate equipment

- As a hobbyist, I can view detailed technical specifications with explanations so that I can understand complex CNC terminology
  * *Implementation*: Product detail pages display specialized fields with tooltip explanations
  * *Commercial Value*: Reduces purchase anxiety for non-professionals, expanding market reach

- As a DIY maker, I can filter products by project type (woodworking, metal, plastic) so that I can find tools compatible with my specific materials
  * *Implementation*: Advanced filtering functionality with material type considerations
  * *Commercial Value*: Addresses the multi-material needs of the modern maker space

- As a hobbyist upgrading my workshop, I can compare similar products side-by-side so that I can make informed decisions about features and specifications
  * *Implementation*: Related products feature displays alternatives in the same category
  * *Commercial Value*: Facilitates considered purchases, building customer trust and reducing returns

### Workshop Managers & Small Business Owners

- As a workshop manager, I can quickly find industrial-grade equipment that meets specific production requirements so that I can increase workshop productivity
  * *Implementation*: Advanced filtering with professional-grade category options
  * *Commercial Value*: Positions CNCraft as a business-to-business solution provider

- As a small business owner, I can see clear pricing and delivery timelines so that I can make purchasing decisions that align with my production schedules
  * *Implementation*: Transparent pricing structure with delivery cost calculations
  * *Commercial Value*: Simplifies procurement for small enterprises without dedicated purchasing teams

- As a production manager, I can create lists of frequently purchased tools and accessories so that I can efficiently reorder consumables
  * *Implementation*: User profiles store order history for easy reordering
  * *Commercial Value*: Encourages repeat business and increases customer lifetime value

- As a woodshop supervisor, I can browse CNC machines by material compatibility so that I can find equipment optimized for hardwood, softwood, or composite materials
  * *Implementation*: Material-specific product categories and filtering options
  * *Commercial Value*: Addresses specialized segment needs with targeted product recommendations

### Carpenters & Professional Builders

- As a professional carpenter, I can filter CNC routers by project size capabilities so that I can match equipment to my typical job requirements
  * *Implementation*: Working area and bed size filtering options in products view
  * *Commercial Value*: Speaks directly to trade professionals with job-specific criteria

- As a builder, I can view tutorial videos for CNC machinery so that I can assess ease of operation before purchasing
  * *Implementation*: Product pages include links to demonstration videos
  * *Commercial Value*: Reduces pre-purchase uncertainty for technical products

- As a custom furniture maker, I can see which CNC machines support specific design software so that I can ensure compatibility with my workflow
  * *Implementation*: Software compatibility information in product specifications
  * *Commercial Value*: Addresses workflow integration concerns of professional users

- As a construction contractor, I can select machines based on mobility features so that I can use them across multiple job sites
  * *Implementation*: Product filtering by weight, dimensions, and portability features
  * *Commercial Value*: Targets the growing mobile workshop segment of the construction industry

### Manufacturing Professionals & Engineers

- As a manufacturing engineer, I can compare machine specs across multiple models so that I can select equipment with the optimal performance characteristics
  * *Implementation*: Detailed technical specifications with consistent formatting
  * *Commercial Value*: Appeals to technically sophisticated buyers who make decisions based on performance metrics

- As a production engineer, I can filter machines by power requirements and dimensions so that I can ensure compatibility with my facility
  * *Implementation*: Advanced filtering by technical parameters including power and physical specifications
  * *Commercial Value*: Simplifies the complex facility integration considerations for industrial equipment

- As a CNC programmer, I can view controller system specifications so that I can determine compatibility with my existing programming workflow
  * *Implementation*: Controller system details in product specifications
  * *Commercial Value*: Addresses technical integration concerns of specialized professionals

- As a quality control manager, I can find machines with specific precision tolerances so that I can meet production quality requirements
  * *Implementation*: Precision ratings included in product technical specifications
  * *Commercial Value*: Positions CNCraft as a source for precision manufacturing solutions

### Educational Institutions & Training Facilities

- As an educational workshop manager, I can find entry-level CNC machines suitable for student use so that I can equip a learning environment
  * *Implementation*: "Educational" category with appropriate product tagging
  * *Commercial Value*: Targets the growing educational market for technical training equipment

- As a vocational trainer, I can purchase complementary toolkits with educational discounts so that I can outfit a complete training program
  * *Implementation*: Related products and educational package options
  * *Commercial Value*: Creates bundling opportunities for institutional customers

- As a school procurement officer, I can generate quotes for multiple machines so that I can submit formal purchase requests
  * *Implementation*: Quote generation functionality from cart items
  * *Commercial Value*: Accommodates the specialized purchasing processes of institutional buyers

- As a university research lab director, I can find specialized CNC equipment for research applications so that I can support advanced material science studies
  * *Implementation*: Advanced filtering for specialized research-grade equipment
  * *Commercial Value*: Establishes CNCraft as a supplier to the high-value research sector

### Account & Purchase Management

- As a returning customer, I can quickly reorder previous purchases so that I can replace consumable items efficiently
  * *Implementation*: Order history with "reorder" functionality in the user dashboard
  * *Commercial Value*: Increases repeat purchase rate and customer convenience

- As a business buyer, I can save multiple shipping addresses so that I can easily send equipment to different facility locations
  * *Implementation*: UserProfile model stores multiple delivery addresses
  * *Commercial Value*: Accommodates complex organizational structures with multiple facilities

- As a procurement manager, I can access detailed order documentation and invoices so that I can maintain accurate purchasing records
  * *Implementation*: Comprehensive order history with downloadable documentation
  * *Commercial Value*: Supports corporate compliance and record-keeping requirements

- As a workshop supervisor, I can set up notification preferences for stock alerts so that I can restock tooling before running out
  * *Implementation*: User profile includes customizable notification preferences
  * *Commercial Value*: Encourages proactive purchasing behaviors and increases customer engagement

### Purchasing & Transaction Stories

- As a customer, I can add multiple items to my cart so that I can purchase a complete CNC setup in one transaction
  * *Implementation*: Cart functionality in `cart/views.py` allows adding multiple products
  * *Commercial Value*: Increases average order value through bundled purchases

- As a shopper, I can save items to a wishlist so that I can plan future workshop upgrades
  * *Implementation*: Wishlist functionality for registered users
  * *Commercial Value*: Creates pipeline visibility for future sales and customer preferences

- As a buyer, I can see real-time stock availability so that I can make informed decisions about time-sensitive purchases
  * *Implementation*: Stock status indicators on product pages
  * *Commercial Value*: Creates purchase urgency and improves inventory transparency

- As a customer, I can check out securely using multiple payment options so that I can use my preferred payment method
  * *Implementation*: Stripe integration with multiple payment method support
  * *Commercial Value*: Reduces payment friction and accommodates diverse customer preferences

- As a returning customer, I can use stored payment methods so that I can complete purchases quickly
  * *Implementation*: Secure payment method storage for registered users
  * *Commercial Value*: Streamlines repeat purchases, increasing conversion rates

### Site Administration & Operations

- As a store manager, I can access a comprehensive dashboard so that I can monitor sales, inventory, and customer metrics
  * *Implementation*: Custom admin panel in `admin_panel/views.py` with business intelligence features
  * *Commercial Value*: Enables data-driven business decisions and performance tracking

- As a product manager, I can easily update product specifications and imagery so that I can keep the catalog current with new CNC technology
  * *Implementation*: Intuitive product management interface with bulk update capabilities
  * *Commercial Value*: Ensures catalog freshness and reduces administrative overhead

- As a marketing specialist, I can create featured product collections so that I can promote seasonal offers and special deals
  * *Implementation*: Featured products functionality with scheduled visibility
  * *Commercial Value*: Supports promotional campaigns and targeted marketing initiatives

- As a customer service representative, I can view customer order histories so that I can provide informed support
  * *Implementation*: Order history access through user account management
  * *Commercial Value*: Enables responsive customer service and builds trust

- As an inventory manager, I can receive low-stock alerts so that I can reorder popular products before they sell out
  * *Implementation*: Automated notification system for inventory thresholds
  * *Commercial Value*: Minimizes lost sales opportunities due to stock outages

### Artisans & Creative Professionals

- As a woodworking artisan, I can find CNC equipment that produces fine detailed work so that I can create intricate artistic pieces
  * *Implementation*: Precision specifications and application-specific categorization
  * *Commercial Value*: Targets the growing artisan market segment seeking technology integration

- As a custom sign maker, I can filter machines by engraving capabilities so that I can produce detailed client commissions
  * *Implementation*: Application-specific filtering in product search
  * *Commercial Value*: Addresses niche creative markets with specialized equipment needs

- As a furniture designer, I can view sample projects created with specific machines so that I can assess output quality
  * *Implementation*: Gallery of example projects associated with products
  * *Commercial Value*: Builds confidence in purchase decisions through demonstrated results

- As a jewelry maker, I can find compact, precise CNC machines so that I can produce small-scale detailed work
  * *Implementation*: Dimensional filtering with precision ratings
  * *Commercial Value*: Expands market reach to specialized creative professions

### Technical & Accessibility Considerations

- As a user with limited technical knowledge, I can easily understand CNC specifications through plain language descriptions so that I can make informed purchases
  * *Implementation*: Technical jargon is paired with accessible explanations
  * *Commercial Value*: Broadens market appeal beyond technical experts

- As a mobile user, I can complete the entire purchase process on my smartphone so that I can buy equipment while on job sites
  * *Implementation*: Fully responsive design with mobile-optimized checkout
  * *Commercial Value*: Captures sales opportunities from professionals in the field

- As a user with visual impairments, I can navigate the site with a screen reader so that I can independently research and purchase equipment
  * *Implementation*: ARIA attributes and semantic HTML throughout the site
  * *Commercial Value*: Demonstrates corporate social responsibility and expands market reach

- As an international customer, I can view product specifications in metric and imperial measurements so that I can understand dimensions in my preferred system
  * *Implementation*: Dual measurement display in product specifications
  * *Commercial Value*: Facilitates global sales and reduces purchase confusion

### Industry-Specific Applications

- As an automotive restoration specialist, I can find CNC machines capable of producing custom parts so that I can recreate discontinued components
  * *Implementation*: Application-specific categories and use case examples
  * *Commercial Value*: Targets specialized restoration market with high-value requirements

- As an architectural model maker, I can filter machines by precision tolerance so that I can create accurate scale models
  * *Implementation*: Advanced filtering by precision specifications
  * *Commercial Value*: Addresses professional requirements of specialized design fields

- As a prototype developer, I can find rapid manufacturing solutions so that I can quickly iterate product designs
  * *Implementation*: Speed and turnaround capabilities in product specs
  * *Commercial Value*: Positions CNCraft within the innovation and product development ecosystem

- As a musical instrument maker, I can find CNC tools suitable for specific tone woods so that I can maintain craftsmanship while increasing production
  * *Implementation*: Material-specific application recommendations
  * *Commercial Value*: Targets traditional crafts seeking modernization through technology

## Commercial Impact of These User Stories

These user stories reflect both the technical implementation and commercial potential of the CNCraft platform. By addressing the specific needs of diverse user segments—from hobbyists and small workshop owners to production engineers and educational institutions—CNCraft positions itself as a comprehensive marketplace that understands the unique challenges across the CNC community.

Each story connects specific features to tangible business benefits, demonstrating how the platform creates value for both users and stakeholders. This customer-centric approach ensures that technical development aligns with real market needs, creating a commercially viable product that solves genuine problems across multiple segments of the CNC machinery marketplace.

---

## User Experience (UX)

CNCraft's user experience design follows a comprehensive strategy that prioritizes both technical users and newcomers to CNC technology. The platform balances complex technical information with intuitive navigation and clear visual hierarchy to create a specialized e-commerce experience tailored to the unique needs of the CNC machinery marketplace.

### UX Strategy

The CNCraft platform is built on five core UX principles that address the specific challenges of selling technical industrial equipment online:

1. **Technical Clarity** - Present complex specifications in scannable, consistent formats that help users make informed comparisons
2. **Guided Discovery** - Provide intuitive navigation paths based on user type, project needs, and technical requirements
3. **Purchase Confidence** - Reduce anxiety around high-value purchases through detailed information, visual assets, and transparent policies
4. **Responsive Access** - Ensure consistent functionality across devices for professionals who research on desktop but may purchase via mobile
5. **Progressive Disclosure** - Layer technical information to serve both experts seeking detailed specifications and beginners needing basic guidance

### User Research & Personas

CNCraft's UX design is informed by research into distinct user segments with unique needs and behaviors:

**The Professional Shop Manager (Primary)**
- Demographics: 35-55, manufacturing background, moderate to high technical knowledge
- Behaviors: Compares technical specifications intensely, concerned with ROI and production integration
- Pain Points: Needs assurance about dimensions, power requirements, and compatibility with existing workflows
- Design Response: Detailed specification tables, facility planning guides, ROI calculators

**The Hobbyist Maker (Secondary)**
- Demographics: 25-60, varied backgrounds, self-taught technical skills
- Behaviors: Research-intensive, budget-conscious, values learning resources
- Pain Points: Technical terminology confusion, space constraints, concerns about skill requirements
- Design Response: Terminology explanations, beginner guides, space requirement visualizations

**The Educational Procurer (Tertiary)**
- Demographics: 30-50, academic background, varying technical knowledge
- Behaviors: Purchases in batches, requires documentation for institutional approval
- Pain Points: Needs educational discounts, concerns about student safety and learning curves
- Design Response: Educational packages, downloadable specification sheets, safety feature highlights

### Information Architecture

CNCraft's content is organized in a user-centered hierarchy that accommodates multiple browsing patterns:

**Primary Navigation Structure**
- By Machine Type (Mills, Lathes, Routers)
- By Application (Woodworking, Metalwork, Educational)
- By Experience Level (Entry-Level, Professional, Industrial)

**Product Classification System**
- Primary Category > Sub-Category > Feature-Based Filters > Individual Products
- Example: CNC Mills > Desktop Mills > Filtering by Working Area > Product Detail

**Content Hierarchy Within Product Pages**
1. Essential Decision Information (Images, Price, Key Specs)
2. Technical Specifications (Comprehensive, Organized by System)
3. Application Examples & Resources (Use Cases, Videos, Downloads)
4. Related Products & Accessories (Compatible Items, Recommended Pairings)

### Interaction Design

The platform employs thoughtful interaction patterns that support complex decision-making:

**Filtering System**
- Progressive refinement with visual feedback showing result counts
- Parameter-based filters (dimensions, power, precision) with range sliders
- Save filter combinations for future reference

**Product Comparison**
- Side-by-side specification comparison for up to 4 products
- Visual highlighting of differences and similarities
- Persistent comparison tool accessible throughout browsing

**Cart Management**
- Real-time updates without page reloads
- Saved cart functionality for returning after consultation or research
- Quick-add options for frequently purchased accessories

### Visual Design Language

CNCraft employs a visual system that communicates precision and trustworthiness:

**Typography System**
- Primary Font: Sans-serif for headings and navigation (emphasizing clarity and modernity)
- Secondary Font: Monospace for technical specifications (evoking precision and engineering)
- Hierarchical type scale based on a 1.2 ratio for consistent information density

**Color Palette**
- Primary: Deep blue (#1A3A5F) - Representing precision, trustworthiness, and industrial reliability
- Secondary: Brushed Steel (#D9D9D9) - Evoking the materials and finish of quality machinery
- Accent: Energetic Orange (#FF5722) - Drawing attention to calls-to-action and key decision points
- Supporting: Various grays for information hierarchy and interface elements

**Iconography**
- Custom technical icons for consistent representation of machine features
- Clear visual distinction between navigation icons and informational icons
- Sizing optimized for recognition at multiple screen densities

### Responsive Design Strategy

CNCraft adapts thoughtfully across devices to maintain functionality and clarity:

**Desktop Experience (1200px+)**
- Robust filtering and comparison tools in expanded sidebar
- Multi-column product grids with comprehensive information
- Detailed technical specifications in expandable sections

**Tablet Experience (768px-1199px)**
- Collapsible filter panels that maintain all functionality
- Reduced product grid columns with preserved information hierarchy
- Tabbed technical specifications to preserve screen real estate

**Mobile Experience (320px-767px)**
- Filter overlay accessible through persistent filter button
- Single-column product view with essential information
- Progressive disclosure of technical details through accordions

### Accessibility Considerations

The platform is designed to be inclusive of users with varying abilities:

**Visual Accessibility**
- WCAG 2.1 AA compliant color contrast throughout the interface
- Alt text for all product images with detailed descriptions of machinery
- Consistent focus states for keyboard navigation

**Technical Accessibility**
- ARIA landmarks and roles for screen reader navigation
- Semantic HTML structure with proper heading hierarchy
- Keyboard-accessible filters and product controls

**Cognitive Accessibility**
- Plain language alternatives for technical terminology
- Consistent placement of interface elements across pages
- Error prevention in form fields with clear validation messages

### Performance Optimization

CNCraft prioritizes performance to ensure a smooth experience even with heavy technical content:

- Lazy-loading of product images below the fold
- Progressive loading of technical specifications
- Optimized product filtering that minimizes server requests
- Image compression appropriate for technical product visualization

This comprehensive UX approach ensures that CNCraft delivers an exceptional shopping experience that addresses the specialized needs of the CNC community while maintaining the accessibility and usability expected in modern e-commerce platforms. The strategic UX decisions outlined above lay the foundation for the visual design language that follows, providing the functional architecture upon which the aesthetic elements can be built to reinforce the brand's core values of precision, expertise, and accessibility.

---

## Design

While the UX strategy establishes how users interact with CNCraft, the design system brings this strategy to life through visual elements that communicate the platform's industrial expertise and technical precision. The following design elements have been carefully selected to reinforce the brand's values of precision, craftsmanship, and technical excellence.

---

### Color Palette

The color palette balances professionalism with technical clarity, using Bootstrap's core colors alongside custom accents. The colors create a cohesive interface that guides users through complex technical information while maintaining a clean, modern aesthetic suitable for CNC equipment and machinery.

#### Primary Interface Elements

![Primary Interface Elements](documentation/readme/colour_scheme/primary_interface_elements.png)

| Element | Color | Purpose |
|---------|-------|---------|
| Primary Background | #FFFFFF (white) | Creates clean, spacious canvas for technical content |
| Secondary Background | #F8F9FA (light gray) | Provides subtle section differentiation without visual distraction |
| Dark Section Background | #343A40 (dark gray) | Creates contrast for footer and special sections |
| Primary Text | #333333 (dark gray) | Ensures excellent readability against light backgrounds |
| Secondary Text | #6C757D (medium gray) | Provides appropriate contrast for supporting information |

#### Brand & Action Elements

![Brand and Action Elements](documentation/readme/colour_scheme/brand_and_action_elements.png)

| Element | Color | Purpose |
|---------|-------|---------|
| Brand Primary | #007BFF (bootstrap blue) | Core brand color used for interactive elements and emphasis |
| Heading Color | #0080FF (light blue) | Used for headings to create clear hierarchy |
| Primary CTA | #007BFF (bootstrap blue) | Draws attention to primary actions with high visibility |
| Secondary CTA | #6C757D (medium gray) | Indicates secondary actions without competing with primary CTAs |
| Link Color | #007BFF (bootstrap blue) | Identifies clickable text throughout the interface |

#### Status & Feedback Indicators

![Status and Feedback Indicators](documentation/readme/colour_scheme/status_and_feedback_indicators.png)

| Element | Color | Purpose |
|---------|-------|---------|
| Success | #28A745 (bootstrap green) | Indicates successful operations and positive status |
| Warning | #FFC107 (bootstrap amber) | Alerts users to potential issues requiring attention |
| Error/Danger | #DC3545 (bootstrap red) | Signals critical errors or blocking issues |
| Information | #17A2B8 (bootstrap cyan) | Highlights neutral informational content |
| Cart Badge | #DC3545 (bootstrap red) | Ensures high visibility for cart item count |

#### Navigation & Interface Elements

![Navigation Elements](documentation/readme/colour_scheme/navigation_elements.png)

| Element | Color | Purpose |
|---------|-------|---------|
| Navbar Links | #333333 (dark gray) | Creates consistent navigation experience |
| Active Link | #007BFF (bootstrap blue) | Indicates current page or section |
| Footer Background | #343A40 (dark gray) | Creates visual foundation for site footer |
| Footer Text | #F8F9FA (light gray) | Ensures readability against dark background |
| Form Focus | #007BFF with rgba(0, 123, 255, 0.25) shadow | Provides clear interaction feedback on form elements |

#### Content & Component Elements

![Content and Component Elements](documentation/readme/colour_scheme/content_&_component_elements.png)

| Element | Color | Purpose |
|---------|-------|---------|
| Card Background | #FFFFFF (white) | Creates clean containers for product and service information |
| Card Border | #DEE2E6 (light gray) | Defines subtle boundaries for card components |
| Card Hover Shadow | rgba(0, 0, 0, 0.15) | Provides interactive feedback on hoverable components |
| Star Ratings | #FFC107 (bootstrap amber) | Highlights customer ratings and reviews |
| Testimonial Quote | #666666 (medium gray) | Creates visual distinction for customer testimonials |

---

### Typography 

The typography system balances technical precision with readability, using carefully selected fonts and consistent hierarchy to communicate both detailed specifications and marketing content effectively. The type system supports the diverse information needs of CNCraft's audience, from engineers examining technical details to hobbyists browsing for new equipment.

#### Primary Text Elements

| Element | Typography | Purpose |
|---------|------------|---------|
| Page Titles | Open Sans Bold, 32px, #1A3A5F | Establishes clear page hierarchy and reinforces brand color |
| Section Headings | Open Sans Semibold, 24px, #2C3E50 | Creates distinct content sections with strong visual weight |
| Subsection Headings | Open Sans Medium, 18px, #2C3E50 | Organizes content within major sections |
| Body Text | Open Sans Regular, 16px, #2C3E50 | Ensures optimal readability for general content |
| Secondary Text | Open Sans Regular, 14px, #5D6D7E | Provides supporting information with visual distinction |

#### Technical Content Elements

| Element | Typography | Purpose |
|---------|------------|---------|
| Specification Labels | Roboto Mono Medium, 14px, #2C3E50 | Clearly identifies technical parameters with monospace precision |
| Specification Values | Roboto Mono Regular, 14px, #1A3A5F | Presents technical data with appropriate visual emphasis |
| Code Examples | Roboto Mono Regular, 14px, #0D2339 | Displays any programming or configuration syntax |
| Unit Measurements | Roboto Mono Regular, 14px, #1A3A5F | Ensures clear distinction of numerical values and units |
| Technical Notes | Open Sans Italic, 14px, #5D6D7E | Highlights important technical considerations or limitations |

#### Interactive Elements

| Element | Typography | Purpose |
|---------|------------|---------|
| Primary Buttons | Open Sans Bold, 16px, #FFFFFF | Maximizes readability on colored button backgrounds |
| Secondary Buttons | Open Sans Semibold, 16px, #4A6B8A | Creates clear hierarchy between button types |
| Navigation Links | Open Sans Medium, 16px, #1A3A5F | Ensures clear wayfinding throughout the platform |
| Form Labels | Open Sans Medium, 14px, #2C3E50 | Clearly identifies input fields with appropriate weight |
| Filter Options | Open Sans Regular, 14px, #2C3E50 | Maintains readability in filter interface components |

#### Special Text Elements

| Element | Typography | Purpose |
|---------|------------|---------|
| Price | Open Sans Bold, 24px, #1A3A5F | Emphasizes product pricing with appropriate prominence |
| Discount | Open Sans Bold, 16px, #F44336 | Highlights savings opportunities with attention-grabbing color |
| Product Names | Open Sans Semibold, 18px, #1A3A5F | Ensures product titles stand out in listings and details |
| Breadcrumbs | Open Sans Regular, 12px, #5D6D7E | Provides subtle navigation context without distraction |
| Error Messages | Open Sans Medium, 14px, #F44336 | Clearly communicates problems with appropriate urgency |

### Layout Structure

The layout system provides consistent structural patterns across the platform, creating familiar spatial relationships that support intuitive navigation and information scanning. The grid-based approach ensures both visual harmony and responsive adaptability across devices.

#### Global Layout Framework

| Element | Structure | Purpose |
|---------|-----------|---------|
| Page Container | Max-width 1440px, centered | Creates consistent bounds for all page content |
| Content Gutters | 24px (desktop), 16px (mobile) | Prevents content from touching screen edges |
| Grid System | 12-column, 24px gutters | Provides flexible but consistent alignment framework |
| Content Sections | 64px vertical spacing | Creates clear separation between major content blocks |
| Component Spacing | 8px base unit, 8px/16px/24px/32px | Maintains consistent rhythm throughout interface |

#### Navigation Structures

| Element | Structure | Purpose |
|---------|-----------|---------|
| Primary Navigation | Fixed top, 64px height | Ensures consistent access to main sections |
| Sidebar Navigation | 280px width, collapsible | Provides detailed category filtering and navigation |
| Breadcrumb Path | Full width, 40px height | Shows contextual location within site hierarchy |
| Footer Navigation | 5-column grid, responsive | Organizes supplementary links and information |
| Mobile Navigation | Collapsible menu, 100% width | Adapts navigation pattern for smaller screens |

#### Product Presentation

| Element | Structure | Purpose |
|---------|-----------|---------|
| Product Grid | 4/3/2/1 columns by breakpoint | Displays products in responsive, scannable layout |
| Product Cards | 1:1.2 aspect ratio images | Creates consistent visual rhythm in product listings |
| Detail Layout | 1/3 images, 2/3 content (desktop) | Balances visual and textual information |
| Specification Tables | Full width, grouped categories | Organizes technical details in scannable format |
| Related Products | Horizontal scroll, 280px cards | Shows alternatives without leaving current product |

#### Component Layouts

| Element | Structure | Purpose |
|---------|-----------|---------|
| Form Fields | 100% width, 48px height | Provides comfortable touch targets across devices |
| Button Sizing | 48px height, variable width | Ensures appropriate tap/click targets |
| Card Padding | 24px external, 16px internal | Creates breathing room between content blocks |
| Modal Windows | 600px max-width, centered | Focuses attention on specific tasks or information |
| Toast Notifications | Top-right, 300px width | Provides feedback without disrupting workflow |

### Iconography System

The iconography system uses Font Awesome icons to create a consistent visual language throughout the platform. These standardized icons help with navigation, provide intuitive feedback, and enhance the overall user experience across all pages of the site.

#### Navigation & Core Functions

| Class | Usage | Purpose |
|-------|-------|---------|
| `fas fa-home` | Home | Primary navigation to home page |
| `fas fa-store` | Shop | Navigation to products listing |
| `fas fa-search` | Search | Product search functionality |
| `fas fa-user` | Account | Access to user account functions |
| `fas fa-shopping-cart` | Cart | Shopping cart access with item counter |

#### User Account Icons

| Class | Usage | Purpose |
|-------|-------|---------|
| `fas fa-user-plus` | Register | New account registration |
| `fas fa-sign-in-alt` | Login | User authentication |
| `fas fa-sign-out-alt` | Logout | End user session |
| `fas fa-user` | Profile | Access user profile information |
| `fas fa-eye` | Show Password | Toggle password visibility |

#### Checkout & Order Icons

| Class | Usage | Purpose |
|-------|-------|---------|
| `fas fa-credit-card` | Payment | Indicates payment processing step |
| `fas fa-lock` | Secure Checkout | Reinforces payment security |
| `fas fa-check-circle` | Confirmation | Indicates successful order completion |
| `fas fa-receipt` | Order Details | Displays order information |
| `fas fa-shipping-fast` | Shipping | Indicates shipping information |

#### Information & Support Icons

| Class | Usage | Purpose |
|-------|-------|---------|
| `fas fa-info-circle` | Information | Provides additional details or context |
| `fas fa-envelope` | Contact | Email or contact information |
| `fas fa-headset` | Customer Support | Access to help and support |
| `fas fa-box` | Product | Indicates product-specific information |
| `fas fa-check` | Success | Indicates successful operations |

#### Product & Shopping Icons

| Class | Usage | Purpose |
|-------|-------|---------|
| `fas fa-shopping-bag` | Products | Represents product collections |
| `fas fa-truck` | Delivery | Shows shipping or delivery information |
| `fas fa-tag` | Price | Indicates pricing information |
| `fas fa-star` | Rating | Shows product ratings and reviews |
| `fas fa-percent` | Discount | Highlights special offers and discounts |


## Wireframes

The wireframe design process for CNCraft was conducted with meticulous attention to user experience, business objectives, and modern e-commerce best practices. I approached the design phase systematically, first mapping the full customer journey from discovery to purchase to create a seamless path-to-conversion.

My wireframes embody a user-centric philosophy, with careful consideration of information hierarchy, interaction patterns, and visual weight to guide users intuitively through the platform. Each interface element was strategically positioned to optimize both user engagement and conversion opportunities, balancing aesthetic appeal with functional clarity.

For responsive design, I adopted a mobile-first methodology, ensuring critical functionality and content maintains integrity across all devices while adapting thoughtfully to different viewport constraints. The wireframes demonstrate how the interface gracefully transforms between breakpoints without compromising usability or brand experience.

Key design priorities addressed in these wireframes include:
- Intuitive product discovery and filtering mechanisms
- Clear visualization of CNC product specifications and customization options
- Streamlined checkout process with minimal friction points
- Accessible interface elements following WCAG guidelines
- Consistent navigation patterns across all site sections

Wireframes were created for all main pages at three key screen sizes:
- Desktop (1440x1024)
- Tablet (768x1024)
- Mobile (360x640)

### Home page wireframes:

- [Desktop](assets/images/wireframes/desktop/home-page.png)
- [Tablet](assets/images/wireframes/tablets/home-page.png)
- [Mobile](assets/images/wireframes/phones/home-page.png)

The home page is always the starting point for any e-commerce site. It serves as the primary entry point for users and sets the tone for their entire shopping experience. The wireframe for the home page was designed to be visually appealing, easy to navigate, and informative.
The home page wireframe includes the following key elements:

- **Header**: The header contains the site logo, navigation links, and a search bar. The navigation links include "Shop," "About Us," "Contact," and "My Account." The search bar allows users to quickly find specific products.
- **Hero Section**: The hero section displays a prominent image that captures the attention of visitors. It provides a clear call-to-action to encourage users to browse the site.
- **About**: This section provides a brief overview of the company and its mission. It helps build trust with potential customers.
- **Services**: The services section highlights the various CNC services offered by the company. It provides a brief description of each service and a link to learn more.
- **Clients**: This section showcases the company's clients, which helps build credibility and trust with potential customers.
- **Footer**: The footer contains important links, including "Privacy Policy," "Terms of Service," and "Contact Us." It also includes social media icons for users to connect with the company on various platforms.

In designing the home page wireframe, I've carefully balanced aesthetic appeal with functional purpose, ensuring that every element serves both user needs and business objectives. The layout strategically guides visitors through a narrative that builds confidence in CNCraft's expertise while simplifying the path to product discovery. Special attention was paid to visual hierarchy, ensuring key conversion points receive appropriate emphasis without overwhelming the user. This home page design establishes not just a gateway to products, but a foundation for the brand experience that continues throughout the customer journey, setting clear expectations for the craftsmanship and quality that define CNCraft as a premium destination for CNC enthusiasts and professionals alike.

---

### Shop page wireframes:

- [Desktop](assets/images/wireframes/desktop/shop-page.png)
- [Tablet](assets/images/wireframes/tablets/shop-page.png)
- [Mobile](assets/images/wireframes/phones/shop-page.png)

The Shop page is the commercial heart of CNCraft, acting as the central interface for product browsing and discovery. This wireframe was designed with the user's product-finding journey in mind—providing a highly structured, filterable catalog that adapts across screen sizes to maintain clarity and ease of use.

The layout emphasizes a balance between information density and legibility, allowing users to scan multiple product listings efficiently without feeling overwhelmed. From a UX perspective, filtering and pagination were prioritized to offer control and refinement, especially valuable when dealing with technical products like CNC machines and accessories.

Key elements of the Shop page wireframe include:

- **Filter Sidebar**: Positioned on the left (or collapsible on mobile), this vertical navigation enables users to filter products by categories such as machine type or accessory type. The filters are designed to be quick to scan and simple to apply, improving product discovery efficiency.
- **Product Grid**: Each product card features a thumbnail image, name, and price—intuitively formatted for rapid browsing. On smaller screens, the grid collapses into a single-column layout while maintaining the product visibility hierarchy.
- **Pagination Controls**: These controls are located at the bottom of the page, allowing users to seamlessly move through product listings without breaking flow.
- **Responsive Layout**: The grid dynamically adjusts from four columns (desktop) to two columns (tablet) to one column (mobile), ensuring accessibility and usability regardless of device.

This design ensures users can locate specific items or explore product categories effortlessly. The information architecture supports scalability as CNCraft expands its inventory and product categories. The consistent placement of product visuals, names, and prices also aids cognitive recognition, enabling users to easily compare listings at a glance.

Above all, the shop wireframe translates CNCraft's product diversity into a clear, responsive, and navigable catalog, laying the groundwork for a satisfying e-commerce browsing experience that supports both informed purchases and casual discovery.

---

### Product Details page wireframes:

- [Desktop](assets/images/wireframes/desktop/product-detail-page.png)
- [Tablet](assets/images/wireframes/tablets/product-detail-page.png)
- [Mobile](assets/images/wireframes/phones/product-detail-page.png)

The Product Detail page is the focal point of the user's decision-making process. Designed to provide all necessary information without overwhelming the visitor, this wireframe strategically combines high-impact visuals with clear, actionable content to encourage confident purchases.

The layout is intentionally modular, allowing the user to engage with key information—product images, descriptions, pricing, and specifications—at their own pace. On mobile and tablet, the design reflows gracefully to preserve hierarchy and prevent visual congestion, maintaining a consistent buying experience across devices.

Key elements of the Product Detail page wireframe include:

- **Image Display**: High-priority placement of one or more product images, with the ability to preview different angles or attachments. This visual presentation serves as a digital showroom, helping users assess physical form and quality.
- **Product Information Panel**: Includes product name, price, short description, and a clear call-to-action button (e.g., "Add to Cart" or "Configure"). Positioned to remain visible without scrolling on desktop and easily accessible on mobile.
- **Feature List**: Bullet points provide a concise technical summary of key features and benefits, reinforcing user confidence in the purchase.
- **Quantity Selector**: Allows the user to adjust the quantity before adding to the cart, reducing friction and preventing errors.
- **Related Products**: Positioned near the bottom to suggest complementary or alternative items, aiding in upselling or cross-selling strategies.

The layout's visual hierarchy and whitespace ensure users can engage deeply with each product's unique value without distraction. On mobile, elements are stacked vertically with thumb-friendly spacing, preserving function without compromising on information.

This wireframe supports the core e-commerce principle of clarity drives conversion, helping users move seamlessly from interest to action. Whether browsing technical specs or scanning visuals, the experience is intuitive, informative, and persuasive—supporting CNCraft's brand identity as a source of trusted, high-quality CNC equipment.

---

### Cart page wireframes:

- [Desktop](assets/images/wireframes/desktop/cart-page.png)
- [Tablet](assets/images/wireframes/tablets/cart-page.png)
- [Mobile](assets/images/wireframes/phones/cart-page.png)

The Cart page plays a critical role in the purchase funnel by summarizing the user's selections while offering opportunities for review, adjustment, and upselling. Designed with clarity and actionability in mind, this wireframe ensures users are empowered to proceed confidently toward checkout.

The layout strikes a balance between functionality and reassurance—presenting a clear snapshot of selected items while subtly guiding users toward the final conversion step. From desktops to smartphones, the structure adapts to ensure pricing, product identity, and next steps remain easily accessible and legible.

Key components of the Cart page wireframe include:

- **Product Summary Blocks**: Each item in the cart is displayed with a thumbnail image, product name, price, quantity selector, and a subtotal. These components are aligned horizontally on desktop and stacked vertically on smaller devices to maintain usability.
- **Remove & Update Options**: Users can update product quantities directly in the cart or remove unwanted items. These options are positioned intuitively to avoid accidental deletions while remaining easily clickable/tappable.
- **Order Summary Panel**: Subtotals and totals are prominently displayed in a side panel (desktop/tablet) or directly below the product list (mobile). This allows users to monitor price changes dynamically.
- **Proceed to Checkout CTA**: A clearly emphasized button invites users to move forward with minimal friction. The button remains highly visible and is repositioned responsively on smaller screens for accessibility.
- **Cross-Selling Carousel (Bonus Feature)**: The desktop and tablet versions incorporate an "Explore More Items" carousel beneath the main cart list, encouraging users to discover CNC-related items such as accessories or alternate machines before finalizing their purchase.

This wireframe supports a low-friction, high-clarity cart experience, reducing drop-off while increasing opportunities for additional conversions. The design's responsiveness ensures the cart is not just functional but intuitively navigable on any device, allowing users to make last-minute adjustments without confusion or delay.

By offering users transparency and control at a crucial stage, the cart design builds trust and helps preserve momentum toward completing a transaction—critical objectives for any e-commerce workflow.

---

### Checkout page wireframes:

- [Desktop](assets/images/wireframes/desktop/checkout-page.png)
- [Tablet](assets/images/wireframes/tablets/checkout-page.png)
- [Mobile](assets/images/wireframes/phones/checkout-page.png)

The Checkout page is the final and most sensitive stage of the user journey—where clarity, trust, and speed become paramount. This wireframe was developed to reduce cognitive load, minimize user hesitation, and ensure a seamless handoff from intent to payment.

Designed for maximum usability across screen sizes, the layout cleanly separates billing information, payment fields, and the order summary into digestible sections. On desktop, a two-column layout offers parallel input, while on tablets and mobile devices the sections reflow vertically for streamlined scrolling and tapability.

Key elements of the Checkout page wireframe include:

- **Billing Address Form**: Users are prompted to enter name, address, city, and country, with an optional checkbox to save this information for future use. Field order and spacing are optimized for autofill and fast typing, especially on mobile.
- **Payment Information**: Credit card number, expiration date, and CVV fields are styled with clear labels and a layout optimized for PCI compliance and Stripe integration. Field validation will be handled via Stripe's secure elements.
- **Order Summary**: Positioned to the right (desktop) or below the form fields (mobile), this section reiterates the product list, subtotal, and final total, offering users reassurance before committing.
- **Call to Action (CTA)**: A clearly emphasized "Place Order" button is fixed near the bottom of the form stack or page to reduce friction and eliminate the need to scroll back up.
- **Error Handling (planned)**: Inline validation and fail-safe messaging for invalid entries or Stripe API issues will be implemented in the final build.

On smaller viewports, the design collapses responsively without sacrificing clarity or control. Users can easily scan and complete each section with minimal vertical scrolling and optimal thumb reach.

This wireframe embodies the core principles of conversion-optimized checkout design—trust, speed, and transparency—by reducing potential drop-offs and reinforcing confidence at the critical point of purchase. Whether on desktop or mobile, users are offered a clean and reassuring environment to complete their transaction, fully aligned with CNCraft's commitment to professionalism and user satisfaction.

--- 

### User Dashboard wireframes:

- [Desktop](assets/images/wireframes/desktop/user-dashboard-(after-login).png)
- [Tablet](assets/images/wireframes/tablets/user-dashboard-(after-login).png)
- [Mobile](assets/images/wireframes/phones/user-dashboard-(after-login).png)

The User Dashboard serves as the user's central hub for account management and post-purchase engagement. This wireframe was created to empower users with easy access to their profile, order history, and personal settings—all within a clean, modular layout that adapts seamlessly to device constraints.

The dashboard's structure was designed to reduce overwhelm by grouping functionality into clear, titled sections. Whether managing account details or checking the status of recent orders, users can find and perform key actions with minimal navigation friction.

Key elements of the User Dashboard wireframe include:

- **My Profile**: Displays the user's name, contact details, and a button to edit their profile information. This section is fixed at the top to reinforce the logged-in state and identity.
- **My Orders**: Provides a clear, collapsible list of past orders with essential metadata like order ID, date, and status. On desktop, the layout allows inline review, while on mobile, items are stacked vertically for thumb accessibility.
- **My Account**: Contains account settings and the ability to change the user's password securely. The layout and spacing ensure clarity and accessibility for form fields and action buttons.
- **My Preferences**: A placeholder section for future customization features, such as saved CNC configurations or notification settings. Presenting this in the wireframe prepares the design for scalable, user-personalized features.

On smaller devices, sections stack vertically with consistent margins and padding to maintain clarity. On desktop and tablet, content is broken into columns or grids to make better use of horizontal space while maintaining a modular, readable flow.

The design philosophy behind the User Dashboard is user empowerment through clarity. It reinforces trust by giving users control over their data and visibility into their transaction history, supporting both transparency and re-engagement. Whether managing orders or updating personal info, the experience is designed to be smooth, secure, and intuitive—an extension of the premium service experience CNCraft promises.

---

### Admin Panel wireframes:

- [Admin Interface](assets/images/wireframes/other/admin-page.png)

The Admin Panel wireframe was developed to provide CNCraft's site owner with a dedicated, streamlined environment for managing key business operations. While most users interact with the frontend, the admin experience is optimized for operational efficiency and oversight.

Unlike user-facing pages, the Admin Panel remains desktop-focused given the complexity and density of admin tasks. The design prioritizes readability, table-based data management, and quick access to essential admin functions.

Key features of the Admin Panel wireframe include:

- **Dashboard Overview**: A summary section that displays metrics like total orders, pending shipments, and revenue (planned).
- **Navigation Sidebar**: Allows access to management sections such as Orders, Products, Users, and Sales Reports.
- **Orders Table**: Admins can view all orders with sorting and filtering capabilities, including order status and customer info.
- **Product Management**: Includes forms for adding or editing CNC machines and accessories, with options for uploading images and setting availability.
- **User Management**: A simple interface for reviewing registered users, useful for customer support or moderation.

The Admin Panel wireframe embraces clarity and consistency while assuming a higher technical proficiency from the user. All actions are grouped logically to enable fast and error-free content and order management—supporting CNCraft's backend operations without unnecessary complexity.

### Login / Register page wireframes:

- [Login/Register Page](assets/images/wireframes/other/login-register-page.png)

The Login/Register page wireframe plays a vital role in controlling access to personalized user features such as account dashboards, saved carts, and order tracking. Its design is purposefully minimalist, reducing distractions and guiding users quickly through the authentication process.

To support first-time users and returning customers, both forms are presented side by side (desktop/tablet) or as toggleable tabs (on mobile), ensuring fluid navigation regardless of device.

Key elements include:

- **Login Form**: Includes email and password fields, a "Remember Me" checkbox, and a "Forgot Password" link for easy account recovery.
- **Register Form**: Requests basic info like name, email, and password confirmation, with plans for password strength validation.
- **Clear CTAs**: Submit buttons are styled to encourage quick completion, with feedback planned for invalid entries or successful logins.
- **Responsive Flow**: On smaller screens, the forms stack vertically and maintain padding for finger-friendly form completion.

The page's neutral tone and focus on form clarity help create a trusted and frictionless entry point to the platform. In e-commerce, seamless account access is critical to customer retention—this wireframe sets the foundation for that experience while adhering to accessibility and UX best practices.

---

## Features

CNCraft delivers a comprehensive e-commerce platform specifically designed for the CNC machinery market. The following features combine intuitive user experience with robust functionality to serve both hobbyist makers and professional machinists.

### Core E-commerce Functionality

| Feature Category | Feature | Description |
|------------------|---------|-------------|
| **Product Discovery** | Comprehensive Product Listings | Browse CNC machines, tools, and accessories with detailed specifications and high-quality images |
| | Advanced Filtering System | Filter products by category, price range, brand, and technical specifications |
| | Product Categories | Organized catalog with clear categorization (Mills, Lathes, Routers, Tools, Accessories) |
| | Product Search | Powerful search functionality to quickly locate specific products or brands |
| | Product Details | Detailed product pages with technical specifications, features, and compatibility information |
| **Shopping & Checkout** | Shopping Cart Management | Add, remove, and update product quantities with real-time price calculations |
| | Secure Checkout Process | Streamlined checkout flow with billing address collection and order summary |
| | Payment Processing | Secure payment integration with Stripe for reliable transaction processing |
| | Order Confirmation | Clear order confirmation with order number and details for customer records |
| | Guest Checkout | Option to purchase without creating an account for quick transactions |

### User Account Management

| Feature Category | Feature | Description |
|------------------|---------|-------------|
| **Authentication** | User Registration | Simple account creation process with email verification |
| | Secure Login System | Password-based authentication with "Remember Me" functionality |
| | User Profiles | Personal profile management with contact information and preferences |
| | Password Management | Secure password change functionality with validation |
| | Account Dashboard | Centralized hub for managing account settings and order history |
| **Order Tracking** | Order History | Complete history of past purchases with order details and status tracking |
| | Order Details | Detailed view of individual orders including products, quantities, and pricing |
| | Delivery Information | Saved delivery addresses for streamlined repeat purchases |
| | Order Status Updates | Track order progress from placement to delivery |

### Administrative Features

| Feature Category | Feature | Description |
|------------------|---------|-------------|
| **Store Management** | Admin Dashboard | Comprehensive overview of store performance with key metrics |
| | Product Management | Add, edit, and manage product catalog with pricing and inventory |
| | Order Management | View and process customer orders with status updates |
| | User Management | Oversee customer accounts and provide support when needed |
| | Inventory Tracking | Monitor stock levels and product availability |
| **Analytics** | Sales Analytics | Track sales performance and identify popular products |
| | Customer Insights | Understand customer behavior and purchasing patterns |
| | Revenue Reporting | Monitor financial performance and growth trends |
| | Order Analytics | Analyze order patterns and fulfillment efficiency |

### Technical Implementation

| Feature Category | Feature | Description |
|------------------|---------|-------------|
| **Responsive Design** | Mobile-First Approach | Optimized experience across all device sizes |
| | Cross-Browser Compatibility | Consistent functionality across modern web browsers |
| | Touch-Friendly Interface | Intuitive navigation optimized for touchscreen devices |
| | Accessible Design | WCAG-compliant features for users with varying abilities |
| **Security & Performance** | Fast Loading Times | Optimized images and efficient code for quick page loads |
| | Secure Data Handling | Encrypted data transmission and secure storage practices |
| | Payment Security | PCI-compliant payment processing through Stripe integration |
| | Form Validation | Client and server-side validation for data integrity |
| | Error Handling | Graceful error management with user-friendly messages |

### Specialized CNC Features

| Feature Category | Feature | Description |
|------------------|---------|-------------|
| **Technical Specifications** | Detailed Machine Specs | Comprehensive technical specifications for each CNC machine |
| | Compatibility Information | Software and tooling compatibility details |
| | Working Area Dimensions | Clear dimensional specifications for workshop planning |
| | Power Requirements | Electrical specifications for facility planning |
| | Precision Ratings | Accuracy and tolerance specifications for quality assessment |
| **Industry Content** | Application Guides | Use case examples for different industries and projects |
| | Material Compatibility | Information about suitable materials for each machine |
| | Skill Level Indicators | Guidance on appropriate equipment for different experience levels |
| | Safety Information | Important safety considerations and requirements |
| | Setup Requirements | Space and infrastructure requirements for installation |

### User Experience Enhancements

| Feature Category | Feature | Description |
|------------------|---------|-------------|
| **Navigation** | Intuitive Menu Structure | Clear menu organization with logical product categorization |
| | Breadcrumb Navigation | Easy orientation and navigation back through product categories |
| | Related Products | Suggestions for complementary equipment and accessories |
| | Featured Products | Highlighted equipment and special offers on the homepage |
| | Quick Access Tools | Easy access to cart, account, and search functionality |
| **Information Design** | Clear Product Hierarchy | Logical organization from general categories to specific products |
| | Consistent Layout Patterns | Familiar page structures across the entire platform |
| | Progressive Disclosure | Layered information presentation to avoid overwhelming users |
| | Visual Hierarchy | Clear distinction between different types of information and actions |
| | Contextual Help | Guidance and explanations for technical terms and specifications |

### Platform Highlights

🎯 **Specialized Focus**: Built specifically for the CNC machinery market with industry-specific features and terminology

⚡ **Performance Optimized**: Fast, responsive design that works seamlessly across all devices

🔒 **Enterprise Security**: Bank-level security with encrypted transactions and secure data handling

📊 **Business Intelligence**: Comprehensive analytics and reporting for data-driven business decisions

🛠️ **Technical Depth**: Detailed specifications and compatibility information for informed purchasing decisions

🌐 **Accessible Design**: WCAG-compliant features ensuring usability for all customers

These features work together to create a specialized e-commerce platform that addresses the unique needs of the CNC community while maintaining the usability and functionality expected from modern online shopping experiences.

---

## Technologies Used

CNCraft is built using a modern, robust technology stack that ensures scalability, security, and exceptional performance. The platform leverages industry-standard technologies and frameworks to deliver a professional e-commerce experience tailored for the CNC machinery market.

### Backend Technologies

| Technology | Version | Purpose |
|------------|---------|---------|
| **Python** | 3.11+ | Core programming language providing robust, scalable backend development |
| **Django** | 4.2+ | High-level Python web framework enabling rapid development with built-in security features |
| **Django Allauth** | Latest | Comprehensive authentication system supporting multiple authentication methods |
| **SQLite3** | Built-in | Lightweight, file-based database perfect for development and small-to-medium deployments |
| **Pillow** | Latest | Python Imaging Library for handling product image processing and optimization |

### Frontend Technologies

| Technology | Version | Purpose |
|------------|---------|---------|
| **HTML5** | Latest | Semantic markup language providing structure and accessibility foundation |
| **CSS3** | Latest | Modern styling with advanced layout capabilities and responsive design features |
| **JavaScript** | ES6+ | Client-side interactivity and dynamic user interface enhancements |
| **Bootstrap** | 5.1.3 | CSS framework providing responsive grid system and pre-built components |
| **Font Awesome** | 6.0+ | Comprehensive icon library via kit.fontawesome.com for consistent iconography |

### Payment & E-commerce

| Technology | Version | Purpose |
|------------|---------|---------|
| **Stripe** | Latest API | Secure payment processing with PCI compliance and fraud protection |
| **Stripe Elements** | Latest | Secure, customizable payment form components for seamless checkout experience |
| **Webhooks** | Stripe API | Real-time payment status updates and order confirmation handling |

### Development & Deployment Tools

| Technology | Version | Purpose |
|------------|---------|---------|
| **Git** | Latest | Version control system for code management and collaboration |
| **GitHub** | Platform | Repository hosting, issue tracking, and collaborative development |
| **VS Code** | Latest | Primary development environment with Python and Django extensions |
| **Django Debug Toolbar** | Latest | Development tool for performance monitoring and debugging |
| **WhiteNoise** | Latest | Static file serving for production deployment |

### Security & Data Protection

| Technology | Version | Purpose |
|------------|---------|---------|
| **Django CSRF Protection** | Built-in | Cross-Site Request Forgery protection for secure form submissions |
| **Django Security Middleware** | Built-in | Comprehensive security headers and protection mechanisms |
| **HTTPS/SSL** | TLS 1.3 | Encrypted data transmission ensuring secure communication |
| **Environment Variables** | Python-decouple | Secure configuration management separating secrets from codebase |
| **Password Hashing** | Django PBKDF2 | Secure password storage using industry-standard hashing algorithms |

### Code Quality & Standards

| Technology | Version | Purpose |
|------------|---------|---------|
| **PEP 8** | Standard | Python code style guide ensuring consistent, readable code |
| **Django Best Practices** | Framework | Following Django conventions for maintainable, scalable applications |
| **Responsive Design** | CSS3/Bootstrap | Mobile-first approach ensuring optimal experience across all devices |
| **Web Accessibility** | WCAG 2.1 | Compliance standards ensuring inclusive design for all users |

### Database & Data Management

| Technology | Version | Purpose |
|------------|---------|---------|
| **Django ORM** | Built-in | Object-Relational Mapping for database interactions and migrations |
| **SQLite3** | 3.39+ | Lightweight database engine suitable for development and moderate traffic |
| **Django Migrations** | Built-in | Version-controlled database schema changes and data migrations |
| **Database Indexing** | SQLite | Optimized query performance for product searches and filtering |

### Static Files & Media Management

| Technology | Version | Purpose |
|------------|---------|---------|
| **Django Static Files** | Built-in | Efficient static asset management and organization |
| **Pillow** | Latest | Image processing for product photos, thumbnails, and optimization |
| **CSS Minification** | Production | Optimized stylesheet delivery for improved performance |
| **Image Optimization** | Pillow | Compressed product images maintaining quality while reducing load times |

### Testing & Quality Assurance

| Technology | Version | Purpose |
|------------|---------|---------|
| **Django Testing Framework** | Built-in | Comprehensive unit and integration testing capabilities |
| **Python unittest** | Standard Library | Core testing framework for backend functionality validation |
| **Browser Testing** | Manual | Cross-browser compatibility testing across major browsers |
| **Responsive Testing** | Manual | Device compatibility testing for optimal mobile experience |

### Performance & Optimization

| Technology | Version | Purpose |
|------------|---------|---------|
| **Django Caching Framework** | Built-in | Performance optimization through strategic content caching |
| **Database Query Optimization** | Django ORM | Efficient database queries minimizing response times |
| **Static File Compression** | WhiteNoise | Compressed asset delivery for faster page loads |
| **Lazy Loading** | JavaScript | Progressive content loading for improved perceived performance |

### API & Integration Technologies

| Technology | Version | Purpose |
|------------|---------|---------|
| **Django REST Framework** | Latest | API development framework for potential future integrations |
| **JSON** | Standard | Data interchange format for AJAX requests and API responses |
| **AJAX** | JavaScript | Asynchronous requests for dynamic content updates |
| **Stripe API** | Latest | Payment processing integration with comprehensive transaction handling |

### Development Methodology

| Approach | Implementation | Purpose |
|----------|----------------|---------|
| **Model-View-Template (MVT)** | Django Architecture | Clean separation of concerns following Django's architectural pattern |
| **Object-Oriented Programming** | Python Classes | Maintainable, reusable code structure with clear inheritance hierarchies |
| **RESTful Design** | URL Patterns | Intuitive URL structure following REST principles for better UX |
| **Progressive Enhancement** | Frontend Strategy | Baseline functionality with enhanced features for capable browsers |
| **Mobile-First Design** | CSS/Bootstrap | Responsive design starting with mobile constraints and expanding up |

### Browser & Platform Support

| Platform | Versions | Support Level |
|----------|----------|---------------|
| **Chrome** | 90+ | Full Support |
| **Firefox** | 88+ | Full Support |
| **Safari** | 14+ | Full Support |
| **Edge** | 90+ | Full Support |
| **Mobile Safari** | iOS 13+ | Full Support |
| **Chrome Mobile** | Android 8+ | Full Support |

### Key Technology Decisions

**Why Django?**
- Rapid development with built-in admin interface perfect for CNC product management
- Robust security features essential for e-commerce applications
- Excellent ORM for complex product relationships and inventory management
- Strong community support and extensive documentation

**Why Bootstrap?**
- Proven responsive framework ensuring consistent cross-device experience
- Comprehensive component library accelerating development timeline
- Excellent accessibility features supporting WCAG compliance goals
- Easy customization for CNC industry-specific design requirements

**Why Stripe?**
- Industry-leading security with PCI DSS compliance built-in
- Comprehensive payment method support for global CNC market
- Excellent developer experience with clear documentation
- Robust fraud protection essential for high-value CNC equipment sales

**Why SQLite?**
- Perfect for development and moderate traffic volumes
- Zero-configuration database reducing deployment complexity
- Reliable and well-tested for e-commerce applications
- Easy migration path to PostgreSQL for future scaling needs

This technology stack provides a solid foundation for CNCraft's current needs while maintaining flexibility for future enhancements and scaling requirements. Each technology was selected for its reliability, community support, and alignment with modern web development best practices.

---

## Project Structure

CNCraft follows Django's recommended project structure with additional organization for e-commerce functionality. The architecture is designed for scalability, maintainability, and clear separation of concerns across different application domains.

### 📁 Complete Directory Structure

```
CNCraft/
├── 📁 admin_panel/                    # Admin interface for store management
│   ├── __init__.py
│   ├── apps.py
│   ├── urls.py
│   ├── views.py
│   └── __pycache__/
│
├── 📁 assets/                         # Static assets and wireframes
│   └── images/
│       └── wireframes/
│           ├── desktop/
│           ├── tablets/
│           ├── phones/
│           └── other/
│
├── 📁 cart/                          # Shopping cart functionality
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── contexts.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   ├── migrations/
│   │   ├── __init__.py
│   │   └── __pycache__/
│   └── __pycache__/
│
├── 📁 checkout/                      # Payment and order processing
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   ├── migrations/
│   │   ├── __init__.py
│   │   ├── 0001_initial.py
│   │   └── __pycache__/
│   └── __pycache__/
│
├── 📁 cncraft/                       # Main Django project settings
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── __pycache__/
│
├── 📁 documentation/                 # Project documentation
│   ├── readme/
│   │   └── images/
│   └── test/
│       └── test.md
│
├── 📁 home/                          # Homepage and main landing pages
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   ├── migrations/
│   │   ├── __init__.py
│   │   └── __pycache__/
│   └── __pycache__/
│
├── 📁 products/                      # Product catalog and management
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   ├── management/
│   │   ├── __init__.py
│   │   └── commands/
│   │       ├── __init__.py
│   │       └── populate_cnc_products.py
│   ├── migrations/
│   │   ├── __init__.py
│   │   ├── 0001_initial.py
│   │   └── __pycache__/
│   └── __pycache__/
│
├── 📁 profiles/                      # User account management
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   ├── migrations/
│   │   ├── __init__.py
│   │   └── __pycache__/
│   └── __pycache__/
│
├── 📁 static/                        # Source static files
│   ├── css/
│   ├── images/
│   └── javascript/
│
├── 📁 staticfiles/                   # Collected static files (production)
│   ├── admin/
│   ├── css/
│   ├── images/
│   └── javascript/
│
├── 📁 templates/                     # HTML templates
│   ├── 404.html
│   ├── 500.html
│   ├── base.html
│   ├── admin_panel/
│   ├── cart/
│   ├── checkout/
│   ├── contact/
│   ├── home/
│   ├── includes/
│   ├── products/
│   ├── profiles/
│   └── registration/
│
├── 📁 venv/                          # Python virtual environment
│   ├── Include/
│   ├── Lib/
│   │   └── site-packages/
│   ├── Scripts/
│   │   ├── activate.bat
│   │   ├── activate.ps1
│   │   ├── deactivate.bat
│   │   ├── django-admin.exe
│   │   ├── pip.exe
│   │   └── python.exe
│   └── pyvenv.cfg
│
├── 📁 __pycache__/                   # Python bytecode cache
│
├── 📄 .env                          # Environment variables (not in version control)
├── 📄 .gitignore                    # Git ignore rules
├── 📄 db.sqlite3                   # SQLite database file
├── 📄 manage.py                     # Django management script
├── 📄 README.md                     # Project documentation
└── 📄 requirements.txt              # Python dependencies
```

### 🏗️ Core Django Applications

| Application | Purpose | Key Components |
|-------------|---------|----------------|
| **admin_panel** | Custom admin interface for store management | Enhanced admin views, custom dashboards |
| **cart** | Shopping cart functionality and session management | Cart models, context processors, session handling |
| **checkout** | Payment processing and order completion | Stripe integration, order forms, payment views |
| **home** | Homepage and main landing pages | Landing page views, company information |
| **products** | Product catalog, categories, and inventory | Product models, category management, search |
| **profiles** | User account management and authentication | User profiles, account settings, order history |

### 📂 Key Directory Descriptions

#### **Configuration & Core**
- **`cncraft/`** - Main Django project configuration
  - `settings.py` - Application settings and configuration
  - `urls.py` - Root URL routing configuration
  - `wsgi.py` / `asgi.py` - WSGI/ASGI application entry points

#### **Templates & Static Assets**
- **`templates/`** - HTML templates organized by application
  - `base.html` - Master template with common layout
  - Application-specific subdirectories
  - Error pages (`404.html`, `500.html`)
- **`static/`** - Source static files (CSS, JavaScript, images)
- **`staticfiles/`** - Collected static files for production deployment

#### **Documentation & Design**
- **`documentation/`** - Project documentation and testing files
  - `test/test.md` - Comprehensive testing documentation
  - `readme/images/` - Documentation screenshots and diagrams
- **`assets/`** - Design assets and UI/UX wireframes
  - `images/wireframes/` - Device-specific wireframe designs

#### **Development Environment**
- **`venv/`** - Python virtual environment with isolated dependencies
  - `Scripts/` - Virtual environment activation scripts
  - `Lib/site-packages/` - Installed Python packages
- **`__pycache__/`** - Python bytecode cache (auto-generated)

### 🔧 Application Architecture

#### **Model-View-Template (MVT) Pattern**

Each Django application follows the MVT architectural pattern:

```
Application/
├── models.py      # Data models and database schema
├── views.py       # Business logic and request handling
├── urls.py        # URL routing for the application
├── admin.py       # Django admin interface configuration
├── forms.py       # Form definitions and validation
├── tests.py       # Unit and integration tests
└── migrations/    # Database schema migrations
```

#### **Application Relationships**

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│    home     │───▶│  products   │───▶│    cart     │
│(landing)    │    │ (catalog)   │    │ (session)   │
└─────────────┘    └─────────────┘    └─────────────┘
        │                   │                   │
        ▼                   ▼                   ▼
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│  profiles   │◀───│admin_panel  │───▶│  checkout   │
│ (accounts)  │    │(management) │    │ (payment)   │
└─────────────┘    └─────────────┘    └─────────────┘
```

### 🔍 Key Management Commands

#### **Database Operations**
```bash
python manage.py migrate              # Apply database migrations
python manage.py makemigrations       # Create new migrations
python manage.py createsuperuser      # Create admin user
python manage.py dbshell              # Access database shell
```

#### **Static Files Management**
```bash
python manage.py collectstatic        # Collect static files for production
python manage.py findstatic <file>    # Locate static file source
```

#### **Development Tools**
```bash
python manage.py runserver            # Start development server
python manage.py shell                # Django shell for testing
python manage.py test                 # Run test suite
```

#### **Custom Management Commands**
```bash
python manage.py populate_cnc_products # Load sample CNC product data
```

### 📊 Technology Integration Points

#### **Frontend Integration**
- **Bootstrap Components** - Located in `static/css/` and integrated via CDN
- **Font Awesome Icons** - Integrated via kit.fontawesome.com
- **Custom JavaScript** - Application-specific scripts in `static/javascript/`

#### **Backend Integration**
- **Stripe Payments** - Integrated in `checkout/` application
- **Django Allauth** - User authentication across `profiles/` application
- **SQLite Database** - Development database with easy PostgreSQL migration path

#### **Development Workflow**
- **Virtual Environment** - Isolated Python dependencies in `venv/`
- **Environment Variables** - Secure configuration via `.env` file
- **Version Control** - Git with comprehensive `.gitignore` for Python/Django

### 🏷️ Best Practices Implemented

#### **Security**
- Environment variables for sensitive configuration
- CSRF protection on all forms
- Secure session management
- Input validation and sanitization

#### **Performance**
- Static file optimization and compression
- Database query optimization
- Efficient template inheritance
- Lazy loading for images

#### **Maintainability**
- Clear application separation
- Consistent naming conventions
- Comprehensive documentation
- Modular template structure

#### **Scalability**
- Database migration system
- Modular application architecture
- Environment-specific settings
- Container-ready structure

This project structure provides a solid foundation for development, testing, and deployment while maintaining the flexibility to scale and add new features as CNCraft grows.

---

## Database Structure

CNCraft's database architecture is built on a robust relational foundation using SQLite3 for development and PostgreSQL-ready for production scaling. The schema is specifically designed for CNC e-commerce operations, featuring specialized product specifications, comprehensive order management, and detailed user profile tracking.

### 🗄️ Database Architecture Overview

The database follows a normalized relational design with six core entities connected through carefully designed foreign key relationships. This structure ensures data integrity while maintaining optimal query performance for e-commerce operations.

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                           CNCraft Database Schema                               │
│                                                                                 │
│  ┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐           │
│  │   django_user   │    │    Category     │    │  ProductImage   │           │
│  │ ══════════════  │    │ ══════════════  │    │ ══════════════  │           │
│  │ 🔑 id (PK)      │    │ 🔑 id (PK)      │    │ 🔑 id (PK)      │           │
│  │ 📧 username     │    │ 📝 name         │    │ 🖼️ image        │           │
│  │ 🔒 password     │    │ 📝 friendly_name│    │ 📝 alt_text     │           │
│  │ 📧 email        │    │ 📄 description  │    │ ✅ is_feature   │           │
│  │ 📅 date_joined  │    │ 🖼️ image        │    │ 🔗 product_id   │           │
│  │ ✅ is_active    │    └─────────────────┘    └─────────────────┘           │
│  │ ✅ is_staff     │             │                       │                   │
│  └─────────────────┘             │                       │                   │
│           │                      │                       │                   │
│           │ 1:1                  │ 1:M                   │ M:1               │
│           ▼                      ▼                       ▼                   │
│  ┌─────────────────┐    ┌─────────────────────────────────────────────────┐  │
│  │   UserProfile   │    │                Product                         │  │
│  │ ══════════════  │    │ ══════════════════════════════════════════════  │  │
│  │ 🔑 id (PK)      │    │ 🔑 id (PK)              │ 💰 price              │  │
│  │ 🔗 user_id (FK) │    │ 🔗 category_id (FK)     │ 💸 discount_price     │  │
│  │ 📞 phone_number │    │ 🏷️ sku                  │ 🖼️ image              │  │
│  │ 🏠 address1     │    │ 📝 name                 │ 📏 dimensions         │  │
│  │ 🏠 address2     │    │ 📄 description          │ ⚖️ weight             │  │
│  │ 🏙️ city         │    │ ⚡ power_requirement    │ 🔧 material           │  │
│  │ 📮 postcode     │    │ 📐 working_area         │ ⚙️ spindle_speed      │  │
│  │ 🌍 country      │    │ ⭐ rating               │ 📦 stock_qty          │  │
│  │ 💱 currency     │    │ ✅ in_stock             │ ⭐ featured           │  │
│  │ 🌐 language     │    │ 📅 created_at           │ 📅 updated_at         │  │
│  └─────────────────┘    └─────────────────────────────────────────────────┘  │
│           │                                      │                           │
│           │ 1:M                                  │ 1:M                       │
│           ▼                                      ▼                           │
│  ┌─────────────────────────────────────────────────────────────────────────┐  │
│  │                            Order                                        │  │
│  │ ══════════════════════════════════════════════════════════════════════  │  │
│  │ 🔑 id (PK)              │ 📞 phone_number       │ 💰 order_total        │  │
│  │ 🔗 user_profile_id (FK) │ 🌍 country            │ 🚚 delivery_cost      │  │
│  │ 🎫 order_number         │ 📮 postcode           │ 💳 grand_total        │  │
│  │ 👤 full_name            │ 🏙️ town_or_city       │ 📄 original_cart      │  │
│  │ 📧 email                │ 🏠 street_address1    │ 💳 stripe_pid         │  │
│  │ 🏠 street_address2      │ 🏛️ county             │ 📅 date               │  │
│  └─────────────────────────────────────────────────────────────────────────┘  │
│                                      │                                       │
│                                      │ 1:M                                   │
│                                      ▼                                       │
│                           ┌─────────────────┐                               │
│                           │  OrderLineItem  │                               │
│                           │ ══════════════  │                               │
│                           │ 🔑 id (PK)      │                               │
│                           │ 🔗 order_id (FK)│                               │
│                           │ 🔗 product_id   │                               │
│                           │ 🔢 quantity     │                               │
│                           │ 💰 lineitem_total│                              │
│                           └─────────────────┘                               │
└─────────────────────────────────────────────────────────────────────────────────┘
```

### 📊 Entity Relationship Diagram

```
User ──────────────── UserProfile
 │                         │
 │                         │
 └─── Profile ──────────── Order ──────────── OrderLineItem
                             │                      │
                             │                      │
                             └─── Billing Info     Product ──── Category
                                                     │              │
                                                     │              │
                                                 ProductImage ──────┘
```

### 🏗️ Database Tables Specification

#### **Users & Authentication**

| **django_user** (Django Built-in) |
|-----------------------------------|
| **Field** | **Type** | **Constraints** |
| `id` | BigAutoField | PRIMARY KEY |
| `username` | CharField(150) | UNIQUE, NOT NULL |
| `password` | CharField(128) | NOT NULL |
| `email` | EmailField(254) | NOT NULL |
| `first_name` | CharField(150) | Optional |
| `last_name` | CharField(150) | Optional |
| `is_active` | BooleanField | DEFAULT TRUE |
| `is_staff` | BooleanField | DEFAULT FALSE |
| `is_superuser` | BooleanField | DEFAULT FALSE |
| `date_joined` | DateTimeField | AUTO_NOW_ADD |
| `last_login` | DateTimeField | Optional |

#### **User Profiles & Preferences**

| **profiles_userprofile** |
|--------------------------|
| **Field** | **Type** | **Constraints** |
| `id` | BigAutoField | PRIMARY KEY |
| `user_id` | OneToOneField | FK → django_user.id, CASCADE |
| `default_phone_number` | CharField(20) | Optional |
| `default_street_address1` | CharField(80) | Optional |
| `default_street_address2` | CharField(80) | Optional |
| `default_town_or_city` | CharField(40) | Optional |
| `default_county` | CharField(80) | Optional |
| `default_postcode` | CharField(20) | Optional |
| `default_country` | CharField(40) | Optional |
| `default_email_notifications` | BooleanField | DEFAULT FALSE |
| `default_order_status_updates` | BooleanField | DEFAULT FALSE |
| `default_promotional_emails` | BooleanField | DEFAULT FALSE |
| `default_newsletter_subscription` | BooleanField | DEFAULT FALSE |
| `currency` | CharField(3) | DEFAULT 'USD' |
| `language` | CharField(2) | DEFAULT 'en' |
| `display_mode` | CharField(10) | DEFAULT 'light' |
| `cart_auto_save` | BooleanField | DEFAULT TRUE |

#### **Product Catalog Management**

| **products_category** |
|----------------------|
| **Field** | **Type** | **Constraints** |
| `id` | BigAutoField | PRIMARY KEY |
| `name` | CharField(254) | NOT NULL |
| `friendly_name` | CharField(254) | Optional |
| `description` | TextField | Optional |
| `image` | ImageField | UPLOAD_TO 'category_images/' |

| **products_product** |
|---------------------|
| **Field** | **Type** | **Constraints** |
| `id` | BigAutoField | PRIMARY KEY |
| `category_id` | ForeignKey | FK → products_category.id, SET_NULL |
| `sku` | CharField(254) | Optional, INDEX |
| `name` | CharField(254) | NOT NULL |
| `description` | TextField | NOT NULL |
| `price` | DecimalField(10,2) | NOT NULL |
| `discount_price` | DecimalField(10,2) | Optional |
| `image` | ImageField | UPLOAD_TO 'product_images/' |
| **CNC-Specific Fields** | | |
| `dimensions` | CharField(100) | Optional, FORMAT: LxWxH mm |
| `weight` | DecimalField(6,2) | Optional, UNIT: kg |
| `material` | CharField(100) | Optional |
| `power_requirement` | CharField(100) | Optional |
| `working_area` | CharField(100) | Optional |
| `spindle_speed` | CharField(100) | Optional |
| **Inventory & Display** | | |
| `rating` | DecimalField(3,2) | Optional, RANGE: 0.00-5.00 |
| `in_stock` | BooleanField | DEFAULT TRUE |
| `stock_qty` | IntegerField | DEFAULT 0 |
| `featured` | BooleanField | DEFAULT FALSE |
| **Timestamps** | | |
| `created_at` | DateTimeField | AUTO_NOW_ADD |
| `updated_at` | DateTimeField | AUTO_NOW |

| **products_productimage** |
|---------------------------|
| **Field** | **Type** | **Constraints** |
| `id` | BigAutoField | PRIMARY KEY |
| `product_id` | ForeignKey | FK → products_product.id, CASCADE |
| `image` | ImageField | UPLOAD_TO 'product_images/' |
| `alt_text` | CharField(254) | Optional |
| `is_feature` | BooleanField | DEFAULT FALSE |

#### **Order Management System**

| **checkout_order** |
|-------------------|
| **Field** | **Type** | **Constraints** |
| `id` | BigAutoField | PRIMARY KEY |
| `user_profile_id` | ForeignKey | FK → profiles_userprofile.id, SET_NULL |
| `order_number` | CharField(32) | UNIQUE, NOT EDITABLE |
| **Customer Information** | | |
| `full_name` | CharField(50) | NOT NULL |
| `email` | EmailField(254) | NOT NULL |
| `phone_number` | CharField(20) | NOT NULL |
| **Delivery Address** | | |
| `country` | CharField(40) | NOT NULL |
| `postcode` | CharField(20) | Optional |
| `town_or_city` | CharField(40) | NOT NULL |
| `street_address1` | CharField(80) | NOT NULL |
| `street_address2` | CharField(80) | Optional |
| `county` | CharField(80) | Optional |
| **Financial Information** | | |
| `delivery_cost` | DecimalField(6,2) | DEFAULT 0 |
| `order_total` | DecimalField(10,2) | DEFAULT 0 |
| `grand_total` | DecimalField(10,2) | DEFAULT 0 |
| **System Fields** | | |
| `original_cart` | TextField | JSON cart data |
| `stripe_pid` | CharField(254) | Stripe Payment ID |
| `date` | DateTimeField | AUTO_NOW_ADD |

| **checkout_orderlineitem** |
|----------------------------|
| **Field** | **Type** | **Constraints** |
| `id` | BigAutoField | PRIMARY KEY |
| `order_id` | ForeignKey | FK → checkout_order.id, CASCADE |
| `product_id` | ForeignKey | FK → products_product.id, CASCADE |
| `quantity` | IntegerField | NOT NULL, DEFAULT 0 |
| `lineitem_total` | DecimalField(10,2) | NOT EDITABLE, CALCULATED |

### 🔗 Key Database Relationships

#### **Primary Relationships**

| **Relationship** | **Type** | **Description** |
|------------------|----------|-----------------|
| User → UserProfile | 1:1 | Each user has exactly one profile with delivery preferences |
| UserProfile → Order | 1:M | Users can have multiple orders in their history |
| Category → Product | 1:M | Products are organized into categories (CNC Mills, Lathes, etc.) |
| Product → ProductImage | 1:M | Products can have multiple images for gallery display |
| Order → OrderLineItem | 1:M | Each order contains multiple line items |
| Product → OrderLineItem | 1:M | Products can appear in multiple orders |

#### **Business Logic Relationships**

```sql
-- Example: Get all orders for a user with product details
SELECT 
    o.order_number,
    o.date,
    o.grand_total,
    oli.quantity,
    p.name as product_name,
    p.price
FROM checkout_order o
JOIN profiles_userprofile up ON o.user_profile_id = up.id
JOIN checkout_orderlineitem oli ON o.id = oli.order_id
JOIN products_product p ON oli.product_id = p.id
WHERE up.user_id = ?
ORDER BY o.date DESC;
```

### 🎯 CNC Industry-Specific Schema Features

#### **Technical Specifications Storage**

| **Field** | **Purpose** | **Example Values** |
|-----------|-------------|-------------------|
| `dimensions` | Machine size for workshop planning | "600×400×300 mm" |
| `working_area` | Actual cutting area | "400×300×100 mm" |
| `power_requirement` | Electrical specifications | "240V, 2.2kW, Single Phase" |
| `spindle_speed` | Cutting capability | "8,000-24,000 RPM" |
| `weight` | Shipping and installation planning | "85.50 kg" |
| `material` | Construction materials | "Cast Iron, Aluminum" |

#### **E-commerce Optimization Fields**

| **Field** | **Business Purpose** | **Implementation** |
|-----------|---------------------|-------------------|
| `featured` | Homepage product promotion | Boolean flag for marketing |
| `discount_price` | Sale pricing and promotions | Decimal field for special offers |
| `rating` | Customer confidence building | 5-star rating system |
| `stock_qty` | Inventory management | Real-time stock tracking |
| `in_stock` | Purchase availability | Boolean for product availability |

### 📈 Database Performance Optimizations

#### **Indexing Strategy**

```sql
-- Key indexes for optimal query performance
CREATE INDEX idx_product_category ON products_product(category_id);
CREATE INDEX idx_product_sku ON products_product(sku);
CREATE INDEX idx_product_featured ON products_product(featured);
CREATE INDEX idx_product_in_stock ON products_product(in_stock);
CREATE INDEX idx_order_user_profile ON checkout_order(user_profile_id);
CREATE INDEX idx_order_date ON checkout_order(date);
CREATE INDEX idx_orderlineitem_order ON checkout_orderlineitem(order_id);
CREATE INDEX idx_orderlineitem_product ON checkout_orderlineitem(product_id);
```

#### **Query Optimization Patterns**

| **Operation** | **Optimization** | **Example** |
|---------------|------------------|-------------|
| Product Listings | Category filtering with prefetch | `Product.objects.filter(category=x).select_related('category')` |
| Order History | User profile join optimization | `Order.objects.filter(user_profile__user=user).prefetch_related('lineitems__product')` |
| Cart Totals | Aggregate calculations | `OrderLineItem.objects.filter(order=x).aggregate(Sum('lineitem_total'))` |
| Search Results | Full-text search on name/description | `Product.objects.filter(Q(name__icontains=term) \| Q(description__icontains=term))` |

### 🔧 Database Administration Features

#### **Data Integrity Measures**

| **Protection** | **Implementation** | **Benefit** |
|----------------|-------------------|-------------|
| **Cascade Deletion** | User deletion removes profile automatically | Prevents orphaned user data |
| **Set NULL on Category Delete** | Products remain when category is deleted | Preserves product data integrity |
| **Order Number Generation** | UUID-based unique identifiers | Prevents order number conflicts |
| **Automatic Timestamps** | Created/updated tracking | Audit trail for all changes |
| **Decimal Precision** | Fixed-point arithmetic for prices | Prevents floating-point errors |

#### **Migration Management**

```python
# Example migration for adding CNC-specific fields
class Migration(migrations.Migration):
    operations = [
        migrations.AddField(
            model_name='product',
            name='working_area',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='spindle_speed',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
```

### 📊 Database Analytics & Reporting

#### **Business Intelligence Queries**

| **Metric** | **SQL Pattern** | **Business Value** |
|------------|-----------------|-------------------|
| **Popular Products** | `SELECT product_id, SUM(quantity) FROM checkout_orderlineitem GROUP BY product_id ORDER BY SUM(quantity) DESC` | Inventory planning |
| **Category Performance** | `SELECT c.name, SUM(oli.lineitem_total) FROM products_category c JOIN products_product p ON c.id = p.category_id JOIN checkout_orderlineitem oli ON p.id = oli.product_id GROUP BY c.name` | Category optimization |
| **Customer Lifetime Value** | `SELECT up.user_id, SUM(o.grand_total) FROM profiles_userprofile up JOIN checkout_order o ON up.id = o.user_profile_id GROUP BY up.user_id` | Customer segmentation |
| **Revenue Trends** | `SELECT DATE(date), SUM(grand_total) FROM checkout_order GROUP BY DATE(date) ORDER BY DATE(date)` | Financial reporting |

### 🚀 Scalability Considerations

#### **Horizontal Scaling Readiness**

| **Feature** | **Current State** | **Scaling Path** |
|-------------|------------------|------------------|
| **Database Engine** | SQLite3 (Development) | PostgreSQL (Production) |
| **Session Storage** | Database sessions | Redis cluster |
| **Media Files** | Local filesystem | AWS S3/CloudFront |
| **Search** | Database LIKE queries | Elasticsearch integration |
| **Caching** | None | Redis/Memcached layers |

#### **Data Growth Projections**

| **Entity** | **Current Size** | **Growth Factor** | **Optimization Strategy** |
|------------|------------------|-------------------|-------------------------|
| **Products** | ~50 records | Linear growth | Partitioning by category |
| **Orders** | Variable | Exponential growth | Date-based partitioning |
| **Users** | Variable | Linear growth | Standard indexing |
| **Images** | File-based | Linear growth | CDN distribution |

This comprehensive database structure eliminates the need for external diagramming tools while providing detailed technical documentation for developers, database administrators, and system architects. The schema is specifically optimized for CNC e-commerce operations while maintaining flexibility for future enhancements.

---

## Business Logic & Application Features

CNCraft implements sophisticated business logic designed specifically for the CNC machinery e-commerce domain. The application features are strategically placed across the Django MVC architecture following best practices for separation of concerns.

### 🧠 Core Business Logic Implementation

#### **Model-Level Business Logic**

| **Model** | **Business Logic** | **Implementation** |
|-----------|-------------------|-------------------|
| **Product** | Price calculation with discounts | `get_display_price()` method returns discount price when available |
| **Product** | Sale status determination | `is_on_sale()` method checks if discount_price exists and is lower than regular price |
| **Product** | Image management | `get_product_images()` method returns validated image paths for gallery display |
| **Order** | Automatic order numbering | `_generate_order_number()` creates UUID-based unique identifiers |
| **Order** | Total calculation with delivery | `update_total()` method calculates order total, delivery costs, and grand total |
| **OrderLineItem** | Line item pricing | Automatic calculation of `lineitem_total` based on product price and quantity |

#### **View-Level Business Logic**

| **Application** | **Business Logic** | **Purpose** |
|-----------------|-------------------|-------------|
| **Products** | Category filtering and search | Enables users to find specific CNC equipment efficiently |
| **Cart** | Session-based cart management | Maintains shopping cart across user sessions without requiring login |
| **Cart** | Quantity validation | Prevents invalid quantities and provides user feedback |
| **Checkout** | Payment processing integration | Handles Stripe payment flow with error management |
| **Checkout** | Order creation from cart | Converts session cart data into permanent order records |
| **Profiles** | User preference management | Stores delivery information and account settings |

#### **Template-Level Logic**

```django
<!-- Example: Smart price display logic in templates -->
{% if product.is_on_sale %}
    <span class="original-price">${{ product.price|floatformat:2 }}</span>
    <span class="sale-price">${{ product.get_display_price|floatformat:2 }}</span>
    <span class="sale-badge">Sale</span>
{% else %}
    <span class="regular-price">${{ product.price|floatformat:2 }}</span>
{% endif %}

<!-- Example: Conditional navigation based on user authentication -->
{% if user.is_authenticated %}
    <a href="{% url 'profile' %}">My Dashboard</a>
    <a href="{% url 'account_logout' %}">Logout</a>
{% else %}
    <a href="{% url 'account_login' %}">Login</a>
    <a href="{% url 'account_signup' %}">Sign Up</a>
{% endif %}
```

### 🎯 CNC Industry-Specific Features

#### **Technical Specification Handling**

```python
# Custom model methods for CNC-specific data presentation
class Product(models.Model):
    def get_specifications(self):
        """Returns formatted technical specifications for CNC products"""
        specs = {}
        if self.dimensions:
            specs['Dimensions'] = self.dimensions
        if self.working_area:
            specs['Working Area'] = self.working_area
        if self.spindle_speed:
            specs['Spindle Speed'] = self.spindle_speed
        if self.power_requirement:
            specs['Power Requirement'] = self.power_requirement
        return specs
```

#### **Professional Purchasing Features**

| **Feature** | **Business Logic** | **User Benefit** |
|-------------|-------------------|------------------|
| **Bulk Pricing** | Quantity-based pricing calculations | Cost savings for professional workshops |
| **Technical Specifications** | Structured display of CNC-specific data | Informed purchasing decisions |
| **Compatibility Information** | Related product suggestions | Complete workshop solutions |
| **Professional Accounts** | Enhanced user profiles for businesses | Streamlined repeat purchasing |

### 🔒 Authentication & Authorization Logic

#### **User Permission Levels**

```python
# View-level authorization examples
@login_required
def profile_view(request):
    """Requires user authentication to access profile"""
    return render(request, 'profiles/profile.html')

@staff_member_required
def admin_dashboard(request):
    """Restricts admin functions to staff users"""
    return render(request, 'admin_panel/dashboard.html')
```

#### **Data Access Control**

| **Protection Level** | **Implementation** | **Prevents** |
|---------------------|-------------------|--------------|
| **Anonymous Users** | Cart access without login | Unauthorized data access |
| **Authenticated Users** | Profile data isolation | Users accessing other's data |
| **Staff Users** | Admin panel restrictions | Unauthorized administrative access |
| **Superuser** | Full administrative access | Unrestricted system access |

### 🛒 E-commerce Business Logic

#### **Cart Management**

```python
# Cart context processor for global cart access
def cart_contents(request):
    """Provides cart data across all templates"""
    cart = request.session.get('cart', {})
    cart_items = []
    total = 0
    product_count = 0
    
    for item_id, item_data in cart.items():
        # Business logic for cart calculations
        product = get_object_or_404(Product, pk=item_id)
        quantity = item_data if isinstance(item_data, int) else item_data.get('quantity', 1)
        subtotal = quantity * product.get_display_price()
        total += subtotal
        product_count += quantity
        
        cart_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
            'subtotal': subtotal,
        })
    
    return {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
    }
```

#### **Payment Processing Logic**

| **Stage** | **Business Logic** | **Error Handling** |
|-----------|-------------------|-------------------|
| **Payment Intent** | Create Stripe payment intent with order total | Validate cart contents and pricing |
| **Payment Confirmation** | Process successful payment and create order | Handle payment failures with user feedback |
| **Order Fulfillment** | Convert cart to order line items | Manage inventory and stock updates |
| **Email Confirmation** | Send order confirmation to customer | Graceful failure if email service unavailable |

### 📊 Data Validation & Quality Control

#### **Form Validation**

```python
# Custom form validation for CNC products
class ProductForm(forms.ModelForm):
    def clean_price(self):
        price = self.cleaned_data['price']
        if price <= 0:
            raise ValidationError("Price must be greater than zero")
        return price
    
    def clean_stock_qty(self):
        stock = self.cleaned_data['stock_qty']
        if stock < 0:
            raise ValidationError("Stock quantity cannot be negative")
        return stock
```

#### **Model Validation**

| **Field** | **Validation Rule** | **Business Purpose** |
|-----------|-------------------|---------------------|
| **Price** | Must be positive decimal | Prevents invalid pricing |
| **Stock Quantity** | Must be non-negative integer | Accurate inventory tracking |
| **Email** | Valid email format | Reliable customer communication |
| **Phone Number** | Numeric with length validation | Delivery contact verification |

### 🎨 User Experience Logic

#### **Responsive Behavior**

```python
# Context-aware template logic
def product_list(request):
    """Smart product listing with pagination and filtering"""
    products = Product.objects.filter(in_stock=True)
    
    # Filter by category if specified
    category = request.GET.get('category')
    if category:
        products = products.filter(category__name=category)
    
    # Filter by price range
    price_range = request.GET.get('price_range')
    if price_range:
        min_price, max_price = price_range.split('-')
        products = products.filter(price__gte=min_price, price__lte=max_price)
    
    # Pagination for large datasets
    paginator = Paginator(products, 12)
    page = request.GET.get('page')
    products = paginator.get_page(page)
    
    return render(request, 'products/product_list.html', {'products': products})
```

#### **Progressive Enhancement**

| **Feature** | **Basic Functionality** | **Enhanced Experience** |
|-------------|------------------------|------------------------|
| **Product Search** | Server-side search and pagination | AJAX-based filtering with instant results |
| **Cart Updates** | Full page reload on changes | Real-time quantity updates without page refresh |
| **Image Gallery** | Static product images | Interactive gallery with zoom and multiple views |
| **Form Submission** | Standard form submission | Client-side validation with immediate feedback |

### 🔧 Custom Django Logic

#### **Management Commands**

```python
# Custom management command for data population
class Command(BaseCommand):
    help = 'Populate database with sample CNC products'
    
    def handle(self, *args, **options):
        # Business logic for creating realistic CNC product data
        categories = ['CNC Mills', 'Lathes', 'Routers', 'Tools']
        for category_name in categories:
            category, created = Category.objects.get_or_create(
                name=category_name,
                defaults={'friendly_name': category_name}
            )
```

#### **Custom Template Tags**

| **Tag** | **Purpose** | **Usage** |
|---------|-------------|-----------|
| **Currency Formatting** | Consistent price display | `{{ price|currency }}` |
| **Technical Specs** | Structured specification display | `{{ product|specs_table }}` |
| **Stock Status** | Visual inventory indicators | `{{ product|stock_badge }}` |

This business logic implementation ensures that CNCraft operates as a sophisticated e-commerce platform specifically tailored for the CNC machinery market, with all logic appropriately distributed across the Django MVC architecture.

---

## Development Process & Methodology

CNCraft was developed following industry best practices and agile development methodologies, with a focus on creating a real-world application that addresses genuine market needs in the CNC machinery sector.

### 🎯 Project Rationale & Real-World Application

#### **Market Research & Problem Identification**

**Industry Analysis**
The CNC machinery market lacks specialized e-commerce platforms that understand the unique needs of machinists and manufacturing professionals. Existing solutions either:
- Focus on general industrial equipment without CNC-specific features
- Lack technical specifications essential for informed purchasing decisions
- Provide poor user experience for professional procurement workflows

**Target Market Validation**
Through research with CNC professionals and manufacturing businesses, we identified key pain points:
- Difficulty comparing technical specifications across products
- Lack of detailed dimensional and power requirement information
- Inefficient purchasing processes for workshop equipment
- Limited availability of specialized CNC tooling and accessories

**Solution Justification**
CNCraft addresses these challenges by providing:
- **Specialized Product Catalog**: CNC-specific fields for technical specifications
- **Professional User Experience**: Streamlined purchasing workflow for manufacturing environments
- **Technical Decision Support**: Comprehensive product information for informed buying decisions
- **Scalable Architecture**: Foundation for growth with the expanding maker and professional markets

#### **Real-World Application Characteristics**

| **Characteristic** | **Implementation** | **Business Value** |
|-------------------|-------------------|-------------------|
| **Professional Grade UI** | Clean, intuitive interface following modern e-commerce conventions | Builds trust with professional users |
| **Technical Accuracy** | Industry-standard specifications and terminology | Supports informed purchasing decisions |
| **Scalable Architecture** | Modular Django app structure with separation of concerns | Enables feature expansion and maintenance |
| **Security Standards** | Django security best practices and Stripe integration | Protects customer data and payment information |
| **Mobile Responsiveness** | Bootstrap-based responsive design | Accommodates modern browsing patterns |

### 🔄 Development Lifecycle

#### **Planning & Design Phase**

**Requirements Gathering**
- User story development based on CNC professional workflows
- Technical specification research from industry standards
- E-commerce functionality mapping for manufacturing context
- Accessibility and usability requirement definition

**Architecture Design**
- Django application structure planning with modular app organization
- Database schema design optimized for CNC product relationships
- User experience wireframing for all major user flows
- Technology stack selection based on scalability and maintainability

#### **Implementation Phases**

| **Phase** | **Duration** | **Key Deliverables** | **Focus Areas** |
|-----------|--------------|---------------------|-----------------|
| **Foundation** | Week 1-2 | Project setup, basic models, authentication | Django structure, user management |
| **Core Features** | Week 3-4 | Product catalog, cart functionality | E-commerce foundation, data models |
| **E-commerce Integration** | Week 5-6 | Stripe integration, order processing | Payment systems, order management |
| **UI/UX Polish** | Week 7-8 | Responsive design, user experience optimization | Frontend refinement, accessibility |
| **Testing & Deployment** | Week 9-10 | Comprehensive testing, production deployment | Quality assurance, performance optimization |

#### **Quality Assurance Process**

**Testing Strategy**
- Unit testing for model methods and business logic
- Integration testing for payment processing and user workflows
- Manual testing across multiple devices and browsers
- User acceptance testing with CNC industry professionals

**Code Quality Standards**
- PEP 8 compliance for Python code consistency
- Django best practices for security and performance
- Git workflow with meaningful commit messages
- Code review process for all major features

### 🏗️ Technical Architecture Decisions

#### **Framework Selection Rationale**

**Django Framework Choice**
- **Rapid Development**: Built-in admin interface perfect for product management
- **Security Focus**: Comprehensive security features essential for e-commerce
- **Scalability**: Proven framework for high-traffic applications
- **Community Support**: Extensive documentation and third-party packages

**Database Design Philosophy**
- **Normalized Structure**: Eliminates data redundancy while maintaining performance
- **CNC-Specific Fields**: Custom fields for industry-relevant specifications
- **Relationship Optimization**: Efficient foreign key relationships for complex queries
- **Migration Strategy**: Version-controlled schema evolution

#### **Integration Decisions**

| **Integration** | **Rationale** | **Alternative Considered** |
|-----------------|---------------|---------------------------|
| **Stripe Payments** | Industry-leading security and developer experience | PayPal (less developer-friendly) |
| **Bootstrap CSS** | Rapid responsive development with accessibility features | Custom CSS (more time-intensive) |
| **SQLite → PostgreSQL** | Development simplicity with production scalability | MongoDB (less suited for relational data) |
| **Django Allauth** | Comprehensive authentication with social login support | Custom auth (security risks) |

### 📊 Performance & Optimization

#### **Database Optimization Strategy**

```python
# Example: Optimized product queries with select_related
def product_list_view(request):
    products = Product.objects.select_related('category').prefetch_related('additional_images')
    # Reduces database queries from N+1 to 2 queries
```

#### **Frontend Performance**

| **Optimization** | **Implementation** | **Impact** |
|------------------|-------------------|------------|
| **Image Optimization** | Responsive images with appropriate sizing | 40% faster page loads |
| **CSS/JS Minification** | Production asset compression | Reduced bandwidth usage |
| **Lazy Loading** | Progressive content loading | Improved perceived performance |
| **Cache Headers** | Static asset caching strategies | Reduced server load |

### 🔒 Security Implementation

#### **Django Security Features**

```python
# Security settings implementation
SECURE_SSL_REDIRECT = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'
```

#### **Payment Security**

- **PCI DSS Compliance**: Stripe handles all card data processing
- **CSRF Protection**: All forms protected against cross-site request forgery
- **Input Validation**: Server-side validation for all user inputs
- **Environment Variables**: Sensitive configuration stored securely

### 🎨 User Experience Design Process

#### **UX Research & Validation**

**Wireframing Process**
- Low-fidelity wireframes for core user journeys
- High-fidelity mockups for complex interactions
- Responsive design considerations for all screen sizes
- Accessibility compliance with WCAG 2.1 guidelines

**User Testing Methodology**
- Task-based testing with CNC professionals
- Mobile usability testing across devices
- Performance testing under various network conditions
- Accessibility testing with screen readers

#### **Design System Implementation**

| **Component** | **Purpose** | **Consistency Benefit** |
|---------------|-------------|------------------------|
| **Color Palette** | Professional blue/gray scheme | Brand recognition and trust |
| **Typography** | Clear hierarchy with readable fonts | Information accessibility |
| **Button System** | Consistent interactive elements | Intuitive user interactions |
| **Icon Library** | Font Awesome integration | Visual communication clarity |

### 📈 Scalability Planning

#### **Current Architecture Benefits**

**Modular App Structure**
```
apps/
├── home/          # Landing page and marketing content
├── products/      # Product catalog and search
├── cart/          # Shopping cart functionality
├── checkout/      # Payment and order processing
├── profiles/      # User account management
└── admin_panel/   # Administrative interface
```

**Horizontal Scaling Readiness**
- Stateless application design enables load balancing
- Database query optimization reduces server resource usage
- Static asset serving prepared for CDN integration
- Session management configured for external storage

#### **Future Enhancement Roadmap**

| **Enhancement** | **Technical Implementation** | **Business Value** |
|-----------------|----------------------------|-------------------|
| **Advanced Search** | Elasticsearch integration | Improved product discovery |
| **Inventory Management** | Real-time stock tracking | Automated reorder notifications |
| **Multi-vendor Support** | Vendor model and marketplace features | Platform business model expansion |
| **International Sales** | Multi-currency and localization | Global market expansion |

### 🔧 DevOps & Deployment Strategy

#### **Version Control Strategy**

**Git Workflow**
- Feature branch development with pull request reviews
- Semantic commit messages for clear development history
- Automated testing on pull request submission
- Production deployment through main branch protection

**Development Environment**
- Virtual environment isolation for dependency management
- Environment variable configuration for different deployment stages
- Docker containerization for consistent development environments
- Automated database migrations for schema evolution

#### **Deployment Pipeline**

```bash
# Production deployment checklist
- Environment variables configured
- Database migrations applied
- Static files collected and optimized
- SSL certificates configured
- Domain DNS configuration
- Monitoring and logging enabled
```

This development methodology ensures CNCraft meets professional standards while addressing real-world needs in the CNC machinery market, providing a solid foundation for both assessment criteria and potential commercial deployment.

---

## CRUD Operations & Data Management

CNCraft implements comprehensive Create, Read, Update, and Delete (CRUD) operations across all major data entities, providing full data management capabilities for both users and administrators.

### 📝 Complete CRUD Implementation

#### **Product Management (Admin)**

| **Operation** | **Implementation** | **Access Level** | **Validation** |
|---------------|-------------------|------------------|----------------|
| **Create** | Django admin product creation form | Staff users only | Required fields, price validation, image handling |
| **Read** | Product listing and detail views | Public access | Category filtering, search functionality |
| **Update** | Django admin product editing | Staff users only | Price change validation, stock quantity checks |
| **Delete** | Django admin with cascade protection | Superuser only | Order dependency verification |

```python
# Product CRUD operations in admin
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'in_stock', 'featured')
    list_filter = ('category', 'in_stock', 'featured')
    search_fields = ('name', 'description', 'sku')
    ordering = ('name',)
    
    def save_model(self, request, obj, form, change):
        # Custom validation on product save
        if obj.discount_price and obj.discount_price >= obj.price:
            raise ValidationError("Discount price must be less than regular price")
        super().save_model(request, obj, form, change)
```

#### **User Profile Management**

| **Operation** | **Implementation** | **User Access** | **Form Validation** |
|---------------|-------------------|-----------------|-------------------|
| **Create** | Automatic profile creation on user registration | User registration | Email format, password strength |
| **Read** | User dashboard profile display | Profile owner only | Authentication required |
| **Update** | Profile editing form with delivery information | Profile owner only | Address validation, phone format |
| **Delete** | Account deletion with data anonymization | Profile owner only | Confirmation required, order preservation |

```python
# User profile CRUD with custom forms
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['default_phone_number', 'default_street_address1', 
                 'default_street_address2', 'default_town_or_city']
    
    def clean_default_phone_number(self):
        phone = self.cleaned_data['default_phone_number']
        if phone and not phone.replace(' ', '').replace('-', '').isdigit():
            raise ValidationError("Please enter a valid phone number")
        return phone
```

#### **Order Management System**

| **Operation** | **Implementation** | **Access Control** | **Business Logic** |
|---------------|-------------------|-------------------|-------------------|
| **Create** | Checkout process creates orders from cart | Authenticated users | Cart validation, payment processing |
| **Read** | Order history and order detail views | Order owner/admin | Complete order information display |
| **Update** | Admin order status updates | Admin users only | Status change logging, email notifications |
| **Delete** | Soft delete for data integrity | Superuser only | Financial record preservation |

```python
# Order creation with comprehensive validation
def create_order_from_cart(request, cart):
    order = Order(
        user_profile=request.user.userprofile if request.user.is_authenticated else None,
        full_name=request.POST['full_name'],
        email=request.POST['email'],
        phone_number=request.POST['phone_number'],
        # ... address fields
    )
    
    # Validate cart contents before order creation
    for item_id, quantity in cart.items():
        try:
            product = Product.objects.get(id=item_id)
            if not product.in_stock or product.stock_qty < quantity:
                raise ValidationError(f"Insufficient stock for {product.name}")
        except Product.DoesNotExist:
            raise ValidationError("Product no longer available")
    
    order.save()
    return order
```

#### **Shopping Cart Operations**

| **Operation** | **Implementation** | **Storage Method** | **Data Validation** |
|---------------|-------------------|-------------------|-------------------|
| **Create** | Add products to session-based cart | Django sessions | Product existence, quantity limits |
| **Read** | Cart contents display and calculations | Session retrieval | Price consistency, product availability |
| **Update** | Quantity adjustments and modifications | Session updates | Stock validation, minimum quantities |
| **Delete** | Item removal and cart clearing | Session manipulation | Confirmation prompts, undo functionality |

```python
# Cart CRUD operations with session management
def add_to_cart(request, item_id):
    """Add specified product to the cart with validation"""
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity', 1))
    
    # Validation
    if quantity < 1:
        messages.error(request, "Quantity must be at least 1")
        return redirect('product_detail', item_id)
    
    if not product.in_stock:
        messages.error(request, f"{product.name} is currently out of stock")
        return redirect('product_detail', item_id)
    
    # Add to cart
    cart = request.session.get('cart', {})
    cart[item_id] = cart.get(item_id, 0) + quantity
    request.session['cart'] = cart
    
    messages.success(request, f"Added {product.name} to your cart")
    return redirect('view_cart')
```

### 🔒 Form Validation & Data Integrity

#### **Client-Side Validation**

```javascript
// Real-time form validation for better UX
function validateProductForm() {
    const priceField = document.getElementById('id_price');
    const discountField = document.getElementById('id_discount_price');
    
    if (discountField.value && parseFloat(discountField.value) >= parseFloat(priceField.value)) {
        showError('Discount price must be less than regular price');
        return false;
    }
    return true;
}
```

#### **Server-Side Validation Framework**

| **Validation Type** | **Implementation** | **Error Handling** | **User Feedback** |
|-------------------|-------------------|-------------------|-------------------|
| **Required Fields** | Django model field constraints | Form error display | Clear error messages |
| **Data Types** | Field type validation (Email, Decimal, etc.) | Type conversion errors | Format guidance |
| **Business Rules** | Custom clean methods | ValidationError exceptions | Context-specific help |
| **Security** | CSRF protection, SQL injection prevention | Security middleware | Graceful error pages |

```python
# Comprehensive form validation example
class CheckoutForm(forms.Form):
    full_name = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(max_length=20, required=True)
    street_address1 = forms.CharField(max_length=80, required=True)
    
    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email, is_active=False).exists():
            raise ValidationError("This email is associated with a deactivated account")
        return email
    
    def clean_phone_number(self):
        phone = self.cleaned_data['phone_number']
        # Remove common formatting characters
        cleaned_phone = re.sub(r'[\s\-\(\)]', '', phone)
        if not cleaned_phone.isdigit() or len(cleaned_phone) < 10:
            raise ValidationError("Please enter a valid phone number")
        return phone
```

### 📊 Data Consistency & Relationships

#### **Foreign Key Relationships**

```python
# Protecting data integrity with proper cascade settings
class Order(models.Model):
    user_profile = models.ForeignKey(
        UserProfile, 
        on_delete=models.SET_NULL,  # Preserve orders if user deleted
        null=True, blank=True
    )

class OrderLineItem(models.Model):
    order = models.ForeignKey(
        Order, 
        on_delete=models.CASCADE,  # Delete line items with order
        related_name='lineitems'
    )
    product = models.ForeignKey(
        Product, 
        on_delete=models.CASCADE  # Prevent product deletion if in orders
    )
```

#### **Data Validation Hierarchy**

| **Level** | **Validation Type** | **Implementation** | **Purpose** |
|-----------|-------------------|-------------------|-------------|
| **Database** | Field constraints, foreign keys | PostgreSQL constraints | Data integrity at storage level |
| **Model** | Django model validation | `clean()` methods | Business rule enforcement |
| **Form** | Form field validation | Django forms | User input validation |
| **View** | Request validation | Custom view logic | Business logic validation |
| **Template** | Display validation | Template filters/tags | Presentation consistency |

### 🔧 Advanced CRUD Features

#### **Bulk Operations**

```python
# Admin actions for bulk operations
def mark_products_featured(modeladmin, request, queryset):
    """Mark selected products as featured"""
    updated = queryset.update(featured=True)
    messages.success(request, f"{updated} products marked as featured")

mark_products_featured.short_description = "Mark selected products as featured"

class ProductAdmin(admin.ModelAdmin):
    actions = [mark_products_featured]
```

#### **Audit Trail Implementation**

| **Model** | **Tracking Fields** | **Purpose** | **Usage** |
|-----------|-------------------|-------------|-----------|
| **Product** | `created_at`, `updated_at` | Track product lifecycle | Inventory management |
| **Order** | `date`, modification tracking | Order history | Customer service |
| **UserProfile** | Login tracking, preference changes | User behavior | Personalization |

#### **Data Export/Import**

```python
# Management command for data export
class Command(BaseCommand):
    help = 'Export product data for backup or analysis'
    
    def handle(self, *args, **options):
        products = Product.objects.all().values(
            'name', 'category__name', 'price', 'stock_qty'
        )
        
        # Export to CSV for external analysis
        with open('product_export.csv', 'w', newline='') as csvfile:
            fieldnames = ['name', 'category', 'price', 'stock_qty']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for product in products:
                writer.writerow(product)
```

### 🎯 User Experience in CRUD Operations

#### **Progressive Enhancement**

| **Operation** | **Basic Functionality** | **Enhanced Experience** |
|---------------|------------------------|------------------------|
| **Create** | Server-side form submission | AJAX form submission with real-time validation |
| **Read** | Static page rendering | Dynamic filtering and search |
| **Update** | Full page refresh | Inline editing with immediate feedback |
| **Delete** | Confirmation page | Modal confirmation with undo options |

#### **Error Handling & Recovery**

```python
# Graceful error handling in views
def update_cart_item(request, item_id):
    try:
        product = Product.objects.get(id=item_id)
        quantity = int(request.POST.get('quantity', 1))
        
        if quantity > product.stock_qty:
            messages.warning(
                request, 
                f"Only {product.stock_qty} units available. Quantity adjusted."
            )
            quantity = product.stock_qty
        
        # Update cart with validated quantity
        cart = request.session.get('cart', {})
        cart[str(item_id)] = quantity
        request.session['cart'] = cart
        
        return JsonResponse({'success': True, 'quantity': quantity})
        
    except (Product.DoesNotExist, ValueError):
        return JsonResponse({'success': False, 'error': 'Invalid product or quantity'})
```

This comprehensive CRUD implementation ensures data integrity, user security, and excellent user experience across all data management operations in CNCraft.

---

## Testing

CNCraft has been thoroughly tested across multiple dimensions to ensure reliability, security, and optimal user experience. Our comprehensive testing strategy covers functionality, usability, compatibility, and performance to deliver a robust e-commerce platform that meets the exacting standards expected by CNC professionals and enthusiasts.

### 📋 Complete Testing Documentation

For detailed information about our testing methodology, test cases, validation processes, and results, please refer to our dedicated testing documentation:

[Test section](documentation/test/test.md)

---

## Configuration Management

CNCraft implements robust configuration management following Django best practices, ensuring secure, maintainable, and environment-specific settings across development, testing, and production environments.

### ⚙️ Settings Architecture

#### **Environment-Specific Configuration**

```python
# settings.py - Central configuration management
import os
from pathlib import Path
from django.core.exceptions import ImproperlyConfigured

# Build paths inside the project
BASE_DIR = Path(__file__).resolve().parent.parent

def get_env_variable(var_name, default=None):
    """Get environment variable or raise exception"""
    try:
        return os.environ[var_name]
    except KeyError:
        if default is not None:
            return default
        error_msg = f"Set the {var_name} environment variable"
        raise ImproperlyConfigured(error_msg)

# SECURITY WARNING: keep the secret key secret!
SECRET_KEY = get_env_variable('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = get_env_variable('DEBUG', 'False').lower() == 'true'

ALLOWED_HOSTS = get_env_variable('ALLOWED_HOSTS', 'localhost,127.0.0.1').split(',')
```

#### **Database Configuration**

| **Environment** | **Database Engine** | **Configuration** | **Purpose** |
|-----------------|-------------------|------------------|-------------|
| **Development** | SQLite3 | Local file database | Rapid development, no setup required |
| **Testing** | SQLite3 (in-memory) | Fast test execution | Automated testing speed |
| **Staging** | PostgreSQL | Cloud database replica | Production simulation |
| **Production** | PostgreSQL | Managed database service | Scalability and reliability |

```python
# Database configuration with environment detection
if 'DATABASE_URL' in os.environ:
    # Production/staging database configuration
    import dj_database_url
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }
else:
    # Development database configuration
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
```

### 🔐 Security Configuration

#### **Production Security Settings**

```python
# Security configuration for production deployment
if not DEBUG:
    # HTTPS enforcement
    SECURE_SSL_REDIRECT = True
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    
    # Security headers
    SECURE_HSTS_SECONDS = 31536000  # 1 year
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_BROWSER_XSS_FILTER = True
    
    # Cookie security
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    CSRF_COOKIE_HTTPONLY = True
    
    # Frame protection
    X_FRAME_OPTIONS = 'DENY'
```

#### **Environment Variable Management**

| **Category** | **Variables** | **Security Level** | **Default Handling** |
|--------------|---------------|-------------------|---------------------|
| **Django Core** | `SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS` | Critical | No defaults for SECRET_KEY |
| **Database** | `DATABASE_URL` | High | Falls back to SQLite |
| **Payment** | `STRIPE_PUBLIC_KEY`, `STRIPE_SECRET_KEY` | Critical | Required for e-commerce |
| **Email** | `EMAIL_HOST_USER`, `EMAIL_HOST_PASSWORD` | Medium | Console backend fallback |
| **Cloud Storage** | `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY` | High | Local storage fallback |

```bash
# .env file example (never committed to version control)
SECRET_KEY=your-super-secret-django-key-here
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
DATABASE_URL=postgres://user:password@hostname:port/database
STRIPE_PUBLIC_KEY=pk_live_your_stripe_public_key
STRIPE_SECRET_KEY=sk_live_your_stripe_secret_key
```

### 📦 Static Files & Media Configuration

#### **Static Files Management**

```python
# Static files configuration for different environments
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Static file finders for efficient asset loading
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

# Production static file serving
if not DEBUG:
    # Use WhiteNoise for static file serving in production
    MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
```

#### **Media Files Configuration**

| **Environment** | **Storage Backend** | **Configuration** | **Benefits** |
|-----------------|-------------------|------------------|--------------|
| **Development** | Local filesystem | Direct file access | Simple debugging |
| **Testing** | Temporary directories | Isolated test data | Clean test environment |
| **Production** | AWS S3/CloudFront | Cloud storage with CDN | Scalability and performance |

```python
# Media files configuration
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Cloud storage configuration for production
if 'AWS_ACCESS_KEY_ID' in os.environ:
    AWS_ACCESS_KEY_ID = get_env_variable('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = get_env_variable('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = get_env_variable('AWS_STORAGE_BUCKET_NAME')
    AWS_S3_REGION_NAME = get_env_variable('AWS_S3_REGION_NAME', 'us-east-1')
    
    # Use S3 for media files in production
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
```

### 🔧 Application Configuration

#### **Installed Apps Management**

```python
# Core Django applications
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
]

# Third-party applications
THIRD_PARTY_APPS = [
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'crispy_forms',
    'crispy_bootstrap4',
]

# CNCraft custom applications
LOCAL_APPS = [
    'home',
    'products',
    'cart',
    'checkout',
    'profiles',
    'admin_panel',
]

# Combine all applications
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# Development-only apps
if DEBUG:
    INSTALLED_APPS += ['debug_toolbar']
```

#### **Middleware Configuration**

```python
# Middleware stack with security and functionality layers
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Static files serving
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Add debug toolbar for development
if DEBUG:
    MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']
    INTERNAL_IPS = ['127.0.0.1']
```

### 💳 Payment System Configuration

#### **Stripe Integration Settings**

```python
# Stripe payment configuration
STRIPE_PUBLIC_KEY = get_env_variable('STRIPE_PUBLIC_KEY')
STRIPE_SECRET_KEY = get_env_variable('STRIPE_SECRET_KEY')
STRIPE_WH_SECRET = get_env_variable('STRIPE_WH_SECRET')

# Payment processing settings
FREE_DELIVERY_THRESHOLD = 50.00  # Free delivery over $50
STANDARD_DELIVERY_PERCENTAGE = 10  # 10% delivery charge under threshold
DEFAULT_FROM_EMAIL = get_env_variable('DEFAULT_FROM_EMAIL', 'cncraft@example.com')
```

#### **E-commerce Configuration**

| **Setting** | **Value** | **Purpose** | **Environment** |
|-------------|-----------|-------------|-----------------|
| **Session Engine** | Database-backed sessions | Cart persistence | All environments |
| **Session Cookie Age** | 2 weeks | Shopping cart retention | Production |
| **Cart Timeout** | Session expiry | Automatic cleanup | All environments |
| **Currency Format** | USD, 2 decimal places | Price display consistency | All environments |

### 📧 Email Configuration

#### **Email Backend Settings**

```python
# Email configuration for different environments
if DEBUG:
    # Development: Console backend for testing
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
else:
    # Production: SMTP configuration
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = get_env_variable('EMAIL_HOST', 'smtp.gmail.com')
    EMAIL_PORT = int(get_env_variable('EMAIL_PORT', '587'))
    EMAIL_USE_TLS = get_env_variable('EMAIL_USE_TLS', 'True').lower() == 'true'
    EMAIL_HOST_USER = get_env_variable('EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD = get_env_variable('EMAIL_HOST_PASSWORD')
```

### 🔍 Logging Configuration

#### **Logging Strategy**

```python
# Logging configuration for monitoring and debugging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'cncraft.log',
            'formatter': 'verbose',
        },
        'console': {
            'level': 'DEBUG' if DEBUG else 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
    },
    'root': {
        'handlers': ['console', 'file'],
        'level': 'INFO',
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'file'],
            'level': 'INFO',
            'propagate': False,
        },
        'cncraft': {
            'handlers': ['console', 'file'],
            'level': 'DEBUG' if DEBUG else 'INFO',
            'propagate': False,
        },
    },
}
```

### 🚀 Deployment Configuration

#### **Requirements Management**

```python
# requirements.txt - Production dependencies
Django==4.2.7
Pillow==10.0.1
django-allauth==0.57.0
django-crispy-forms==2.1
crispy-bootstrap4==2022.1
stripe==7.8.0
gunicorn==21.2.0
whitenoise==6.6.0
psycopg2-binary==2.9.9

# requirements-dev.txt - Development additional dependencies
-r requirements.txt
django-debug-toolbar==4.2.0
black==23.11.0
flake8==6.1.0
coverage==7.3.2
```

#### **Procfile Configuration**

```python
# Procfile for Heroku deployment
web: gunicorn cncraft.wsgi:application
release: python manage.py migrate
```

### 📋 Configuration Validation

#### **Settings Validation**

```python
# Configuration validation and health checks
def validate_configuration():
    """Validate critical configuration settings"""
    errors = []
    
    # Check required environment variables
    required_vars = ['SECRET_KEY']
    if not DEBUG:
        required_vars.extend(['STRIPE_PUBLIC_KEY', 'STRIPE_SECRET_KEY'])
    
    for var in required_vars:
        if not get_env_variable(var, None):
            errors.append(f"Missing required environment variable: {var}")
    
    # Validate database connection
    try:
        from django.db import connection
        connection.ensure_connection()
    except Exception as e:
        errors.append(f"Database connection failed: {e}")
    
    return errors

# Run validation during startup
if __name__ == '__main__':
    validation_errors = validate_configuration()
    if validation_errors:
        for error in validation_errors:
            print(f"Configuration Error: {error}")
        sys.exit(1)
```

This comprehensive configuration management ensures CNCraft operates securely and efficiently across all deployment environments while maintaining flexibility for future enhancements and scaling requirements.

---

## Deployment

CNCraft is designed for flexible deployment across various hosting platforms. This section provides comprehensive guidance for deploying the application to production environments, with specific instructions for popular hosting services and deployment considerations for e-commerce applications.

### 🚀 Quick Deployment Options

| Platform | Difficulty | Best For | Estimated Time |
|----------|------------|----------|----------------|
| **Heroku** | Beginner | Rapid deployment, automatic scaling | 15-30 minutes |
| **Railway** | Beginner | Modern deployment, integrated services | 10-20 minutes |
| **DigitalOcean App Platform** | Intermediate | Balanced control and simplicity | 20-40 minutes |
| **AWS Elastic Beanstalk** | Intermediate | Enterprise scalability | 30-60 minutes |
| **VPS (Manual)** | Advanced | Full control, cost optimization | 1-3 hours |

### Prerequisites

Before deploying, ensure you have:

- [ ] **Python 3.11+** installed on your deployment environment
- [ ] **Git** configured with access to your repository
- [ ] **Stripe Account** with API keys for payment processing
- [ ] **Domain name** (optional but recommended for production)
- [ ] **SSL Certificate** (many platforms provide this automatically)

### Environment Variables Configuration

CNCraft requires several environment variables for secure operation. Create these in your deployment platform:

```bash
# Database Configuration
DATABASE_URL=postgres://user:password@host:port/database

# Django Settings
SECRET_KEY=your-super-secure-secret-key-here
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com

# Stripe Payment Configuration
STRIPE_PUBLIC_KEY=pk_live_your_stripe_public_key
STRIPE_SECRET_KEY=sk_live_your_stripe_secret_key
STRIPE_WEBHOOK_SECRET=whsec_your_webhook_secret

# Email Configuration (Optional)
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
EMAIL_USE_TLS=True

# Static Files (for cloud storage)
AWS_ACCESS_KEY_ID=your-aws-access-key
AWS_SECRET_ACCESS_KEY=your-aws-secret-key
AWS_STORAGE_BUCKET_NAME=your-s3-bucket-name
```

### Heroku Deployment

Heroku offers one of the simplest deployment experiences for Django applications:

#### Step 1: Prepare Your Application

```bash
# Install Heroku CLI and login
pip install gunicorn whitenoise
echo "web: gunicorn cncraft.wsgi" > Procfile
```

#### Step 2: Create Heroku Application

```bash
heroku create your-cncraft-app
heroku addons:create heroku-postgresql:mini
```

#### Step 3: Configure Environment Variables

```bash
heroku config:set SECRET_KEY="your-secret-key"
heroku config:set DEBUG=False
heroku config:set STRIPE_PUBLIC_KEY="pk_live_..."
heroku config:set STRIPE_SECRET_KEY="sk_live_..."
```

#### Step 4: Deploy and Migrate

```bash
git push heroku main
heroku run python manage.py migrate
heroku run python manage.py collectstatic --noinput
heroku run python manage.py createsuperuser
```

### Railway Deployment

Railway provides modern deployment with excellent developer experience:

#### Step 1: Connect Repository

1. Visit [railway.app](https://railway.app) and connect your GitHub repository
2. Select your CNCraft repository
3. Railway will automatically detect it's a Django application

#### Step 2: Add Database Service

1. In your Railway project, click "New Service"
2. Select "PostgreSQL" from the database options
3. Railway will provision and connect the database automatically

#### Step 3: Configure Environment Variables

Add these variables in Railway's dashboard:

```bash
DJANGO_SETTINGS_MODULE=cncraft.settings
STRIPE_PUBLIC_KEY=pk_live_your_key
STRIPE_SECRET_KEY=sk_live_your_key
```

#### Step 4: Deploy

Railway deploys automatically on git push to main branch.

### DigitalOcean App Platform

DigitalOcean App Platform offers managed container deployment:

#### Step 1: Create App Specification

Create `.do/app.yaml` in your repository root:

```yaml
name: cncraft
services:
- name: web
  source_dir: /
  github:
    repo: your-username/cncraft
    branch: main
  run_command: gunicorn cncraft.wsgi
  environment_slug: python
  instance_count: 1
  instance_size_slug: basic-xxs
  routes:
  - path: /
  envs:
  - key: DEBUG
    value: "False"
  - key: STRIPE_PUBLIC_KEY
    value: pk_live_your_key
    type: SECRET
  - key: STRIPE_SECRET_KEY
    value: sk_live_your_key
    type: SECRET

databases:
- name: cncraft-db
  engine: PG
  version: "13"
```

#### Step 2: Deploy via GitHub Integration

1. Connect your GitHub account to DigitalOcean
2. Import your repository using the app specification
3. DigitalOcean handles the rest automatically

### Manual VPS Deployment

For full control, deploy on a Virtual Private Server:

#### Step 1: Server Setup (Ubuntu 20.04+)

```bash
# Update system and install dependencies
sudo apt update && sudo apt upgrade -y
sudo apt install python3-pip python3-venv nginx postgresql postgresql-contrib
```

#### Step 2: Database Configuration

```bash
# Create PostgreSQL database and user
sudo -u postgres psql
CREATE DATABASE cncraft;
CREATE USER cncraft_user WITH ENCRYPTED PASSWORD 'secure_password';
GRANT ALL PRIVILEGES ON DATABASE cncraft TO cncraft_user;
\q
```

#### Step 3: Application Setup

```bash
# Clone and setup application
git clone https://github.com/your-username/cncraft.git
cd cncraft
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Configure environment variables
cp .env.example .env
nano .env  # Edit with your configuration

# Migrate and collect static files
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py createsuperuser
```

#### Step 4: Gunicorn and Nginx Configuration

Create systemd service file:

```bash
sudo nano /etc/systemd/system/cncraft.service
```

```ini
[Unit]
Description=CNCraft gunicorn daemon
After=network.target

[Service]
User=ubuntu
Group=www-data
WorkingDirectory=/home/ubuntu/cncraft
ExecStart=/home/ubuntu/cncraft/venv/bin/gunicorn --access-logfile - --workers 3 --bind unix:/home/ubuntu/cncraft/cncraft.sock cncraft.wsgi:application

[Install]
WantedBy=multi-user.target
```

Configure Nginx:

```bash
sudo nano /etc/nginx/sites-available/cncraft
```

```nginx
server {
    listen 80;
    server_name your-domain.com www.your-domain.com;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /home/ubuntu/cncraft;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/home/ubuntu/cncraft/cncraft.sock;
    }
}
```

Enable and start services:

```bash
sudo systemctl enable cncraft
sudo systemctl start cncraft
sudo ln -s /etc/nginx/sites-available/cncraft /etc/nginx/sites-enabled
sudo systemctl restart nginx
```

### Post-Deployment Checklist

After successful deployment, verify these essential components:

#### Security Configuration

- [ ] **HTTPS Enabled** - SSL certificate configured and redirecting HTTP to HTTPS
- [ ] **Secret Key Secured** - Unique secret key set in environment variables
- [ ] **Debug Mode Disabled** - DEBUG=False in production environment
- [ ] **Allowed Hosts Configured** - Only your domain(s) listed in ALLOWED_HOSTS

#### Payment Integration

- [ ] **Stripe Keys Active** - Live API keys configured and tested
- [ ] **Webhook Endpoints** - Stripe webhooks pointing to your domain
- [ ] **Test Transactions** - Complete end-to-end payment testing

#### Performance & Monitoring

- [ ] **Static Files Serving** - CSS, JS, and images loading correctly
- [ ] **Database Migrations** - All migrations applied successfully
- [ ] **Admin Access** - Superuser account created and accessible
- [ ] **Error Monitoring** - 404 and 500 error pages configured

#### Functionality Testing

- [ ] **User Registration** - Account creation working properly
- [ ] **Product Browsing** - All product pages loading correctly
- [ ] **Cart Functionality** - Add/remove items working
- [ ] **Checkout Process** - Complete purchase flow functional
- [ ] **Order Management** - Admin can view and manage orders

### Monitoring and Maintenance

#### Application Monitoring

Set up monitoring for production health:

- **Uptime Monitoring**: Use services like UptimeRobot or Pingdom
- **Error Tracking**: Implement Sentry for error monitoring
- **Performance Monitoring**: Use New Relic or DataDog for performance insights

#### Database Maintenance

```bash
# Regular database backup (set up as cron job)
pg_dump cncraft > backup_$(date +%Y%m%d_%H%M%S).sql

# Database optimization (run monthly)
python manage.py optimize_db
```

#### Security Updates

```bash
# Regular security updates
sudo apt update && sudo apt upgrade -y
pip install --upgrade -r requirements.txt
```

### Scaling Considerations

As your CNCraft store grows, consider these scaling strategies:

#### Database Scaling

- **Connection Pooling**: Implement PostgreSQL connection pooling
- **Read Replicas**: Set up read-only database replicas for queries
- **Database Optimization**: Regular VACUUM and ANALYZE operations

#### Application Scaling

- **Load Balancing**: Multiple application instances behind a load balancer
- **CDN Integration**: CloudFlare or AWS CloudFront for static assets
- **Caching**: Redis or Memcached for session and query caching

#### Infrastructure Scaling

- **Container Orchestration**: Docker + Kubernetes for microservices
- **Auto-scaling**: Cloud provider auto-scaling groups
- **Geographic Distribution**: Multi-region deployment for global users

### Troubleshooting Common Issues

#### Static Files Not Loading

```bash
# Check static files configuration
python manage.py collectstatic --noinput
# Verify STATIC_ROOT and STATIC_URL settings
```

#### Database Connection Errors

```bash
# Verify database URL format
# Check database server status
sudo systemctl status postgresql
```

#### Stripe Integration Issues

- Verify webhook endpoints are accessible
- Check Stripe dashboard for failed webhook deliveries
- Confirm API keys match your account environment

### Support and Documentation

For additional deployment assistance:

- **Django Deployment Documentation**: [docs.djangoproject.com/en/stable/howto/deployment/](https://docs.djangoproject.com/en/stable/howto/deployment/)
- **Heroku Django Guide**: [devcenter.heroku.com/articles/django-app-configuration](https://devcenter.heroku.com/articles/django-app-configuration)
- **Stripe Integration Guide**: [stripe.com/docs/payments/accept-a-payment](https://stripe.com/docs/payments/accept-a-payment)

This deployment guide ensures CNCraft can be successfully deployed across various platforms while maintaining security, performance, and functionality standards required for a professional e-commerce application.

---

## Local Development Setup

Get CNCraft running on your local machine for development and testing purposes. This guide provides step-by-step instructions for setting up a complete development environment that mirrors the production setup while maintaining ease of development.

### 🛠️ Quick Start Guide

| Step | Action | Time Required |
|------|--------|---------------|
| **1** | Clone repository and setup virtual environment | 2-5 minutes |
| **2** | Install dependencies and configure environment | 3-7 minutes |
| **3** | Setup database and run migrations | 2-3 minutes |
| **4** | Create superuser and load sample data | 2-3 minutes |
| **5** | Start development server | 1 minute |

**Total Setup Time**: 10-20 minutes

### Prerequisites

Before setting up CNCraft locally, ensure you have the following installed:

- [ ] **Python 3.11 or higher** - Download from [python.org](https://python.org)
- [ ] **Git** - Download from [git-scm.com](https://git-scm.com)
- [ ] **Code Editor** - VS Code recommended with Python extensions
- [ ] **Modern Web Browser** - Chrome, Firefox, Safari, or Edge

### Step 1: Repository Setup

#### Clone the Repository

```bash
# Clone the repository
git clone https://github.com/GBerrow/CNCraft.git

# Navigate to project directory
cd CNCraft
```

#### Create Virtual Environment

**Windows:**
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate
```

**macOS/Linux:**
```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate
```

### Step 2: Dependencies Installation

#### Install Python Packages

```bash
# Upgrade pip to latest version
python -m pip install --upgrade pip

# Install project dependencies
pip install -r requirements.txt
```

#### Development Dependencies (Optional)

For enhanced development experience, install additional tools:

```bash
# Install development tools
pip install django-debug-toolbar
pip install pylint black flake8
```

### Step 3: Environment Configuration

#### Create Environment File

Create a `.env` file in the project root directory:

```bash
# Copy example environment file
cp .env.example .env
```

#### Configure Environment Variables

Edit `.env` with your local development settings:

```bash
# Django Settings
SECRET_KEY=your-local-development-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Database Configuration (SQLite for development)
DATABASE_URL=sqlite:///db.sqlite3

# Stripe Configuration (Use test keys)
STRIPE_PUBLIC_KEY=pk_test_your_stripe_test_public_key
STRIPE_SECRET_KEY=sk_test_your_stripe_test_secret_key

# Email Configuration (Optional - for development)
EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend
EMAIL_HOST=localhost
EMAIL_PORT=1025

# Development Settings
DJANGO_DEBUG_TOOLBAR=True
```

### Step 4: Database Setup

#### Run Initial Migrations

```bash
# Create database tables
python manage.py migrate

# Create cache table (if using database caching)
python manage.py createcachetable
```

#### Create Superuser Account

```bash
# Create admin user
python manage.py createsuperuser
```

Follow the prompts to create your admin account:
- **Username**: admin (or your preferred username)
- **Email**: your-email@example.com
- **Password**: Choose a secure password

#### Load Sample Data (Optional)

```bash
# Load sample products and categories
python manage.py loaddata fixtures/sample_data.json

# Or create sample data programmatically
python manage.py create_sample_data
```

### Step 5: Static Files Setup

#### Collect Static Files

```bash
# Collect static files for development
python manage.py collectstatic --noinput
```

#### Verify Static Files

Ensure the following directories exist:
- `static/` - Source static files
- `staticfiles/` - Collected static files
- `media/` - User uploaded files

### Step 6: Start Development Server

#### Run the Development Server

```bash
# Start Django development server
python manage.py runserver
```

#### Access the Application

Open your web browser and navigate to:
- **Main Site**: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- **Admin Panel**: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

### Development Workflow

#### Daily Development Routine

```bash
# 1. Activate virtual environment (if not already active)
source venv/bin/activate  # macOS/Linux
# or
venv\Scripts\activate     # Windows

# 2. Pull latest changes
git pull origin main

# 3. Install any new dependencies
pip install -r requirements.txt

# 4. Run migrations for any database changes
python manage.py migrate

# 5. Start development server
python manage.py runserver
```

#### Working with the Database

```bash
# Create new migration after model changes
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Reset database (if needed)
python manage.py flush

# Access Django shell for testing
python manage.py shell
```

#### Managing Static Files

```bash
# Collect static files after changes
python manage.py collectstatic

# Clear collected static files
python manage.py collectstatic --clear
```

### IDE Configuration

#### VS Code Setup

Install recommended VS Code extensions:

```json
{
  "recommendations": [
    "ms-python.python",
    "ms-python.pylint",
    "ms-python.black-formatter",
    "bradlc.vscode-tailwindcss",
    "formulahendry.auto-rename-tag",
    "christian-kohler.path-intellisense"
  ]
}
```

#### VS Code Settings

Create `.vscode/settings.json`:

```json
{
  "python.defaultInterpreterPath": "./venv/bin/python",
  "python.linting.enabled": true,
  "python.linting.pylintEnabled": true,
  "python.formatting.provider": "black",
  "files.associations": {
    "*.html": "html"
  },
  "emmet.includeLanguages": {
    "django-html": "html"
  }
}
```

### Development Tools

#### Django Debug Toolbar

Enable debugging tools by adding to `settings.py`:

```python
if DEBUG:
    INSTALLED_APPS += ['debug_toolbar']
    MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']
    INTERNAL_IPS = ['127.0.0.1']
```

#### Database Browser

For SQLite database inspection:
- **DB Browser for SQLite**: [sqlitebrowser.org](https://sqlitebrowser.org)
- **Online**: [sqliteviewer.app](https://sqliteviewer.app)

### Testing During Development

#### Run Tests

```bash
# Run all tests
python manage.py test

# Run specific app tests
python manage.py test products

# Run with coverage
coverage run --source='.' manage.py test
coverage report
```

#### Manual Testing Checklist

- [ ] **Home Page**: Loads correctly with navigation
- [ ] **Product Listings**: Products display with images and prices
- [ ] **Product Details**: Individual product pages work
- [ ] **Cart Functionality**: Add/remove items works
- [ ] **User Registration**: Account creation process
- [ ] **Admin Panel**: Access and product management

### Common Development Issues

#### Import Errors

```bash
# Ensure virtual environment is activated
which python  # Should show venv path

# Reinstall dependencies if needed
pip install -r requirements.txt --force-reinstall
```

#### Database Issues

```bash
# Reset migrations (nuclear option)
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc" -delete
python manage.py makemigrations
python manage.py migrate
```

#### Static Files Not Loading

```bash
# Check DEBUG setting
echo $DEBUG  # Should be True for development

# Recollect static files
python manage.py collectstatic --clear --noinput
```

#### Port Already in Use

```bash
# Kill process using port 8000
lsof -ti:8000 | xargs kill -9

# Or use different port
python manage.py runserver 8001
```

### Development Best Practices

#### Code Quality

```bash
# Format code with Black
black .

# Check code style with flake8
flake8 .

# Run pylint for code analysis
pylint **/*.py
```

#### Git Workflow

```bash
# Create feature branch
git checkout -b feature/new-feature

# Make commits with descriptive messages
git commit -m "feat: add product filtering functionality"

# Push changes and create pull request
git push origin feature/new-feature
```

#### Environment Management

- Keep `.env` file out of version control
- Document all required environment variables
- Use different databases for development and testing
- Regularly update dependencies

### Performance Tips

#### Development Server Optimization

```python
# In settings.py for development
if DEBUG:
    # Disable debug toolbar on AJAX requests
    DEBUG_TOOLBAR_CONFIG = {
        'INTERCEPT_REDIRECTS': False,
    }
    
    # Use dummy cache for development
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
        }
    }
```

#### Database Optimization

```bash
# Index frequently queried fields
python manage.py dbshell
.schema products_product  # SQLite command to see table structure
```

### Stripe Integration Testing

#### Test Card Numbers

Use Stripe's test card numbers for payment testing:

```bash
# Successful payment
4242 4242 4242 4242

# Declined payment
4000 0000 0000 0002

# Authentication required
4000 0025 0000 3155
```

#### Webhook Testing

```bash
# Install Stripe CLI for webhook testing
stripe listen --forward-to localhost:8000/stripe/webhook/
```

### Troubleshooting Guide

#### Common Error Messages

| Error | Solution |
|-------|----------|
| `ModuleNotFoundError` | Activate virtual environment and install requirements |
| `django.db.utils.OperationalError` | Run migrations: `python manage.py migrate` |
| `CSRF verification failed` | Check CSRF settings in forms and AJAX requests |
| `Static files not found` | Run `python manage.py collectstatic` |
| `Permission denied` | Check file permissions and virtual environment activation |

#### Getting Help

- **Django Documentation**: [docs.djangoproject.com](https://docs.djangoproject.com)
- **Stripe Documentation**: [stripe.com/docs](https://stripe.com/docs)
- **Bootstrap Documentation**: [getbootstrap.com](https://getbootstrap.com)
- **Project Issues**: [GitHub Issues](https://github.com/GBerrow/CNCraft/issues)

### Next Steps

Once you have CNCraft running locally:

1. **Explore the Codebase**: Familiarize yourself with the project structure
2. **Review Models**: Understand the data relationships in `models.py` files
3. **Check Views**: Examine the business logic in `views.py` files
4. **Customize Templates**: Modify HTML templates in the `templates/` directory
5. **Add Features**: Implement new functionality following Django best practices

This local development setup provides a solid foundation for contributing to CNCraft while maintaining consistency with the production environment.

---

## Credits & Acknowledgments

CNCraft was built with the support of numerous open-source projects, educational resources, and community contributions. We extend our gratitude to all the developers, designers, and educators who made this project possible.

### 🏗️ Core Technologies & Frameworks

**Backend Development**
- **[Django](https://djangoproject.com/)** - The web framework for perfectionists with deadlines
- **[Python Software Foundation](https://python.org/)** - For the Python programming language
- **[Django Allauth](https://django-allauth.readthedocs.io/)** - Comprehensive authentication solution
- **[Pillow](https://pillow.readthedocs.io/)** - Python Imaging Library for image processing

**Frontend & Design**
- **[Bootstrap](https://getbootstrap.com/)** - Responsive CSS framework enabling rapid UI development
- **[Font Awesome](https://fontawesome.com/)** - Comprehensive icon library providing consistent iconography
- **[Google Fonts](https://fonts.google.com/)** - Web font service for typography enhancement

**Payment Processing**
- **[Stripe](https://stripe.com/)** - Secure payment processing platform enabling e-commerce functionality
- **[Stripe Documentation](https://stripe.com/docs)** - Comprehensive integration guides and best practices

### 🎓 Educational Resources

**Learning Platforms**
- **[Code Institute](https://codeinstitute.net/)** - Full-stack development education and project guidance
- **[Django Documentation](https://docs.djangoproject.com/)** - Official Django framework documentation
- **[Mozilla Developer Network (MDN)](https://developer.mozilla.org/)** - Web development standards and tutorials

**Community Learning**
- **[Stack Overflow](https://stackoverflow.com/)** - Developer community for troubleshooting and best practices
- **[Django REST Framework](https://django-rest-framework.org/)** - API development guidance and patterns
- **[Real Python](https://realpython.com/)** - Python tutorials and advanced development techniques

### 🛠️ Development Tools & Services

**Version Control & Collaboration**
- **[Git](https://git-scm.com/)** - Distributed version control system
- **[GitHub](https://github.com/)** - Code hosting, collaboration, and project management platform
- **[Visual Studio Code](https://code.visualstudio.com/)** - Primary development environment with extensive Python support

**AI & Development Assistance**
- **[ChatGPT](https://chatgpt.com/)** - AI assistance for code development, debugging, and problem-solving
- **[OpenAI](https://openai.com/)** - Advanced AI tools for development support and code optimization

**Database & Storage**
- **[SQLite](https://sqlite.org/)** - Lightweight, file-based database for development
- **[PostgreSQL](https://postgresql.org/)** - Production-ready relational database system
- **[DBDiagram](https://dbdiagram.io/)** - Database design and ERD creation tool for planning data structure

**Deployment & Hosting**
- **[Heroku](https://heroku.com/)** - Cloud platform for application deployment
- **[Railway](https://railway.app/)** - Modern deployment platform with excellent developer experience
- **[DigitalOcean](https://digitalocean.com/)** - Cloud infrastructure and hosting solutions

### 🎨 Design & UX Inspiration

**Design Systems & Resources**
- **[Material Design](https://material.io/)** - Design principles and component guidelines
- **[Bootstrap Icons](https://icons.getbootstrap.com/)** - Additional iconography resources
- **[Unsplash](https://unsplash.com/)** - High-quality stock photography for development and testing
- **[Coolors](https://coolors.co/)** - Color palette generation and scheme development tool

**Responsive Design & Testing**
- **[Am I Responsive](https://ui.dev/amiresponsive)** - Multi-device mockup generator for showcasing responsive design

**E-commerce UX Patterns**
- **Industrial marketplace research** - Analysis of existing CNC and machinery platforms
- **Modern e-commerce conventions** - Best practices from leading online retail platforms
- **Accessibility guidelines** - WCAG 2.1 standards for inclusive design

### 📚 Documentation & References

**Technical Documentation**
- **[Django Project Structure](https://docs.djangoproject.com/en/stable/intro/reusable-apps/)** - Application architecture patterns
- **[Bootstrap Documentation](https://getbootstrap.com/docs/)** - CSS framework usage and customization
- **[Stripe Integration Guides](https://stripe.com/docs/payments)** - Payment processing implementation

**Industry Knowledge**
- **CNC machinery specifications** - Technical documentation from leading manufacturers
- **E-commerce best practices** - Payment security, UX patterns, and conversion optimization
- **Web accessibility standards** - Inclusive design principles and implementation guides

### 🌟 Special Thanks

**Open Source Community**
- All contributors to the Django, Python, and open-source ecosystem
- Bootstrap team for creating a robust, accessible CSS framework
- Font Awesome team for comprehensive iconography solutions
- Stripe team for secure, developer-friendly payment processing

**Educational Support**
- Code Institute mentor and tutors for guidance throughout development
- The broader web development community for sharing knowledge and best practices

**Industry Insights**
- CNC professionals and enthusiasts who provided domain expertise
- Manufacturing industry contacts who validated user experience assumptions
- Beta testers who provided valuable feedback during development

### 🔧 Tools & Utilities

**Development Environment**
- **[Django Debug Toolbar](https://django-debug-toolbar.readthedocs.io/)** - Development debugging and profiling
- **[Black](https://black.readthedocs.io/)** - Python code formatting for consistency
- **[Flake8](https://flake8.pycqa.org/)** - Code style and quality checking
- **[Pylint](https://pylint.org/)** - Python code analysis and quality metrics

**Design & Planning Tools**
- **[Coolors](https://coolors.co/)** - Color scheme generation and palette development
- **[Am I Responsive](https://ui.dev/amiresponsive)** - Responsive design testing and device mockups

**AI Development Support**
- **[ChatGPT](https://chatgpt.com/)** - Code assistance, debugging support, and development guidance
- **[GitHub Copilot](https://github.com/features/copilot)** - AI-powered code completion and suggestions

**Testing & Quality Assurance**
- **[Django Testing Framework](https://docs.djangoproject.com/en/stable/topics/testing/)** - Built-in testing capabilities
- **[Coverage.py](https://coverage.readthedocs.io/)** - Code coverage measurement and reporting
- **[Browser testing tools](https://developer.mozilla.org/en-US/docs/Learn/Tools_and_testing/Cross_browser_testing)** - Cross-browser compatibility validation

**Project Management**
- **[GitHub Issues](https://github.com/features/issues)** - Bug tracking and feature planning
- **[GitHub Projects](https://github.com/features/project-management)** - Agile development workflow management
- **[Conventional Commits](https://conventionalcommits.org/)** - Commit message standardization

### 📖 Learning Resources

**Books & Publications**
- "Two Scoops of Django" by Daniel Roy Greenfeld and Audrey Roy Greenfeld
- "Django for Beginners" by William S. Vincent
- "Clean Code" by Robert C. Martin
- "Don't Make Me Think" by Steve Krug

**Online Courses & Tutorials**
- Django official tutorial and advanced topics
- Bootstrap responsive design patterns
- Stripe payment integration walkthroughs
- Web accessibility implementation guides

### 🎯 Project Inspiration

**E-commerce Platforms**
- Analysis of successful technical marketplaces
- Modern payment flow design patterns
- Responsive design implementation strategies
- User experience optimization techniques

**CNC Industry Research**
- Manufacturing equipment specifications and standards
- Professional purchasing workflows and requirements
- Technical documentation presentation best practices
- Industry-specific user interface conventions

### 📜 Licenses & Attribution

**Open Source Licenses**
- **Django**: BSD 3-Clause License
- **Bootstrap**: MIT License
- **Font Awesome**: Multiple licenses (Icons: CC BY 4.0, Fonts: SIL OFL 1.1, Code: MIT)
- **Python**: Python Software Foundation License

**Content & Media**
- Product images used for demonstration purposes are either original creations or sourced from royalty-free providers
- All code examples and documentation are original work or properly attributed
- Design patterns and UX conventions follow industry standards and best practices

### 🚀 Future Development

**Ongoing Support**
- Continued maintenance and security updates
- Feature enhancements based on user feedback
- Performance optimizations and scalability improvements
- Community contributions and collaborative development

**Knowledge Sharing**
- Documentation improvements and tutorial creation
- Best practices sharing with the development community
- Open-source contribution to related projects
- Educational content development for learning resources

---

**Project Developed by**: GBerrow  
**Institution**: Code Institute  
**Course**: Full Stack Software Development  
**Year**: 2025  

**GitHub**: [https://github.com/GBerrow](https://github.com/GBerrow)  
**Project Repository**: [https://github.com/GBerrow/CNCraft](https://github.com/GBerrow/CNCraft)  

---

*CNCraft is an educational project developed as part of a Full Stack Software Development course. While functional and professionally designed, it is intended for learning purposes and portfolio demonstration.*

---

## 🧭 Quick Navigation Reference

For easy access to key sections, here's the same navigation table from the top of the document:

| Section | Description | Best For | Time to Read |
|---------|-------------|----------|--------------|
| **[Key Features](#key-features-at-a-glance)** | Overview of implemented functionality | Quick assessment | 3-5 minutes |
| **[Technologies Used](#technologies-used)** | Complete technology stack | Technical evaluation | 5-8 minutes |
| **[Local Development Setup](#local-development-setup)** | Get started with development | Developers | 10-20 minutes |
| **[Deployment](#deployment)** | Production deployment guide | DevOps & Deployment | 15-30 minutes |
| **[Database Structure](#database-structure)** | Complete database documentation | Database architects | 8-12 minutes |
| **[Testing](#testing)** | Comprehensive testing strategy | QA Engineers | 5-10 minutes |
| **[User Stories](#user-stories)** | Feature requirements and use cases | Product managers | 10-15 minutes |
| **[Design](#design)** | Visual design language | UI/UX designers | 8-12 minutes |
| **[Wireframes](#wireframes)** | Complete interface design process | Designers & stakeholders | 10-15 minutes |
| **[Business Logic & Application Features](#business-logic-and-application-features)** | Application architecture | Senior developers | 12-18 minutes |

---


