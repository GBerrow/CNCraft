# Manual Testing Procedures

## Overview

This document outlines comprehensive manual testing procedures for CNCraft, covering user journeys, device compatibility, browser testing, and CRUD operations validation. These tests complement the automated testing suite to ensure complete application quality assurance.

## User Journey Testing Framework

### Test Scenario 1: New Customer Registration and Purchase Flow

| Step | Action | Expected Outcome | Status | Notes |
|------|--------|------------------|--------|-------|
| 1 | Navigate to homepage | Homepage loads with proper navigation and content | ⏳ | Check loading time and layout |
| 2 | Access registration form | Registration form displays with validation | ⏳ | Verify all fields present |
| 3 | Submit registration data | User account created successfully | ⏳ | Validate with proper data format |
| 4 | Browse product catalog | Product listing displays with filtering options | ⏳ | Test sorting and filtering |
| 5 | Execute product search | Search functionality returns relevant results | ⏳ | Try various search terms |
| 6 | View product details | Complete product information displayed | ⏳ | Check images, price, description |
| 7 | Add item to cart | Product added with correct quantity and pricing | ⏳ | Verify cart counter updates |
| 8 | Review cart contents | All items displayed with accurate totals | ⏳ | Check calculations |
| 9 | Modify cart quantities | Price calculations update dynamically | ⏳ | Test quantity validation |
| 10 | Proceed to checkout | Checkout form loads with customer information | ⏳ | Verify form pre-population |
| 11 | Complete order form | Form accepts valid customer data | ⏳ | Test validation errors |
| 12 | Process payment | Stripe payment integration completes successfully | ⏳ | Use test card: 4242424242424242 |
| 13 | Receive confirmation | Order confirmation page displays with order details | ⏳ | Verify order number generation |

### Test Scenario 2: Returning Customer Experience

| Step | Action | Expected Outcome | Status | Notes |
|------|--------|------------------|--------|-------|
| 1 | User authentication | Successful login with existing credentials | ⏳ | Test remember me functionality |
| 2 | Profile information review | Saved customer data displays correctly | ⏳ | Verify all profile fields |
| 3 | Order history access | Previous orders display with complete details | ⏳ | Check order details accuracy |
| 4 | Profile data modification | Profile updates save successfully | ⏳ | Test individual field updates |
| 5 | Repeat purchase process | Shopping experience maintains consistency | ⏳ | Compare with first-time experience |

### Test Scenario 3: Administrative Functions

| Step | Action | Expected Outcome | Status | Notes |
|------|--------|------------------|--------|-------|
| 1 | Admin authentication | Administrative panel access granted | ⏳ | Test admin login process |
| 2 | Product management | New product creation and modification | ⏳ | Test all product fields |
| 3 | Product data modification | Changes reflect immediately on frontend | ⏳ | Verify real-time updates |
| 4 | Order management | Customer order visibility and status updates | ⏳ | Test order status workflow |
| 5 | Order status updates | Status changes visible to customers | ⏳ | Verify customer notifications |

## Form Validation Testing

### User Registration Form

| Field | Valid Data Test | Invalid Data Test | Status | Notes |
|-------|----------------|-------------------|--------|-------|
| **Email Address** | test@example.com | invalid-email-format | ⏳ | Check email format validation |
| **Password** | SecurePass123! | 123 (too weak) | ⏳ | Test password strength requirements |
| **Password Confirmation** | Matching passwords | Non-matching passwords | ⏳ | Verify password confirmation |
| **Required Fields** | All fields completed | Empty required fields | ⏳ | Check field validation messages |

### Checkout Form

| Field | Valid Data Test | Invalid Data Test | Status | Notes |
|-------|----------------|-------------------|--------|-------|
| **Full Name** | John Doe | Empty field | ⏳ | Required field validation |
| **Email Address** | john@example.com | not-an-email | ⏳ | Email format validation |
| **Phone Number** | +1234567890 | invalid-phone | ⏳ | Phone format validation |
| **Address Fields** | Complete address | Missing required fields | ⏳ | Address validation |
| **Payment Information** | Valid card details | Invalid card number | ⏳ | Stripe validation integration |

### Contact Form

| Field | Valid Data Test | Invalid Data Test | Status | Notes |
|-------|----------------|-------------------|--------|-------|
| **Name** | Customer Name | Empty field | ⏳ | Required field validation |
| **Email** | customer@email.com | invalid.email | ⏳ | Email validation |
| **Message** | Valid inquiry message | Empty message | ⏳ | Message content validation |
| **Machine Type** | CNC Mill selection | No selection | ⏳ | Dropdown validation |

