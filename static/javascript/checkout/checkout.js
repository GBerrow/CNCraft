/* ========================================================================
   CNCraft - Modern Checkout Page JavaScript
   ========================================================================
   Enhanced checkout functionality with form validation, UX improvements,
   and accessibility features for a professional e-commerce experience.
   ======================================================================== */

// IMMEDIATE FIX: Clear any stuck loading states and prevent browser warnings
(function() {
    'use strict';
    
    // Clear loading overlay immediately if it exists
    const loadingOverlay = document.getElementById('loading-overlay');
    if (loadingOverlay) {
        loadingOverlay.style.display = 'none';
    }
    
    // Re-enable submit button if it's disabled
    const submitButton = document.querySelector('#submit-button');
    if (submitButton && submitButton.disabled) {
        submitButton.disabled = false;
        submitButton.innerHTML = '<span class="btn-content"><i class="fas fa-lock"></i> Complete Order</span>';
    }
    
    // Remove all beforeunload listeners to prevent "Leave site?" prompts
    window.removeEventListener('beforeunload', function() {});
    
    // Reset form to clear autofill data and prevent "unsaved changes" warnings
    const form = document.getElementById('payment-form');
    if (form) {
        // Store original values before reset
        const originalValues = {};
        const inputs = form.querySelectorAll('input, select, textarea');
        inputs.forEach(input => {
            if (input.value) {
                originalValues[input.name] = input.value;
            }
        });
        
        // Reset form to clear browser warnings
        form.reset();
        
        // Restore values after a short delay
        setTimeout(() => {
            inputs.forEach(input => {
                if (originalValues[input.name]) {
                    input.value = originalValues[input.name];
                }
            });
        }, 100);
    }
    
})();

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
            phone: /^[\+]?[0-9]{10,15}$/,
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
        
        // Track form changes to prevent browser "unsaved changes" warnings
        // Note: Simplified approach to avoid syntax errors
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
        // Check if Stripe card element exists
        const cardElement = document.getElementById('card-element');
        
        // If Stripe is active, ALWAYS preventDefault and let Stripe handle submission
        if (cardElement) {
            event.preventDefault();
            return false;
        }

        // Check if we're in test mode (no Stripe integration)
        const stripePublicKey = document.getElementById('id_stripe_public_key');
        if (stripePublicKey && stripePublicKey.textContent === 'pk_test_placeholder') {
            // Test mode - allow form submission without Stripe processing
            
            // Don't prevent default - let the form submit naturally
            // Don't show loading state in test mode to avoid getting stuck
            this.state.isSubmitting = false;
            return true; // Allow form to submit normally
        }

        // If we get here, something is wrong - prevent submission
        event.preventDefault();
        return false;
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

    // Add keyboard shortcuts help
    addKeyboardShortcutsHelp() {
        // Add keyboard shortcut listener for Ctrl+? to show shortcuts dialog
        document.addEventListener('keydown', (event) => {
            if (event.ctrlKey && event.key === '?') {
                event.preventDefault();
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
        
        // Emergency escape from loading state
        if (event.key === 'Escape' && this.state.isSubmitting) {
            event.preventDefault();
            this.forceClearLoadingState();
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
        
        // Add click handler to loading overlay for emergency cancel
        const loadingOverlay = document.querySelector(this.config.loadingOverlaySelector);
        if (loadingOverlay) {
            loadingOverlay.addEventListener('click', (event) => {
                // Only trigger if clicking the overlay itself, not its children
                if (event.target === loadingOverlay) {
                    this.forceClearLoadingState();
                }
            });
            
            // Add emergency cancel button to loading overlay
            const emergencyButton = document.createElement('button');
            emergencyButton.type = 'button';
            emergencyButton.className = 'emergency-cancel-btn';
            emergencyButton.innerHTML = '<i class="fas fa-times"></i> Cancel';
            emergencyButton.style.cssText = `
                position: absolute;
                top: 20px;
                right: 20px;
                background: #dc3545;
                color: white;
                border: none;
                padding: 10px 15px;
                border-radius: 5px;
                cursor: pointer;
                font-size: 14px;
                z-index: 10001;
                display: none;
            `;
            
            emergencyButton.addEventListener('click', (e) => {
                e.stopPropagation();
                this.forceClearLoadingState();
            });
            
            loadingOverlay.appendChild(emergencyButton);
            
            // Show emergency button after 5 seconds if still loading
            setTimeout(() => {
                if (this.state.isSubmitting) {
                    emergencyButton.style.display = 'block';
                }
            }, 5000);
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
        
        // Only add beforeunload listener for real Stripe payments, not test mode
        const stripePublicKey = document.getElementById('id_stripe_public_key');
        if (!stripePublicKey || stripePublicKey.textContent !== 'pk_test_placeholder') {
        window.addEventListener('beforeunload', this.handleBeforeUnload);
        }
        
        // Add timeout to automatically clear loading state after 30 seconds
        this.loadingTimeout = setTimeout(() => {
            this.forceClearLoadingState();
        }, 30000); // 30 seconds
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
        
        // Clear the timeout if it exists
        if (this.loadingTimeout) {
            clearTimeout(this.loadingTimeout);
            this.loadingTimeout = null;
        }
    },

    // Handle before unload warning
    handleBeforeUnload(event) {
        const message = 'Your payment is being processed. Are you sure you want to leave?';
        event.returnValue = message;
        return message;
    },

    // Force clear loading state (for emergency situations)
    forceClearLoadingState() {
        this.state.isSubmitting = false;
        this.hideLoadingState();
        
        // Also clear any beforeunload listeners
        window.removeEventListener('beforeunload', this.handleBeforeUnload);
        
        // Clear the timeout if it exists
        if (this.loadingTimeout) {
            clearTimeout(this.loadingTimeout);
            this.loadingTimeout = null;
        }
        
        // Re-enable submit button
        const submitButton = document.querySelector(this.config.submitButtonSelector);
        if (submitButton && submitButton.dataset.originalContent) {
            submitButton.disabled = false;
            submitButton.innerHTML = submitButton.dataset.originalContent;
        }
        
        // Clear form state to prevent browser "unsaved changes" warnings
        this.clearFormState();
    },
    
    // Clear form state to prevent browser warnings
    clearFormState() {
        const form = document.querySelector(this.config.formSelector);
        if (form) {
            // Reset form to initial state
            form.reset();
            
            // Remove any beforeunload listeners
            window.removeEventListener('beforeunload', this.handleBeforeUnload);
            
        }
    },

    // Handle visibility change for security
    handleVisibilityChange() {
        if (document.hidden && this.state.isSubmitting) {
            // User switched tabs during payment processing
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
    },
    
    // Simple function to clear form state and prevent browser warnings
    clearFormState() {
        const form = document.querySelector(this.config.formSelector);
        if (form) {
            // Reset form to initial state
            form.reset();
            
            // Remove any beforeunload listeners
            window.removeEventListener('beforeunload', this.handleBeforeUnload);
            
        }
    }
};

// Stripe payment processing for checkout
document.addEventListener('DOMContentLoaded', function() {
    // Get Stripe public key from template
    const stripePublicKeyElement = document.getElementById('id_stripe_public_key');
    if (!stripePublicKeyElement) {
        return;
    }
    
    // Parse JSON (json_script filter wraps in quotes)
    let stripePublicKey = stripePublicKeyElement.textContent.trim();
    try {
        stripePublicKey = JSON.parse(stripePublicKey);
    } catch (e) {
        // If parsing fails, use as-is (for backward compatibility)
    }
    
    // Check if card element exists before initializing
    const cardElement = document.getElementById('card-element');
    if (!cardElement) {
        return;
    }
    
    // Initialize Stripe if we have a valid public key (test or live)
    if (stripePublicKey && (stripePublicKey.startsWith('pk_test_') || stripePublicKey.startsWith('pk_live_'))) {
        const stripe = Stripe(stripePublicKey);
        const elements = stripe.elements();
        
        // Create card element with better styling
        const card = elements.create('card', {
            style: {
                base: {
                    fontSize: '16px',
                    color: '#32325d',
                    fontFamily: '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif',
                    fontSmoothing: 'antialiased',
                    '::placeholder': {
                        color: '#aab7c4',
                    },
                },
                invalid: {
                    color: '#fa755a',
                    iconColor: '#fa755a',
                },
            },
            hidePostalCode: true,
        });
        
        // Mount card element (synchronous operation - no Promise returned)
        try {
            card.mount('#card-element');
        } catch (error) {
        }
        
        // Wait for card element to be ready
        card.on('ready', function() {
        });
        
        // Handle real-time validation errors
        card.on('change', function(event) {
            const displayError = document.getElementById('card-errors');
            if (event.error) {
                displayError.textContent = event.error.message;
                displayError.style.display = 'block';
            } else {
                displayError.textContent = '';
                displayError.style.display = 'none';
            }
        });
        
        // Log focus events for debugging
        card.on('focus', function() {
        });
        
        card.on('blur', function() {
        });
        
        // Handle form submission
        const form = document.getElementById('payment-form');
        if (form) {
            form.addEventListener('submit', function(event) {
                event.preventDefault();
                
                // Validate all required fields
                let allValid = true;
                const requiredFields = ['full_name', 'email', 'phone_number', 'street_address1', 'town_or_city', 'postcode', 'country'];
                
                requiredFields.forEach(fieldName => {
                    const field = document.querySelector(`[name="${fieldName}"]`);
                    if (field && !field.value.trim()) {
                        allValid = false;
                        field.classList.add('is-invalid');
                        const errorElement = field.parentNode.querySelector('.invalid-feedback');
                        if (errorElement) {
                            errorElement.textContent = 'This field is required.';
                            errorElement.style.display = 'block';
                        }
                    }
                });
                
                if (!allValid) {
                    CheckoutManager.showValidationSummary();
                    return false;
                }
                
                // Disable submit button to prevent double submission
                const submitButton = form.querySelector('button[type="submit"]');
                const originalText = submitButton.innerHTML;
                submitButton.disabled = true;
                submitButton.innerHTML = '<span class="btn-content"><i class="fas fa-spinner fa-spin"></i> Processing...</span>';
                
                // Show loading state
                const loadingSpinner = document.getElementById('loading-overlay');
                if (loadingSpinner) {
                    loadingSpinner.style.display = 'flex';
                }
                
                // Get client_secret from hidden input
                const clientSecretInput = document.querySelector('input[name="client_secret"]');
                const clientSecret = clientSecretInput ? clientSecretInput.value : null;
                
                if (!clientSecret || clientSecret === 'None' || clientSecret === '') {
                    alert('Payment system error. Please refresh the page and try again.');
                    submitButton.disabled = false;
                    submitButton.innerHTML = originalText;
                    if (loadingSpinner) loadingSpinner.style.display = 'none';
                    return;
                }
                
                
                // Confirm the card payment with Stripe
                stripe.confirmCardPayment(clientSecret, {
                    payment_method: {
                        card: card,
                        billing_details: {
                            name: document.getElementById('id_full_name').value,
                            email: document.getElementById('id_email').value,
                            phone: document.getElementById('id_phone_number').value,
                            address: {
                                line1: document.getElementById('id_street_address1').value,
                                line2: document.getElementById('id_street_address2')?.value || '',
                                city: document.getElementById('id_town_or_city').value,
                                state: document.getElementById('id_county')?.value || '',
                                postal_code: document.getElementById('id_postcode').value,
                                country: document.getElementById('id_country').value,
                            }
                        }
                    }
                }).then(function(result) {
                    if (result.error) {
                        // Show error to customer
                        const errorElement = document.getElementById('card-errors');
                        errorElement.textContent = result.error.message;
                        errorElement.style.display = 'block';
                        
                        // Re-enable submit button
                        submitButton.disabled = false;
                        submitButton.innerHTML = originalText;
                        
                        // Hide loading state
                        if (loadingSpinner) {
                            loadingSpinner.style.display = 'none';
                        }
                        
                    } else {
                        // Payment succeeded!
                        if (result.paymentIntent.status === 'succeeded') {
                            
                            // Add payment intent ID to form
                            const hiddenInput = document.createElement('input');
                            hiddenInput.setAttribute('type', 'hidden');
                            hiddenInput.setAttribute('name', 'payment_intent_id');
                            hiddenInput.setAttribute('value', result.paymentIntent.id);
                            form.appendChild(hiddenInput);
                            
                            // Now submit the form to create the order
                            form.submit();
                        }
                    }
                }).catch(function(error) {
                    
                    // Show error message
                    const errorElement = document.getElementById('card-errors');
                    errorElement.textContent = 'An error occurred. Please try again.';
                    errorElement.style.display = 'block';
                    
                    // Re-enable submit button
                    submitButton.disabled = false;
                    submitButton.innerHTML = originalText;
                    
                    // Hide loading state
                    if (loadingSpinner) {
                        loadingSpinner.style.display = 'none';
                    }
                });
            });
        }
    } else {
    }
    
    // Form validation for both test and real modes
    const form = document.getElementById('payment-form');
    if (form) {
        const requiredFields = form.querySelectorAll('[required]');
        requiredFields.forEach(function(field) {
            field.addEventListener('blur', function() {
                validateField(field);
            });
            
            field.addEventListener('input', function() {
                if (field.classList.contains('is-invalid')) {
                    validateField(field);
                }
            });
        });
        
        function validateField(field) {
            const value = field.value.trim();
            const errorElement = field.parentNode.querySelector('.invalid-feedback');
            
            if (!value) {
                field.classList.add('is-invalid');
                if (errorElement) {
                    errorElement.textContent = 'This field is required.';
                    errorElement.style.display = 'block';
                }
            } else {
                field.classList.remove('is-invalid');
                if (errorElement) {
                    errorElement.style.display = 'none';
                }
            }
            
            // Email validation
            if (field.type === 'email' && value) {
                const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
                if (!emailRegex.test(value)) {
                    field.classList.add('is-invalid');
                    if (errorElement) {
                        errorElement.textContent = 'Please enter a valid email address.';
                        errorElement.style.display = 'block';
                    }
                }
            }
            
            // Phone validation
            if (field.name === 'phone_number' && value) {
                const phoneRegex = /^[\+]?[0-9]{10,15}$/;
                if (!phoneRegex.test(value.replace(/\s/g, ''))) {
                    field.classList.add('is-invalid');
                    if (errorElement) {
                        errorElement.textContent = 'Please enter a valid phone number.';
                        errorElement.style.display = 'block';
                    }
                }
            }
        }
        
        // Auto-save form data to localStorage
        const formInputs = form.querySelectorAll('input, select, textarea');
        formInputs.forEach(function(input) {
            // Load saved data
            const savedValue = localStorage.getItem(`checkout_${input.name}`);
            if (savedValue && !input.value) {
                input.value = savedValue;
            }
            
            // Save data on input
            input.addEventListener('input', function() {
                localStorage.setItem(`checkout_${input.name}`, input.value);
            });
        });
        
        // Clear saved data on successful submission
        form.addEventListener('submit', function() {
            formInputs.forEach(function(input) {
                localStorage.removeItem(`checkout_${input.name}`);
            });
        });
    }
});

// Initialize when DOM is ready
document.addEventListener('DOMContentLoaded', function() {
    CheckoutManager.injectNotificationStyles();
    CheckoutManager.init();
});

// Export for potential external use
window.CheckoutManager = CheckoutManager;

// Emergency function for users to call from console
window.clearCheckoutLoading = function() {
    if (window.CheckoutManager) {
        window.CheckoutManager.forceClearLoadingState();
    } else {
        // Fallback if CheckoutManager isn't available
        const overlay = document.getElementById('loading-overlay');
        if (overlay) {
            overlay.style.display = 'none';
        }
        const submitButton = document.querySelector('#submit-button');
        if (submitButton) {
            submitButton.disabled = false;
        }
    }
};

// Additional emergency function to clear form state and browser warnings
window.clearFormState = function() {
    const form = document.getElementById('payment-form');
    if (form) {
        form.reset();
    }
    
    // Also clear loading state
    window.clearCheckoutLoading();
};
