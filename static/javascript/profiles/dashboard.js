/* ========================================================================
   CNCraft - Modern Dashboard JavaScript
   ========================================================================
   Enhanced dashboard functionality with smooth animations, better UX,
   and modern interactions for a professional e-commerce experience.
   ======================================================================== */

const DashboardManager = {
    // Configuration
    config: {
        animationDuration: 300,
        cardHoverDelay: 100,
        formSelector: '#profile-update-form',
        sectionSelector: '.dashboard-section',
        collapseSelector: '[data-bs-toggle="collapse"]'
    },

    // Initialize dashboard functionality
    init() {
        this.bindEventListeners();
        this.initializeCardAnimations();
        this.initializeFormEnhancements();
        this.initializeProgressiveEnhancement();
        this.initializeMobileOptimizations();
        console.log('Dashboard Manager initialized successfully');
    },

    // Bind all event listeners
    bindEventListeners() {
        // Card hover effects
        document.querySelectorAll(this.config.sectionSelector).forEach(card => {
            card.addEventListener('mouseenter', () => this.handleCardHover(card, true));
            card.addEventListener('mouseleave', () => this.handleCardHover(card, false));
        });

        // Enhanced collapse functionality
        document.querySelectorAll(this.config.collapseSelector).forEach(trigger => {
            trigger.addEventListener('click', (e) => this.handleCollapseToggle(e));
        });

        // Form submission enhancements
        const form = document.querySelector(this.config.formSelector);
        if (form) {
            form.addEventListener('submit', (e) => this.handleFormSubmit(e));
        }

        // Button enhancements
        document.querySelectorAll('.btn').forEach(btn => {
            btn.addEventListener('click', (e) => this.handleButtonClick(e));
        });

        // Order item interactions
        document.querySelectorAll('.order-item').forEach(item => {
            item.addEventListener('click', () => this.handleOrderItemClick(item));
        });

        // Account option interactions
        document.querySelectorAll('.account-option').forEach(option => {
            option.addEventListener('click', () => this.handleAccountOptionClick(option));
        });
    },

    // Initialize card animations
    initializeCardAnimations() {
        // Stagger card entrance animations
        const cards = document.querySelectorAll(this.config.sectionSelector);
        cards.forEach((card, index) => {
            card.style.opacity = '0';
            card.style.transform = 'translateY(20px)';
            
            setTimeout(() => {
                card.style.transition = `all ${this.config.animationDuration}ms ease`;
                card.style.opacity = '1';
                card.style.transform = 'translateY(0)';
            }, index * 100);
        });

        // Animate progress placeholders
        const placeholders = document.querySelectorAll('.preferences-placeholder');
        placeholders.forEach(placeholder => {
            this.animatePlaceholder(placeholder);
        });
    },

    // Handle card hover effects
    handleCardHover(card, isHovering) {
        const header = card.querySelector('.section-header');
        if (header) {
            const icon = header.querySelector('i');
            if (icon) {
                if (isHovering) {
                    icon.style.transform = 'scale(1.1) rotate(5deg)';
                    icon.style.color = '#0080ff';
                } else {
                    icon.style.transform = 'scale(1) rotate(0deg)';
                    icon.style.color = '';
                }
            }
        }
    },

    // Enhanced collapse toggle
    handleCollapseToggle(event) {
        const button = event.currentTarget;
        const targetId = button.getAttribute('data-bs-target');
        const target = document.querySelector(targetId);
        
        if (target && button.id === 'editProfileBtn') {
            // Add loading state
            const originalContent = button.innerHTML;
            button.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Loading...';
            button.disabled = true;
            
            setTimeout(() => {
                // Check if the target is currently shown or will be shown
                const isCurrentlyShown = target.classList.contains('show');
                button.innerHTML = isCurrentlyShown ? 
                    '<i class="fas fa-edit"></i> Edit Profile' : 
                    '<i class="fas fa-times"></i> Cancel Edit';
                button.disabled = false;
                
                // Update button class
                if (isCurrentlyShown) {
                    button.classList.remove('btn-secondary');
                    button.classList.add('btn-outline-black');
                } else {
                    button.classList.remove('btn-outline-black');
                    button.classList.add('btn-secondary');
                }
            }, 300);

            // Scroll to form when opening
            if (!target.classList.contains('show')) {
                setTimeout(() => {
                    target.scrollIntoView({ 
                        behavior: 'smooth', 
                        block: 'center' 
                    });
                }, 400);
            }
        }
    },

    // Initialize form enhancements
    initializeFormEnhancements() {
        const form = document.querySelector(this.config.formSelector);
        if (!form) return;

        // Add loading states to form fields
        const inputs = form.querySelectorAll('input, select, textarea');
        inputs.forEach(input => {
            input.addEventListener('focus', () => this.handleFieldFocus(input));
            input.addEventListener('blur', () => this.handleFieldBlur(input));
            input.addEventListener('input', () => this.handleFieldInput(input));
        });

        // Enhance form validation
        this.addFormValidation(form);
    },

    // Handle field focus
    handleFieldFocus(field) {
        const wrapper = field.closest('.form-group') || field.closest('.col-12');
        if (wrapper) {
            wrapper.style.transform = 'scale(1.02)';
            wrapper.style.transition = 'transform 0.2s ease';
        }
    },

    // Handle field blur
    handleFieldBlur(field) {
        const wrapper = field.closest('.form-group') || field.closest('.col-12');
        if (wrapper) {
            wrapper.style.transform = 'scale(1)';
        }
    },

    // Handle field input
    handleFieldInput(field) {
        // Add visual feedback for valid input
        if (field.value.trim()) {
            field.style.borderColor = '#28a745';
            field.style.boxShadow = '0 0 0 0.2rem rgba(40, 167, 69, 0.15)';
        } else {
            field.style.borderColor = '';
            field.style.boxShadow = '';
        }
    },

    // Add form validation
    addFormValidation(form) {
        form.addEventListener('submit', (e) => {
            let isValid = true;
            const requiredFields = form.querySelectorAll('[required]');
            
            requiredFields.forEach(field => {
                if (!field.value.trim()) {
                    this.showFieldError(field, 'This field is required');
                    isValid = false;
                } else {
                    this.clearFieldError(field);
                }
            });

            if (!isValid) {
                e.preventDefault();
                this.showNotification('Please complete all required fields', 'error');
            }
        });
    },

    // Show field error
    showFieldError(field, message) {
        field.style.borderColor = '#dc3545';
        field.style.boxShadow = '0 0 0 0.2rem rgba(220, 53, 69, 0.15)';
        
        let errorDiv = field.parentNode.querySelector('.field-error');
        if (!errorDiv) {
            errorDiv = document.createElement('div');
            errorDiv.className = 'field-error text-danger small mt-1';
            field.parentNode.appendChild(errorDiv);
        }
        errorDiv.textContent = message;
    },

    // Clear field error
    clearFieldError(field) {
        field.style.borderColor = '';
        field.style.boxShadow = '';
        
        const errorDiv = field.parentNode.querySelector('.field-error');
        if (errorDiv) {
            errorDiv.remove();
        }
    },

    // Handle form submission
    handleFormSubmit(event) {
        const form = event.target;
        const submitBtn = form.querySelector('button[type="submit"]');
        
        if (submitBtn) {
            const originalText = submitBtn.innerHTML;
            submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Updating...';
            submitBtn.disabled = true;
            
            // Show loading overlay
            this.showLoadingOverlay();
            
            // Reset after delay (in real app, this would be on form response)
            setTimeout(() => {
                submitBtn.innerHTML = originalText;
                submitBtn.disabled = false;
                this.hideLoadingOverlay();
                this.showNotification('Profile updated successfully!', 'success');
            }, 2000);
        }
    },

    // Handle button clicks
    handleButtonClick(event) {
        const button = event.currentTarget;
        
        // Add ripple effect
        this.addRippleEffect(button, event);
        
        // Add click feedback
        button.style.transform = 'scale(0.98)';
        setTimeout(() => {
            button.style.transform = '';
        }, 150);
    },

    // Add ripple effect to buttons
    addRippleEffect(element, event) {
        const ripple = document.createElement('span');
        const rect = element.getBoundingClientRect();
        const size = Math.max(rect.width, rect.height);
        const x = event.clientX - rect.left - size / 2;
        const y = event.clientY - rect.top - size / 2;
        
        ripple.style.cssText = `
            position: absolute;
            width: ${size}px;
            height: ${size}px;
            left: ${x}px;
            top: ${y}px;
            background: rgba(255, 255, 255, 0.5);
            border-radius: 50%;
            transform: scale(0);
            animation: ripple 0.6s linear;
            pointer-events: none;
            z-index: 1;
        `;
        
        element.style.position = 'relative';
        element.style.overflow = 'hidden';
        element.appendChild(ripple);
        
        setTimeout(() => ripple.remove(), 600);
    },

    // Handle order item clicks
    handleOrderItemClick(item) {
        // Add selection state
        document.querySelectorAll('.order-item').forEach(i => i.classList.remove('selected'));
        item.classList.add('selected');
        
        // Animate selection
        item.style.transform = 'scale(1.02)';
        setTimeout(() => {
            item.style.transform = '';
        }, 200);
    },

    // Handle account option clicks
    handleAccountOptionClick(option) {
        const button = option.querySelector('button');
        if (button && !button.disabled) {
            // Future functionality placeholder
            this.showNotification('Feature coming soon!', 'info');
        }
    },

    // Animate placeholder elements
    animatePlaceholder(placeholder) {
        const items = placeholder.querySelectorAll('.preference-item');
        items.forEach((item, index) => {
            item.style.animationDelay = `${index * 0.2}s`;
            item.style.animation = 'fadeInUp 0.6s ease forwards';
        });
    },

    // Initialize progressive enhancement
    initializeProgressiveEnhancement() {
        // Add smooth scrolling to internal links
        document.querySelectorAll('a[href^="#"]').forEach(link => {
            link.addEventListener('click', (e) => {
                e.preventDefault();
                const href = link.getAttribute('href');
                // Skip empty href or just "#"
                if (href && href !== '#') {
                    const target = document.querySelector(href);
                    if (target) {
                        target.scrollIntoView({ behavior: 'smooth' });
                    }
                }
            });
        });

        // Add keyboard navigation
        document.addEventListener('keydown', (e) => this.handleKeyboardNavigation(e));
    },

    // Handle keyboard navigation
    handleKeyboardNavigation(event) {
        // Tab navigation enhancements
        if (event.key === 'Tab') {
            const focusedElement = document.activeElement;
            if (focusedElement.classList.contains('dashboard-section')) {
                focusedElement.style.outline = '3px solid #0080ff';
            }
        }
        
        // Escape key functionality
        if (event.key === 'Escape') {
            const openCollapse = document.querySelector('.collapse.show');
            if (openCollapse) {
                const button = document.querySelector(`[data-bs-target="#${openCollapse.id}"]`);
                if (button) button.click();
            }
        }
    },

    // Initialize mobile optimizations
    initializeMobileOptimizations() {
        if (window.innerWidth <= 768) {
            // Add touch feedback
            this.addTouchFeedback();
            
            // Optimize for mobile interactions
            this.optimizeForTouch();
        }
        
        // Handle orientation changes
        window.addEventListener('orientationchange', () => {
            setTimeout(() => this.handleOrientationChange(), 100);
        });
    },

    // Add touch feedback
    addTouchFeedback() {
        document.querySelectorAll('.btn, .dashboard-section, .order-item, .account-option').forEach(element => {
            element.addEventListener('touchstart', function() {
                this.classList.add('touch-active');
            });
            
            element.addEventListener('touchend', function() {
                setTimeout(() => {
                    this.classList.remove('touch-active');
                }, 150);
            });
        });
    },

    // Optimize for touch devices
    optimizeForTouch() {
        // Increase touch targets
        const buttons = document.querySelectorAll('.btn');
        buttons.forEach(btn => {
            btn.style.minHeight = '44px';
            btn.style.minWidth = '44px';
        });
    },

    // Handle orientation changes
    handleOrientationChange() {
        // Refresh layout calculations
        const cards = document.querySelectorAll(this.config.sectionSelector);
        cards.forEach(card => {
            card.style.height = 'auto';
        });
    },

    // Show loading overlay
    showLoadingOverlay() {
        let overlay = document.querySelector('.dashboard-loading-overlay');
        if (!overlay) {
            overlay = document.createElement('div');
            overlay.className = 'dashboard-loading-overlay';
            overlay.innerHTML = `
                <div class="loading-content">
                    <i class="fas fa-spinner fa-spin fa-2x"></i>
                    <p>Updating your information...</p>
                </div>
            `;
            document.body.appendChild(overlay);
        }
        overlay.classList.add('show');
    },

    // Hide loading overlay
    hideLoadingOverlay() {
        const overlay = document.querySelector('.dashboard-loading-overlay');
        if (overlay) {
            overlay.classList.remove('show');
            setTimeout(() => overlay.remove(), 300);
        }
    },

    // Show notification
    showNotification(message, type = 'info') {
        const notification = document.createElement('div');
        notification.className = `dashboard-notification notification-${type}`;
        notification.innerHTML = `
            <div class="notification-content">
                <i class="fas fa-${this.getNotificationIcon(type)}"></i>
                <span>${message}</span>
                <button type="button" class="notification-close">
                    <i class="fas fa-times"></i>
                </button>
            </div>
        `;
        
        document.body.appendChild(notification);
        
        // Show notification
        setTimeout(() => notification.classList.add('show'), 100);
        
        // Auto-hide after delay
        setTimeout(() => {
            notification.classList.remove('show');
            setTimeout(() => notification.remove(), 300);
        }, 4000);
        
        // Close button functionality
        notification.querySelector('.notification-close').addEventListener('click', () => {
            notification.classList.remove('show');
            setTimeout(() => notification.remove(), 300);
        });
    },

    // Get notification icon
    getNotificationIcon(type) {
        const icons = {
            success: 'check-circle',
            error: 'exclamation-triangle',
            warning: 'exclamation-triangle',
            info: 'info-circle'
        };
        return icons[type] || 'info-circle';
    },

    // Inject notification styles
    injectStyles() {
        const styles = `
            @keyframes ripple {
                to { transform: scale(2); opacity: 0; }
            }
            
            @keyframes fadeInUp {
                from {
                    opacity: 0;
                    transform: translateY(20px);
                }
                to {
                    opacity: 1;
                    transform: translateY(0);
                }
            }
            
            .touch-active {
                transform: scale(0.98);
                opacity: 0.8;
            }
            
            .order-item.selected {
                border-color: #0080ff !important;
                box-shadow: 0 0 0 2px rgba(0, 128, 255, 0.2) !important;
            }
            
            .dashboard-loading-overlay {
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                background: rgba(0, 0, 0, 0.8);
                backdrop-filter: blur(5px);
                display: flex;
                align-items: center;
                justify-content: center;
                z-index: 9999;
                opacity: 0;
                visibility: hidden;
                transition: all 0.3s ease;
            }
            
            .dashboard-loading-overlay.show {
                opacity: 1;
                visibility: visible;
            }
            
            .loading-content {
                text-align: center;
                color: white;
                background: rgba(255, 255, 255, 0.1);
                padding: 2rem;
                border-radius: 12px;
                backdrop-filter: blur(10px);
            }
            
            .loading-content i {
                color: #0080ff;
                margin-bottom: 1rem;
            }
            
            .dashboard-notification {
                position: fixed;
                top: 20px;
                right: 20px;
                z-index: 10000;
                max-width: 400px;
                background: white;
                border-radius: 12px;
                box-shadow: 0 8px 30px rgba(0,0,0,0.15);
                border-left: 4px solid #17a2b8;
                opacity: 0;
                transform: translateX(100%);
                transition: all 0.3s ease;
            }
            
            .dashboard-notification.show {
                opacity: 1;
                transform: translateX(0);
            }
            
            .notification-success {
                border-left-color: #28a745;
            }
            
            .notification-error {
                border-left-color: #dc3545;
            }
            
            .notification-warning {
                border-left-color: #ffc107;
            }
            
            .notification-content {
                padding: 1rem;
                display: flex;
                align-items: center;
                gap: 0.75rem;
            }
            
            .notification-content i:first-child {
                color: #17a2b8;
                font-size: 1.2rem;
            }
            
            .notification-success .notification-content i:first-child {
                color: #28a745;
            }
            
            .notification-error .notification-content i:first-child {
                color: #dc3545;
            }
            
            .notification-warning .notification-content i:first-child {
                color: #ffc107;
            }
            
            .notification-content span {
                flex: 1;
                color: #2c3e50;
                font-weight: 500;
            }
            
            .notification-close {
                background: none;
                border: none;
                color: #6c757d;
                cursor: pointer;
                padding: 0.25rem;
                border-radius: 4px;
                transition: background-color 0.3s ease;
            }
            
            .notification-close:hover {
                background-color: #f8f9fa;
            }
            
            @media (max-width: 768px) {
                .dashboard-notification {
                    top: 10px;
                    right: 10px;
                    left: 10px;
                    max-width: none;
                }
            }
        `;
        
        const styleSheet = document.createElement('style');
        styleSheet.textContent = styles;
        document.head.appendChild(styleSheet);
    }
};

// Initialize when DOM is ready
document.addEventListener('DOMContentLoaded', function() {
    DashboardManager.injectStyles();
    DashboardManager.init();
});

// Export for potential external use
window.DashboardManager = DashboardManager;
