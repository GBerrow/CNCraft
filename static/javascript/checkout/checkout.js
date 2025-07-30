/* ========================================================================
   CNCraft - Modern Checkout Page JavaScript
   ========================================================================
   Enhanced checkout functionality with form validation, UX improvements,
   and accessibility features for a professional e-commerce experience.
   ======================================================================== */

const CheckoutManager = {
    // Configuration and state
    config: {
        formSelector: '#payment-form',
        loadingOverlaySelector: '#loading-overlay',
        submitButtonSelector: '#submit-button',
        cardErrorsSelector: '#card-errors',
        progressSteps: '.progress-step',
        requiredFields: [
            'full_name',
            'email',
            'phone_number',
            'street_address1',
            'town_or_city',
            'postcode',
            'country'
        ],
        validationRules: {
            email: /^[^\s@]+@[^\s@]+\.[^\s@]+$/,
            phone: /^[\+]?[1-9][\d]{0,15}$/,
            postcode: /^[A-Z0-9\s\-]{3,10}$/i
        }
    },

    state: {
        isFormValid: false,
        isSubmitting: false,
        validatedFields: new Set(),
        touchedFields: new Set()
    },

    // Initialize the checkout manager
    init() {
        this.bindEventListeners();
        this.initializeFormValidation();
        this.initializeProgressTracking();
        this.initializeAccessibilityFeatures();
        this.initializeLoadingStates();
        this.initializeMobileEnhancements();
        console.log('Checkout Manager initialized successfully');
    },

    // Bind all event listeners
    bindEventListeners() {
        const form = document.querySelector(this.config.formSelector);
        if (!form) return;

        // Form submission handling
        form.addEventListener('submit', (e) => this.handleFormSubmit(e));

        // Real-time field validation
        this.config.requiredFields.forEach(fieldName => {
            const field = form.querySelector(`[name="${fieldName}"]`);
            if (field) {
                field.addEventListener('blur', (e) => this.validateField(e.target));
                field.addEventListener('input', (e) => this.handleFieldInput(e.target));
            }
        });

        // Payment method selection
        const paymentMethods = document.querySelectorAll('.payment-method');
        paymentMethods.forEach(method => {
            method.addEventListener('click', (e) => this.handlePaymentMethodSelect(e.target));
        });

        // Submit button enhancements
        const submitButton = document.querySelector(this.config.submitButtonSelector);
        if (submitButton) {
            submitButton.addEventListener('click', () => this.trackFormProgress());
        }

        // Keyboard navigation
        document.addEventListener('keydown', (e) => this.handleKeyboardNavigation(e));

        // Window visibility for security
        document.addEventListener('visibilitychange', () => this.handleVisibilityChange());
    },

    // Initialize comprehensive form validation
    initializeFormValidation() {
        const form = document.querySelector(this.config.formSelector);
        if (!form) return;

        // Add validation classes to form elements
        this.config.requiredFields.forEach(fieldName => {
            const field = form.querySelector(`[name="${fieldName}"]`);
            if (field) {
                field.setAttribute('aria-required', 'true');
                this.addFieldValidationUI(field);
            }
        });

        // Initial validation state
        this.updateFormValidationState();
    },

    // Add validation UI elements to fields
    addFieldValidationUI(field) {
        const wrapper = field.closest('.form-group') || field.parentElement;
        
        // Create validation feedback element
        const feedback = document.createElement('div');
        feedback.className = 'validation-feedback';
        feedback.setAttribute('aria-live', 'polite');
        feedback.style.display = 'none';
        
        wrapper.appendChild(feedback);

        // Add validation icon
        const iconWrapper = document.createElement('div');
        iconWrapper.className = 'field-validation-icon';
        iconWrapper.innerHTML = '<i class="fas fa-check-circle text-success"></i><i class="fas fa-exclamation-circle text-danger"></i>';
        wrapper.style.position = 'relative';
        wrapper.appendChild(iconWrapper);
    },

    // Validate individual field
    validateField(field) {
        const fieldName = field.name;
        const value = field.value.trim();
        const wrapper = field.closest('.form-group') || field.parentElement;
        const feedback = wrapper.querySelector('.validation-feedback');
        const iconWrapper = wrapper.querySelector('.field-validation-icon');
        
        let isValid = true;
        let message = '';

        // Required field check
        if (this.config.requiredFields.includes(fieldName) && !value) {
            isValid = false;
            message = `${this.getFieldLabel(field)} is required`;
        }
        // Specific validation rules
        else if (value) {
            switch (fieldName) {
                case 'email':
                    if (!this.config.validationRules.email.test(value)) {
                        isValid = false;
                        message = 'Please enter a valid email address';
                    }
                    break;
                case 'phone_number':
                    if (!this.config.validationRules.phone.test(value.replace(/\s/g, ''))) {
                        isValid = false;
                        message = 'Please enter a valid phone number';
                    }
                    break;
                case 'postcode':
                    if (!this.config.validationRules.postcode.test(value)) {
                        isValid = false;
                        message = 'Please enter a valid postal code';
                    }
                    break;
            }
        }

        // Update UI based on validation result
        this.updateFieldValidationUI(field, wrapper, feedback, iconWrapper, isValid, message);
        
        // Update validation state
        if (isValid) {
            this.state.validatedFields.add(fieldName);
        } else {
            this.state.validatedFields.delete(fieldName);
        }

        this.updateFormValidationState();
        return isValid;
    },

    // Update field validation UI
    updateFieldValidationUI(field, wrapper, feedback, iconWrapper, isValid, message) {
        // Remove existing validation classes
        field.classList.remove('is-valid', 'is-invalid');
        wrapper.classList.remove('field-valid', 'field-invalid');

        if (this.state.touchedFields.has(field.name)) {
            if (isValid) {
                field.classList.add('is-valid');
                wrapper.classList.add('field-valid');
                feedback.style.display = 'none';
            } else {
                field.classList.add('is-invalid');
                wrapper.classList.add('field-invalid');
                feedback.textContent = message;
                feedback.style.display = 'block';
                feedback.className = 'validation-feedback text-danger';
            }

            // Update validation icon
            if (iconWrapper) {
                iconWrapper.style.display = 'block';
                const successIcon = iconWrapper.querySelector('.fa-check-circle');
                const errorIcon = iconWrapper.querySelector('.fa-exclamation-circle');
                
                if (isValid) {
                    successIcon.style.display = 'inline';
                    errorIcon.style.display = 'none';
                } else {
                    successIcon.style.display = 'none';
                    errorIcon.style.display = 'inline';
                }
            }
        }
    },

    // Handle field input with debouncing
    handleFieldInput(field) {
        this.state.touchedFields.add(field.name);
        
        // Debounce validation
        clearTimeout(field.validationTimeout);
        field.validationTimeout = setTimeout(() => {
            this.validateField(field);
        }, 500);
    },

    // Get user-friendly field label
    getFieldLabel(field) {
        const label = field.closest('.form-group')?.querySelector('label');
        if (label) {
            return label.textContent.replace('*', '').trim();
        }
        return field.name.replace('_', ' ').replace(/\b\w/g, l => l.toUpperCase());
    },

    // Update overall form validation state
    updateFormValidationState() {
        const requiredFieldsValid = this.config.requiredFields.every(field => 
            this.state.validatedFields.has(field)
        );
        
        this.state.isFormValid = requiredFieldsValid;
        
        // Update submit button state
        const submitButton = document.querySelector(this.config.submitButtonSelector);
        if (submitButton) {
            submitButton.disabled = !this.state.isFormValid || this.state.isSubmitting;
            
            // Update button text based on validation state
            const buttonContent = submitButton.querySelector('.btn-content');
            if (buttonContent && !this.state.isFormValid && this.state.touchedFields.size > 0) {
                const originalText = buttonContent.innerHTML;
                buttonContent.innerHTML = '<i class="fas fa-exclamation-triangle"></i>Please complete required fields';
                
                setTimeout(() => {
                    buttonContent.innerHTML = originalText;
                }, 3000);
            }
        }
    },

    // Handle payment method selection
    handlePaymentMethodSelect(methodElement) {
        // Remove active class from all methods
        document.querySelectorAll('.payment-method').forEach(method => {
            method.classList.remove('active');
        });
        
        // Add active class to selected method
        methodElement.classList.add('active');
        
        // Announce selection for screen readers
        this.announceToScreenReader(`${methodElement.textContent.trim()} payment method selected`);
    },

    // Handle form submission
    handleFormSubmit(event) {
        // Don't prevent default submission - let Stripe handle it
        // This is just for additional validation and UX enhancements
        
        if (this.state.isSubmitting) {
            event.preventDefault();
            return false;
        }

        // Validate all fields before submission
        let allValid = true;
        this.config.requiredFields.forEach(fieldName => {
            const field = document.querySelector(`[name="${fieldName}"]`);
            if (field) {
                this.state.touchedFields.add(fieldName);
                if (!this.validateField(field)) {
                    allValid = false;
                }
            }
        });

        if (!allValid) {
            event.preventDefault();
            this.showValidationSummary();
            return false;
        }

        // Set submitting state
        this.state.isSubmitting = true;
        this.showLoadingState();
        
        // Track completion
        this.trackFormProgress();
    },

    // Show validation summary for accessibility
    showValidationSummary() {
        const invalidFields = [];
        this.config.requiredFields.forEach(fieldName => {
            if (!this.state.validatedFields.has(fieldName)) {
                const field = document.querySelector(`[name="${fieldName}"]`);
                if (field) {
                    invalidFields.push(this.getFieldLabel(field));
                }
            }
        });

        if (invalidFields.length > 0) {
            const message = `Please complete the following required fields: ${invalidFields.join(', ')}`;
            this.showNotification(message, 'error');
            
            // Focus first invalid field
            const firstInvalidField = document.querySelector(`[name="${this.config.requiredFields.find(field => !this.state.validatedFields.has(field))}"]`);
            if (firstInvalidField) {
                firstInvalidField.focus();
                firstInvalidField.scrollIntoView({ behavior: 'smooth', block: 'center' });
            }
        }
    },

    // Initialize progress tracking
    initializeProgressTracking() {
        // Track form completion progress
        const steps = document.querySelectorAll(this.config.progressSteps);
        steps.forEach((step, index) => {
            step.addEventListener('click', () => {
                if (index < 2) { // Only allow navigation to previous steps
                    this.navigateToStep(index);
                }
            });
        });
    },

    // Track form progress and update UI
    trackFormProgress() {
        const completedFields = this.state.validatedFields.size;
        const totalFields = this.config.requiredFields.length;
        const progress = (completedFields / totalFields) * 100;
        
        // Update progress indicator if exists
        const progressBar = document.querySelector('.checkout-progress-bar');
        if (progressBar) {
            progressBar.style.width = `${progress}%`;
        }
        
        // Update step indicator
        this.updateProgressSteps(progress);
    },

    // Update progress steps visual state
    updateProgressSteps(progress) {
        const steps = document.querySelectorAll(this.config.progressSteps);
        if (progress >= 100) {
            // Mark checkout step as completed when form is valid
            steps.forEach((step, index) => {
                if (index === 1) { // Checkout step
                    step.classList.add('completed');
                }
            });
        }
    },

    // Initialize accessibility features
    initializeAccessibilityFeatures() {
        // Add ARIA live region for announcements
        const liveRegion = document.createElement('div');
        liveRegion.setAttribute('aria-live', 'polite');
        liveRegion.setAttribute('aria-atomic', 'true');
        liveRegion.className = 'sr-only';
        liveRegion.id = 'checkout-announcements';
        document.body.appendChild(liveRegion);

        // Enhance form sections with ARIA
        document.querySelectorAll('.form-section').forEach((section, index) => {
            section.setAttribute('aria-labelledby', `section-title-${index}`);
            const title = section.querySelector('.section-title');
            if (title) {
                title.id = `section-title-${index}`;
            }
        });

        // Add keyboard shortcuts help
        this.addKeyboardShortcutsHelp();
    },

    // Add keyboard shortcuts help dialog
    addKeyboardShortcutsHelp() {
        document.addEventListener('keydown', (e) => {
            if (e.ctrlKey && e.key === '?') {
                e.preventDefault();
                this.showKeyboardShortcutsDialog();
            }
        });
    },

    // Show keyboard shortcuts dialog
    showKeyboardShortcutsDialog() {
        const dialog = document.createElement('div');
        dialog.className = 'keyboard-shortcuts-dialog';
        dialog.innerHTML = `
            <div class="dialog-backdrop"></div>
            <div class="dialog-content" role="dialog" aria-labelledby="shortcuts-title" aria-modal="true">
                <h3 id="shortcuts-title">Keyboard Shortcuts</h3>
                <ul>
                    <li><kbd>Tab</kbd> - Navigate between form fields</li>
                    <li><kbd>Shift + Tab</kbd> - Navigate backwards</li>
                    <li><kbd>Enter</kbd> - Submit form or activate button</li>
                    <li><kbd>Escape</kbd> - Cancel or close dialogs</li>
                    <li><kbd>Ctrl + ?</kbd> - Show this help dialog</li>
                </ul>
                <button type="button" class="btn btn-secondary" onclick="this.closest('.keyboard-shortcuts-dialog').remove()">
                    Close
                </button>
            </div>
        `;
        
        document.body.appendChild(dialog);
        dialog.querySelector('button').focus();
        
        // Close on escape
        const closeHandler = (e) => {
            if (e.key === 'Escape') {
                dialog.remove();
                document.removeEventListener('keydown', closeHandler);
            }
        };
        document.addEventListener('keydown', closeHandler);
    },

    // Handle keyboard navigation
    handleKeyboardNavigation(event) {
        // Enhanced keyboard navigation for form
        if (event.key === 'Enter' && event.target.tagName === 'INPUT') {
            const form = event.target.closest('form');
            const inputs = Array.from(form.querySelectorAll('input, select, textarea'));
            const currentIndex = inputs.indexOf(event.target);
            
            if (currentIndex < inputs.length - 1) {
                event.preventDefault();
                inputs[currentIndex + 1].focus();
            }
        }
    },

    // Initialize loading states
    initializeLoadingStates() {
        // Add loading state management
        const submitButton = document.querySelector(this.config.submitButtonSelector);
        if (submitButton) {
            const originalContent = submitButton.innerHTML;
            
            // Store original content for restoration
            submitButton.dataset.originalContent = originalContent;
        }
    },

    // Show loading state
    showLoadingState() {
        const overlay = document.querySelector(this.config.loadingOverlaySelector);
        const submitButton = document.querySelector(this.config.submitButtonSelector);
        
        if (overlay) {
            overlay.classList.add('show');
        }
        
        if (submitButton) {
            submitButton.disabled = true;
            submitButton.innerHTML = `
                <span class="btn-content">
                    <i class="fas fa-spinner fa-spin"></i>
                    Processing...
                </span>
            `;
        }
        
        // Prevent navigation away
        window.addEventListener('beforeunload', this.handleBeforeUnload);
    },

    // Hide loading state
    hideLoadingState() {
        const overlay = document.querySelector(this.config.loadingOverlaySelector);
        const submitButton = document.querySelector(this.config.submitButtonSelector);
        
        if (overlay) {
            overlay.classList.remove('show');
        }
        
        if (submitButton && submitButton.dataset.originalContent) {
            submitButton.disabled = false;
            submitButton.innerHTML = submitButton.dataset.originalContent;
        }
        
        this.state.isSubmitting = false;
        window.removeEventListener('beforeunload', this.handleBeforeUnload);
    },

    // Handle before unload warning
    handleBeforeUnload(event) {
        const message = 'Your payment is being processed. Are you sure you want to leave?';
        event.returnValue = message;
        return message;
    },

    // Handle visibility change for security
    handleVisibilityChange() {
        if (document.hidden && this.state.isSubmitting) {
            // User switched tabs during payment processing
            console.warn('User navigated away during payment processing');
        }
    },

    // Initialize mobile-specific enhancements
    initializeMobileEnhancements() {
        if (window.innerWidth <= 768) {
            // Add mobile-specific behaviors
            this.enhanceFormForMobile();
            this.addMobileTouchFeedback();
        }
        
        // Listen for orientation changes
        window.addEventListener('orientationchange', () => {
            setTimeout(() => {
                this.adjustLayoutForOrientation();
            }, 100);
        });
    },

    // Enhance form for mobile devices
    enhanceFormForMobile() {
        // Add appropriate input types and attributes for mobile
        const fieldMappings = [
            { selector: '[name="email"]', autocomplete: 'email', inputmode: 'email' },
            { selector: '[name="phone_number"]', autocomplete: 'tel', inputmode: 'tel' },
            { selector: '[name="postcode"]', autocomplete: 'postal-code' },
            { selector: '[name="full_name"]', autocomplete: 'name' },
            { selector: '[name="street_address1"]', autocomplete: 'address-line1' },
            { selector: '[name="street_address2"]', autocomplete: 'address-line2' },
            { selector: '[name="town_or_city"]', autocomplete: 'address-level2' },
            { selector: '[name="county"]', autocomplete: 'address-level1' },
            { selector: '[name="country"]', autocomplete: 'country' }
        ];

        fieldMappings.forEach(field => {
            const element = document.querySelector(field.selector);
            if (element && !element.hasAttribute('autocomplete')) {
                element.setAttribute('autocomplete', field.autocomplete);
                if (field.inputmode) {
                    element.setAttribute('inputmode', field.inputmode);
                }
            }
        });
    },

    // Add mobile touch feedback
    addMobileTouchFeedback() {
        document.querySelectorAll('.btn, .payment-method').forEach(element => {
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

    // Adjust layout for orientation changes
    adjustLayoutForOrientation() {
        const stickyElements = document.querySelectorAll('.sticky-summary');
        stickyElements.forEach(element => {
            // Temporarily disable sticky positioning during orientation change
            element.style.position = 'static';
            setTimeout(() => {
                element.style.position = '';
            }, 300);
        });
    },

    // Show notification to user
    showNotification(message, type = 'info') {
        const notification = document.createElement('div');
        notification.className = `checkout-notification notification-${type}`;
        notification.innerHTML = `
            <div class="notification-content">
                <i class="fas fa-${type === 'error' ? 'exclamation-triangle' : 'info-circle'}"></i>
                <span>${message}</span>
                <button type="button" class="notification-close" aria-label="Close notification">
                    <i class="fas fa-times"></i>
                </button>
            </div>
        `;
        
        document.body.appendChild(notification);
        
        // Auto-remove after delay
        setTimeout(() => {
            notification.classList.add('notification-fade-out');
            setTimeout(() => {
                notification.remove();
            }, 300);
        }, 5000);
        
        // Close button functionality
        notification.querySelector('.notification-close').addEventListener('click', () => {
            notification.remove();
        });
        
        // Announce to screen readers
        this.announceToScreenReader(message);
    },

    // Announce message to screen readers
    announceToScreenReader(message) {
        const liveRegion = document.getElementById('checkout-announcements');
        if (liveRegion) {
            liveRegion.textContent = message;
            setTimeout(() => {
                liveRegion.textContent = '';
            }, 1000);
        }
    },

    // Inject notification styles
    injectNotificationStyles() {
        const styles = `
            .checkout-notification {
                position: fixed;
                top: 20px;
                right: 20px;
                z-index: 10000;
                max-width: 400px;
                background: white;
                border-radius: 8px;
                box-shadow: 0 8px 30px rgba(0,0,0,0.15);
                border-left: 4px solid #17a2b8;
                opacity: 0;
                transform: translateX(100%);
                transition: all 0.3s ease;
            }
            
            .checkout-notification.notification-error {
                border-left-color: #dc3545;
            }
            
            .checkout-notification.notification-success {
                border-left-color: #28a745;
            }
            
            .notification-content {
                padding: 1rem;
                display: flex;
                align-items: center;
                gap: 0.75rem;
            }
            
            .notification-content i:first-child {
                color: #17a2b8;
                font-size: 1.1rem;
            }
            
            .notification-error .notification-content i:first-child {
                color: #dc3545;
            }
            
            .notification-success .notification-content i:first-child {
                color: #28a745;
            }
            
            .notification-content span {
                flex: 1;
                font-size: 0.95rem;
                color: #2c3e50;
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
            
            .checkout-notification:not(.notification-fade-out) {
                opacity: 1;
                transform: translateX(0);
            }
            
            .notification-fade-out {
                opacity: 0;
                transform: translateX(100%);
            }
            
            /* Touch feedback for mobile */
            .touch-active {
                transform: scale(0.98);
                opacity: 0.8;
            }
            
            /* Field validation icons */
            .field-validation-icon {
                position: absolute;
                right: 1rem;
                top: 50%;
                transform: translateY(-50%);
                display: none;
                z-index: 2;
            }
            
            .field-validation-icon i {
                font-size: 1.1rem;
            }
            
            /* Keyboard shortcuts dialog */
            .keyboard-shortcuts-dialog {
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                z-index: 10001;
                display: flex;
                align-items: center;
                justify-content: center;
            }
            
            .keyboard-shortcuts-dialog .dialog-backdrop {
                position: absolute;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                background: rgba(0,0,0,0.6);
                backdrop-filter: blur(5px);
            }
            
            .keyboard-shortcuts-dialog .dialog-content {
                background: white;
                padding: 2rem;
                border-radius: 12px;
                max-width: 500px;
                width: 90%;
                z-index: 1;
                box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            }
            
            .keyboard-shortcuts-dialog h3 {
                margin-top: 0;
                color: #2c3e50;
            }
            
            .keyboard-shortcuts-dialog ul {
                list-style: none;
                padding: 0;
            }
            
            .keyboard-shortcuts-dialog li {
                padding: 0.5rem 0;
                border-bottom: 1px solid #f1f3f4;
            }
            
            .keyboard-shortcuts-dialog kbd {
                background: #f8f9fa;
                border: 1px solid #dee2e6;
                border-radius: 4px;
                padding: 0.25rem 0.5rem;
                font-family: monospace;
                font-size: 0.9rem;
            }
            
            @media (max-width: 768px) {
                .checkout-notification {
                    top: 10px;
                    right: 10px;
                    left: 10px;
                    max-width: none;
                }
                
                .field-validation-icon {
                    right: 0.75rem;
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
    CheckoutManager.injectNotificationStyles();
    CheckoutManager.init();
});

// Export for potential external use
window.CheckoutManager = CheckoutManager;