## Input Validation Testing

| Test Case | Bad Input | Expected Result | ✅/❌ | Notes |
|-----------|-----------|-----------------|-------|-------|
| **Invalid Email** | "not-an-email" | Show validation error | ⏳ | Email format validation |
| **Weak Password** | "123" | Reject password | ⏳ | Password strength validation |
| **Negative Quantity** | -1 in cart | Don't allow or show error | ⏳ | Cart quantity validation |
| **Empty Required Field** | Leave name blank | Show "required" error | ⏳ | Required field validation |
| **Long Input** | 1000 character string | Handle gracefully | ⏳ | Input length validation |
| **Special Characters** | `<script>alert('test')</script>` | Sanitize and escape | ⏳ | XSS prevention testing |
| **SQL Injection** | `'; DROP TABLE users--` | Block malicious input | ⏳ | SQL injection prevention |

## CRUD Operations Testing

### Products CRUD Testing

| Operation | Test Case | Steps | Expected Result | ✅/❌ | Priority | Notes |
|-----------|-----------|-------|----------------|-------|----------|-------|
| **Create** | Admin adds new product | 1. Login as admin<br>2. Navigate to admin panel<br>3. Add new product<br>4. Fill all required fields<br>5. Save product | Product saved to database and visible on site | ⏳ | HIGH | Test with valid and edge case data |
| **Read** | View product on frontend | 1. Navigate to products page<br>2. Click on product<br>3. View product details | Product displays correctly with all information | ⏳ | HIGH | Verify all fields display properly |
| **Update** | Admin edits existing product | 1. Access admin panel<br>2. Find existing product<br>3. Edit product details<br>4. Save changes | Changes reflected immediately on frontend | ⏳ | HIGH | Test partial and complete updates |
| **Delete** | Admin removes product | 1. Select product in admin<br>2. Delete product<br>3. Confirm deletion | Product no longer visible on site | ⏳ | MEDIUM | Verify proper cleanup and error handling |

### Orders CRUD Testing

| Operation | Test Case | Steps | Expected Result | ✅/❌ | Priority | Notes |
|-----------|-----------|-------|----------------|-------|----------|-------|
| **Create** | User completes checkout | 1. Add items to cart<br>2. Proceed to checkout<br>3. Fill order form<br>4. Complete payment | Order created in database with correct details | ⏳ | HIGH | Test with various item combinations |
| **Read** | User views order history | 1. Login as customer<br>2. Navigate to profile<br>3. View order history<br>4. Click order details | Orders displayed with complete information | ⏳ | HIGH | Verify order details accuracy |
| **Update** | Admin updates order status | 1. Access admin panel<br>2. Find order<br>3. Update status<br>4. Save changes | Status change saved and visible to customer | ⏳ | HIGH | Test all status transitions |
| **Delete** | N/A - Orders preserved | Order deletion not permitted | Orders maintained for audit trail | N/A | N/A | Orders should never be deleted |

### User Profiles CRUD Testing

| Operation | Test Case | Steps | Expected Result | ✅/❌ | Priority | Notes |
|-----------|-----------|-------|----------------|-------|----------|-------|
| **Create** | User registers account | 1. Visit registration page<br>2. Fill registration form<br>3. Submit form<br>4. Verify email (if required) | Profile created and user can login | ⏳ | HIGH | Test with various email formats |
| **Read** | User views profile | 1. Login as user<br>2. Navigate to profile page<br>3. View profile information | Profile info displayed correctly | ⏳ | MEDIUM | Verify all saved information appears |
| **Update** | User edits profile | 1. Access profile page<br>2. Edit profile fields<br>3. Save changes<br>4. Verify updates | Changes saved and reflected immediately | ⏳ | MEDIUM | Test individual field updates |
| **Delete** | User deletes account | 1. Access account settings<br>2. Choose delete account<br>3. Confirm deletion | Account deactivated, data anonymized | ⏳ | LOW | Verify GDPR compliance |

### Shopping Cart CRUD Testing

| Operation | Test Case | Steps | Expected Result | ✅/❌ | Priority | Notes |
|-----------|-----------|-------|----------------|-------|----------|-------|
| **Create** | Add item to cart | 1. Browse products<br>2. Select product<br>3. Choose quantity<br>4. Add to cart | Item appears in cart with correct details | ⏳ | HIGH | Test quantity validation |
| **Read** | View cart contents | 1. Add items to cart<br>2. Navigate to cart page<br>3. Review items | All cart items display with totals | ⏳ | HIGH | Verify price calculations |
| **Update** | Modify cart items | 1. Access cart<br>2. Change item quantities<br>3. Update cart | Quantities and totals update correctly | ⏳ | HIGH | Test zero quantity handling |
| **Delete** | Remove cart items | 1. Access cart<br>2. Remove specific items<br>3. Confirm removal | Items removed from cart | ⏳ | HIGH | Test single and bulk removal |

## Payment Testing

### Payment Integration Testing

| Test Scenario | Test Card | Expected Result | ✅/❌ | Notes |
|---------------|-----------|-----------------|-------|-------|
| **Successful Payment** | 4242 4242 4242 4242 | Payment goes through | ⏳ | Standard test card |
| **Declined Card** | 4000 0000 0000 0002 | Payment rejected | ⏳ | Display clear error message |
| **Expired Card** | Use expired date | Show expiry error | ⏳ | Test expiration validation |
| **Invalid CVV** | Wrong security code | Show CVV error | ⏳ | Security code validation |
| **Insufficient Funds** | 4000 0000 0000 9995 | Decline with specific message | ⏳ | Test specific decline reasons |
| **Processing Error** | 4000 0000 0000 0119 | Handle processing failure | ⏳ | Error handling validation |

### Payment Form Validation

| Field | Test Case | Expected Behavior | ✅/❌ | Priority |
|-------|-----------|-------------------|-------|----------|
| **Card Number** | Invalid format | Real-time validation error | ⏳ | HIGH |
| **Expiry Date** | Past date | Expiration validation | ⏳ | HIGH |
| **CVV** | Incorrect length | Security code validation | ⏳ | HIGH |
| **Cardholder Name** | Empty field | Required field validation | ⏳ | MEDIUM |

## Responsive Design Testing

### Breakpoint Testing

| Device Category | Screen Size | Layout Test | Navigation Test | Forms Test | ✅/❌ | Priority |
|----------------|-------------|-------------|-----------------|------------|-------|----------|
| **Mobile** | 320px - 767px | Layout adapts correctly | Hamburger menu works | Forms stack properly | ⏳ | HIGH |
| **Small Mobile** | 320px - 480px | Single column layout | Touch-friendly navigation | Simplified forms | ⏳ | HIGH |
| **Large Mobile** | 481px - 767px | Optimized mobile layout | Expanded touch targets | Mobile-optimized forms | ⏳ | HIGH |
| **Tablet Portrait** | 768px - 1024px | 2-column layout | Tab navigation works | Forms resize appropriately | ⏳ | HIGH |
| **Tablet Landscape** | 768px - 1199px | Multi-column layout | Full navigation visible | Horizontal form layouts | ⏳ | MEDIUM |
| **Desktop** | 1200px+ | Full layout displayed | Complete navigation | Full-width forms | ⏳ | MEDIUM |
| **Large Desktop** | 1440px+ | Optimized wide layout | Enhanced navigation | Spacious form layouts | ⏳ | LOW |

### Mobile Device Testing

| Device | Screen Size | Orientation | Browser | Test Result | ✅/❌ | Priority |
|--------|-------------|-------------|---------|-------------|-------|----------|
| **iPhone 14** | 390x844 | Portrait | Safari | All features functional | ⏳ | HIGH |
| **iPhone 14** | 844x390 | Landscape | Safari | Layout adapts properly | ⏳ | HIGH |
| **iPhone 12** | 390x844 | Portrait | Chrome | Cross-browser compatibility | ⏳ | HIGH |
| **Samsung Galaxy S21** | 384x854 | Portrait | Chrome | Android compatibility | ⏳ | HIGH |
| **iPad Air** | 820x1180 | Portrait | Safari | Tablet layout testing | ⏳ | HIGH |
| **iPad Air** | 1180x820 | Landscape | Safari | Tablet landscape mode | ⏳ | HIGH |

### Touch Interface Testing

| Feature | Test Case | Expected Result | Test Environment | ✅/❌ | Priority |
|---------|-----------|----------------|------------------|-------|----------|
| **Product Cards** | Tap to view details | Product detail page opens | Mobile devices | ⏳ | HIGH |
| **Cart Management** | Add/remove items via touch | Items update immediately | Touch screens | ⏳ | HIGH |
| **Form Input** | Touch input fields | Keyboard appears, field focuses | Mobile browsers | ⏳ | HIGH |
| **Navigation Menu** | Touch menu items | Pages load correctly | All touch devices | ⏳ | HIGH |
| **Checkout Process** | Complete purchase on mobile | Full checkout works | Mobile checkout | ⏳ | HIGH |

## Browser Compatibility Testing

### Desktop Browsers

| Browser | Version | Homepage | Products | Cart | Checkout | Status |
|---------|---------|----------|----------|------|----------|--------|
| **Chrome** | 120+ | Test all features | Test product browsing | Test cart operations | Test checkout process | ⏳ |
| **Firefox** | 115+ | Test all features | Test product browsing | Test cart operations | Test checkout process | ⏳ |
| **Safari** | 16+ | Test all features | Test product browsing | Test cart operations | Test checkout process | ⏳ |
| **Edge** | 118+ | Test all features | Test product browsing | Test cart operations | Test checkout process | ⏳ |

### Mobile Browsers

| Browser | Platform | Navigation | Search | Purchase | Status |
|---------|----------|------------|--------|----------|--------|
| **Chrome Mobile** | Android | Test navigation | Test search functionality | Test complete purchase | ⏳ |
| **Safari Mobile** | iOS | Test navigation | Test search functionality | Test complete purchase | ⏳ |
| **Firefox Mobile** | Android | Test navigation | Test search functionality | Test complete purchase | ⏳ |
| **Samsung Internet** | Android | Test navigation | Test search functionality | Test complete purchase | ⏳ |

## Accessibility Testing

### Keyboard Navigation Testing

| Component | Keyboard Test | Expected Behavior | ✅/❌ | Priority |
|-----------|---------------|-------------------|-------|----------|
| **Main Navigation** | Tab through menu | All links accessible via keyboard | ⏳ | HIGH |
| **Product Listings** | Navigate product grid | Products reachable with Tab/Arrow keys | ⏳ | HIGH |
| **Shopping Cart** | Modify cart with keyboard | All cart functions keyboard accessible | ⏳ | HIGH |
| **Forms** | Complete forms without mouse | All form interactions keyboard-only | ⏳ | HIGH |
| **Checkout Process** | Complete purchase via keyboard | Full checkout process accessible | ⏳ | HIGH |

### Screen Reader Testing

| Test Scenario | Expected Behavior | ✅/❌ | Priority | Notes |
|---------------|-------------------|-------|----------|-------|
| **Navigation Menu** | Menu items read correctly | ⏳ | HIGH | Test hierarchical navigation |
| **Product Information** | All product details accessible | ⏳ | HIGH | Price, description, availability |
| **Shopping Cart** | Cart contents and totals read | ⏳ | HIGH | Item quantities and prices |
| **Checkout Form** | Form fields and labels clear | ⏳ | HIGH | Payment form accessibility |
| **Error Messages** | Errors announced clearly | ⏳ | HIGH | Form validation feedback |

## Testing Checklist

### Core Testing Requirements
- [ ] ⏳ Execute manual testing of main user journeys
- [ ] ⏳ Test on mobile and desktop devices
- [ ] ⏳ Validate browser compatibility
- [ ] ⏳ Test payment integration with Stripe test cards
- [ ] ⏳ Verify responsive design across breakpoints
- [ ] ⏳ Test accessibility features
- [ ] ⏳ Validate form submission and error handling
- [ ] ⏳ Test admin functionality

### Enhanced Testing Coverage
- [ ] ⏳ Test error handling and edge cases
- [ ] ⏳ Validate user authentication flows
- [ ] ⏳ Test CRUD operations comprehensively
- [ ] ⏳ Verify data persistence across sessions
- [ ] ⏳ Test performance on different devices

### Advanced Testing Implementation
- [ ] ⏳ Test security aspects (XSS, CSRF prevention)
- [ ] ⏳ Validate accessibility compliance (WCAG 2.1)
- [ ] ⏳ Test performance considerations
- [ ] ⏳ Verify SEO optimization
- [ ] ⏳ Test internationalization features

## Test Execution Status

**Current Status**: ✅ **Framework ready for execution**  
**Automated Foundation**: ✅ **197 tests passing with 97% coverage**  
**Manual Testing**: ⏳ **Test scripts prepared, ready to execute**

The manual testing framework complements the comprehensive automated testing suite, providing complete validation of user experience, device compatibility, and business process integrity.
