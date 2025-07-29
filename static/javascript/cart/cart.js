/**
 * CNCraft - Enhanced Cart Management JavaScript
 * ====================================================
 * Modern, accessible cart functionality with real-time updates,
 * smooth animations, and comprehensive error handling.
 * 
 * Sections
 * 1. CART MANAGER - MAIN OBJECT
 * 2. CONFIGURATION & STATE
 * 3. INITIALIZATION
 * 4. EVENT LISTENERS & HANDLERS
 * 5. QUANTITY CONTROL HANDLERS
 * 6. ITEM REMOVAL HANDLERS
 * 7. KEYBOARD & ACCESSIBILITY HANDLERS
 * 8. QUANTITY VALIDATION & CONTROLS
 * 9. PRICE CALCULATION & UPDATES
 * 10. AJAX CART OPERATIONS
 * 11. SUCCESS & ERROR HANDLERS 
 * 12. UI STATE MANAGEMENT 
 * 13. UTILITY FUNCTIONS 
 * 14. NOTIFICATIONS & DIALOGS 
 * 15. LOCAL STORAGE MANAGEMENT 
 * 16. ACCESSIBILITY FEATURES 
 * 17. ANIMATION INITIALIZATION 
 * 18. PAGE VISIBILITY HANDLING 
 * 19. INITIALIZATION & GLOBAL EXPOSURE 
 */

'use strict';

// ============================================================================
// CART MANAGER - MAIN OBJECT
// ============================================================================

const CartManager = {
    
    // ========================================================================
    // CONFIGURATION & STATE
    // ========================================================================
    
    // Configuration
    config: {
        debounceDelay: 500,
        animationDuration: 300,
        maxQuantity: 99,
        minQuantity: 1,
        endpoints: {
            adjust: '/cart/adjust/',
            remove: '/cart/remove/',
            view: '/cart/'
        }
    },

    // State management
    state: {
        isLoading: false,
        updateQueue: new Map(),
        cartData: {
            items: [],
            total: 0,
            delivery: 0,
            grandTotal: 0,
            itemCount: 0
        }
    },

    // ========================================================================
    // INITIALIZATION
    // ========================================================================

    // Initialization
    init() {
        this.bindEventListeners();
        this.initializeQuantityControls();
        this.loadCartFromStorage();
        this.initializeAccessibility();
        this.initializeAnimations();
        console.log('Cart Manager initialized successfully');
    },

    // ========================================================================
    // EVENT LISTENERS & HANDLERS
    // ========================================================================

    // Event listeners
    bindEventListeners() {
        // Quantity control buttons
        $(document).on('click', '.quantity-increase', this.handleQuantityIncrease.bind(this));
        $(document).on('click', '.quantity-decrease', this.handleQuantityDecrease.bind(this));
        
        // Quantity input changes
        $(document).on('input', '.quantity-input', this.handleQuantityInput.bind(this));
        $(document).on('blur', '.quantity-input', this.handleQuantityBlur.bind(this));
        
        // Form submissions
        $(document).on('submit', '.quantity-form', this.handleQuantityFormSubmit.bind(this));
        
        // Remove buttons
        $(document).on('click', '.btn-remove', this.handleRemoveItem.bind(this));
        
        // Keyboard navigation
        $(document).on('keydown', '.quantity-controls', this.handleKeyboardNavigation.bind(this));
        
        // Page visibility changes
        $(document).on('visibilitychange', this.handleVisibilityChange.bind(this));
        
        // Window unload (save state)
        $(window).on('beforeunload', this.saveCartToStorage.bind(this));
    },

    // ========================================================================
    // QUANTITY CONTROL HANDLERS
    // ========================================================================

    // Quantity control handlers
    handleQuantityIncrease(event) {
        event.preventDefault();
        event.stopPropagation();
        const $button = $(event.currentTarget);
        const productId = $button.data('product-id');
        const $input = $(`.quantity-input[data-product-id="${productId}"]`);
        const currentValue = parseInt($input.val()) || this.config.minQuantity;
        const newValue = Math.min(currentValue + 1, this.config.maxQuantity);
        
        if (newValue !== currentValue) {
            $input.val(newValue);
            this.validateQuantityControls(productId);
            this.queuePriceUpdate(productId, newValue);
        }
    },

    handleQuantityDecrease(event) {
        event.preventDefault();
        event.stopPropagation();
        const $button = $(event.currentTarget);
        const productId = $button.data('product-id');
        const $input = $(`.quantity-input[data-product-id="${productId}"]`);
        const currentValue = parseInt($input.val()) || this.config.minQuantity;
        const newValue = Math.max(currentValue - 1, this.config.minQuantity);
        
        if (newValue !== currentValue) {
            $input.val(newValue);
            this.validateQuantityControls(productId);
            this.queuePriceUpdate(productId, newValue);
        }
    },

    handleQuantityInput(event) {
        const $input = $(event.currentTarget);
        const productId = $input.data('product-id');
        let value = parseInt($input.val()) || this.config.minQuantity;
        
        // Validate range
        value = Math.max(this.config.minQuantity, Math.min(value, this.config.maxQuantity));
        
        // Update input if value was corrected
        if (parseInt($input.val()) !== value) {
            $input.val(value);
        }
        
        this.validateQuantityControls(productId);
        this.queuePriceUpdate(productId, value);
    },

    handleQuantityBlur(event) {
        const $input = $(event.currentTarget);
        const productId = $input.data('product-id');
        const value = parseInt($input.val()) || this.config.minQuantity;
        
        // Ensure valid value
        const validValue = Math.max(this.config.minQuantity, Math.min(value, this.config.maxQuantity));
        $input.val(validValue);
        
        this.validateQuantityControls(productId);
        this.processPriceUpdate(productId, validValue);
    },

    handleQuantityFormSubmit(event) {
        event.preventDefault();
        const $form = $(event.currentTarget);
        const productId = $form.find('.quantity-input').data('product-id');
        const quantity = parseInt($form.find('.quantity-input').val());
        
        this.updateCartItem(productId, quantity);
    },

    // ========================================================================
    // ITEM REMOVAL HANDLERS
    // ========================================================================

    // Remove item handler
    handleRemoveItem(event) {
        event.preventDefault();
        const $button = $(event.currentTarget);
        const productId = $button.data('product-id');
        
        // Show confirmation dialog
        this.showConfirmationDialog(
            'Remove Item',
            'Are you sure you want to remove this item from your cart?',
            () => this.removeCartItem(productId)
        );
    },

    // ========================================================================
    // KEYBOARD & ACCESSIBILITY HANDLERS
    // ========================================================================

    // Keyboard navigation
    handleKeyboardNavigation(event) {
        const $controls = $(event.currentTarget);
        const $input = $controls.find('.quantity-input');
        const productId = $input.data('product-id');
        
        switch (event.key) {
            case 'ArrowUp':
            case '+':
                event.preventDefault();
                $controls.find('.quantity-increase').click();
                break;
            case 'ArrowDown':
            case '-':
                event.preventDefault();
                $controls.find('.quantity-decrease').click();
                break;
            case 'Delete':
            case 'Backspace':
                if (event.ctrlKey) {
                    event.preventDefault();
                    this.removeCartItem(productId);
                }
                break;
        }
    },

    // ========================================================================
    // QUANTITY VALIDATION & CONTROLS
    // ========================================================================

    // Quantity control validation
    validateQuantityControls(productId) {
        const $input = $(`.quantity-input[data-product-id="${productId}"]`);
        const $decreaseBtn = $(`.quantity-decrease[data-product-id="${productId}"]`);
        const $increaseBtn = $(`.quantity-increase[data-product-id="${productId}"]`);
        const value = parseInt($input.val()) || this.config.minQuantity;
        
        // Update button states
        $decreaseBtn.prop('disabled', value <= this.config.minQuantity);
        $increaseBtn.prop('disabled', value >= this.config.maxQuantity);
        
        // Add visual feedback
        $decreaseBtn.toggleClass('disabled', value <= this.config.minQuantity);
        $increaseBtn.toggleClass('disabled', value >= this.config.maxQuantity);
    },

    // Initialize all quantity controls
    initializeQuantityControls() {
        $('.quantity-input').each((index, element) => {
            const $input = $(element);
            const productId = $input.data('product-id');
            this.validateQuantityControls(productId);
        });
    },

    // ========================================================================
    // PRICE CALCULATION & UPDATES
    // ========================================================================

    // Price update management
    queuePriceUpdate(productId, quantity) {
        // Clear existing timeout for this product
        if (this.state.updateQueue.has(productId)) {
            clearTimeout(this.state.updateQueue.get(productId));
        }
        
        // Queue new update
        const timeoutId = setTimeout(() => {
            this.processPriceUpdate(productId, quantity);
            this.state.updateQueue.delete(productId);
        }, this.config.debounceDelay);
        
        this.state.updateQueue.set(productId, timeoutId);
    },

    processPriceUpdate(productId, quantity) {
        const $cartItem = $(`.cart-item[data-product-id="${productId}"]`);
        const price = this.getProductPrice(productId);
        
        if (price && quantity > 0) {
            const subtotal = price * quantity;
            this.updateSubtotal(productId, subtotal);
            this.updateCartTotals();
            this.animateValueChange($cartItem.find('.subtotal-value'));
        }
    },

    // Get product price from DOM
    getProductPrice(productId) {
        const $priceElement = $(`.cart-item[data-product-id="${productId}"] .price-value`);
        const priceText = $priceElement.text().replace(/[$,\s]/g, '');
        return parseFloat(priceText) || 0;
    },

    // Update subtotal display
    updateSubtotal(productId, subtotal) {
        const $subtotalElement = $(`.subtotal-value[data-product-id="${productId}"]`);
        const formattedSubtotal = `$${subtotal.toFixed(2)}`;
        
        if ($subtotalElement.text() !== formattedSubtotal) {
            $subtotalElement.text(formattedSubtotal);
        }
    },

    // Update cart totals
    updateCartTotals() {
        let total = 0;
        let itemCount = 0;
        
        $('.cart-item').each((index, element) => {
            const $item = $(element);
            const $subtotalElement = $item.find('.subtotal-value');
            const subtotalText = $subtotalElement.text().replace(/[$,\s]/g, '');
            const subtotal = parseFloat(subtotalText) || 0;
            
            const $quantityInput = $item.find('.quantity-input');
            const quantity = parseInt($quantityInput.val()) || 0;
            
            total += subtotal;
            itemCount += quantity;
        });
        
        // Update cart subtotal
        $('#cart-subtotal').text(`$${total.toFixed(2)}`);
        
        // Update delivery cost
        const deliveryThreshold = parseFloat($('[data-bs-toggle="tooltip"]').attr('title').match(/\$([0-9,]+)/)?.[1]?.replace(',', '')) || 250;
        const delivery = total >= deliveryThreshold ? 0 : total * 0.1;
        $('#cart-delivery').html(delivery > 0 ? `$${delivery.toFixed(2)}` : '<span class="text-success">FREE</span>');
        
        // Update grand total
        const grandTotal = total + delivery;
        $('#cart-total').text(`$${grandTotal.toFixed(2)}`);
        
        // Update free shipping progress
        this.updateFreeShippingProgress(total, deliveryThreshold);
        
        // Store updated data
        this.state.cartData = { total, delivery, grandTotal, itemCount };
    },

    // Update free shipping progress
    updateFreeShippingProgress(total, threshold) {
        const $progressBar = $('.progress-bar');
        const $freeShippingNotice = $('.free-shipping-notice');
        
        if (total >= threshold) {
            $freeShippingNotice.fadeOut();
        } else {
            const progress = (total / threshold) * 100;
            const remaining = threshold - total;
            
            $progressBar.css('width', `${progress}%`).attr('aria-valuenow', total);
            $freeShippingNotice.find('strong').text(`Add $${remaining.toFixed(2)} more for FREE shipping!`);
            $freeShippingNotice.fadeIn();
        }
    },

    // ========================================================================
    // AJAX OPERATIONS
    // ========================================================================

    // AJAX Operations
    updateCartItem(productId, quantity) {
        if (this.state.isLoading) return;
        
        this.setLoadingState(true);
        const $cartItem = $(`.cart-item[data-product-id="${productId}"]`);
        $cartItem.addClass('updating');
        
        $.ajax({
            url: `${this.config.endpoints.adjust}${productId}/`,
            type: 'POST',
            data: {
                quantity: quantity,
                csrfmiddlewaretoken: $('[name=csrfmiddlewaretoken]').val()
            },
            success: (response) => {
                this.handleUpdateSuccess(productId, quantity);
                this.showNotification('Cart updated successfully', 'success');
            },
            error: (xhr) => {
                this.handleUpdateError(productId, xhr);
                this.showNotification('Failed to update cart', 'error');
            },
            complete: () => {
                this.setLoadingState(false);
                $cartItem.removeClass('updating');
            }
        });
    },

    removeCartItem(productId) {
        if (this.state.isLoading) return;
        
        this.setLoadingState(true);
        const $cartItem = $(`.cart-item[data-product-id="${productId}"]`);
        
        $.ajax({
            url: `${this.config.endpoints.remove}${productId}/`,
            type: 'POST',
            data: {
                csrfmiddlewaretoken: $('[name=csrfmiddlewaretoken]').val()
            },
            success: () => {
                this.handleRemoveSuccess(productId);
                this.showNotification('Item removed from cart', 'success');
            },
            error: (xhr) => {
                this.handleRemoveError(productId, xhr);
                this.showNotification('Failed to remove item', 'error');
            },
            complete: () => {
                this.setLoadingState(false);
            }
        });
    },

    // ========================================================================
    // SUCCESS & ERROR HANDLERS
    // ========================================================================

    // Success/Error handlers
    handleUpdateSuccess(productId, quantity) {
        this.updateCartTotals();
        this.saveCartToStorage();
        this.validateQuantityControls(productId);
    },

    handleUpdateError(productId, xhr) {
        // Revert quantity input to original value
        const $input = $(`.quantity-input[data-product-id="${productId}"]`);
        const originalValue = $input.data('original-value') || this.config.minQuantity;
        $input.val(originalValue);
        this.validateQuantityControls(productId);
        
        console.error('Cart update failed:', xhr.responseText);
    },

    handleRemoveSuccess(productId) {
        const $cartItem = $(`.cart-item[data-product-id="${productId}"]`);
        
        // Animate removal
        $cartItem.addClass('removing');
        setTimeout(() => {
            $cartItem.slideUp(this.config.animationDuration, () => {
                $cartItem.remove();
                this.updateCartTotals();
                this.checkEmptyCart();
                this.saveCartToStorage();
            });
        }, 100);
    },

    handleRemoveError(productId, xhr) {
        console.error('Cart item removal failed:', xhr.responseText);
    },

    // ========================================================================
    // UI STATE MANAGEMENT
    // ========================================================================

    // UI State Management
    setLoadingState(isLoading) {
        this.state.isLoading = isLoading;
        const $overlay = $('#loadingOverlay');
        
        if (isLoading) {
            $overlay.addClass('show');
            $('body').addClass('loading');
        } else {
            $overlay.removeClass('show');
            $('body').removeClass('loading');
        }
    },

    // Check if cart is empty and show appropriate state
    checkEmptyCart() {
        if ($('.cart-item').length === 0) {
            // Redirect to empty cart state or reload page
            window.location.reload();
        }
    },

    // ========================================================================
    // UTILITY FUNCTIONS
    // ========================================================================

    // Utility functions
    updateQuantityInput($input, value) {
        // Store original value for error recovery
        if (!$input.data('original-value')) {
            $input.data('original-value', $input.val());
        }
        
        $input.val(value);
        
        // Reset original value after successful update
        setTimeout(() => {
            $input.data('original-value', value);
        }, 1000);
    },

    animateValueChange($element) {
        $element.addClass('value-updated');
        setTimeout(() => {
            $element.removeClass('value-updated');
        }, this.config.animationDuration);
    },

    // ========================================================================
    // NOTIFICATIONS & DIALOGS
    // ========================================================================

    // Notifications
    showNotification(message, type = 'info') {
        // Create notification element
        const $notification = $(`
            <div class="cart-notification cart-notification-${type}">
                <div class="notification-content">
                    <i class="fas fa-${this.getNotificationIcon(type)}"></i>
                    <span>${message}</span>
                </div>
            </div>
        `);
        
        // Add to page
        $('body').append($notification);
        
        // Animate in
        setTimeout(() => $notification.addClass('show'), 100);
        
        // Auto remove
        setTimeout(() => {
            $notification.removeClass('show');
            setTimeout(() => $notification.remove(), this.config.animationDuration);
        }, 3000);
    },

    getNotificationIcon(type) {
        const icons = {
            success: 'check-circle',
            error: 'exclamation-triangle',
            warning: 'exclamation-circle',
            info: 'info-circle'
        };
        return icons[type] || icons.info;
    },

    // Confirmation dialog
    showConfirmationDialog(title, message, onConfirm) {
        const $dialog = $(`
            <div class="cart-confirmation-dialog">
                <div class="dialog-backdrop"></div>
                <div class="dialog-content">
                    <h4>${title}</h4>
                    <p>${message}</p>
                    <div class="dialog-actions">
                        <button type="button" class="btn-cancel">Cancel</button>
                        <button type="button" class="btn-confirm">Confirm</button>
                    </div>
                </div>
            </div>
        `);
        
        $('body').append($dialog);
        
        // Event handlers
        $dialog.find('.btn-cancel, .dialog-backdrop').on('click', () => {
            $dialog.removeClass('show');
            setTimeout(() => $dialog.remove(), this.config.animationDuration);
        });
        
        $dialog.find('.btn-confirm').on('click', () => {
            onConfirm();
            $dialog.removeClass('show');
            setTimeout(() => $dialog.remove(), this.config.animationDuration);
        });
        
        // Show dialog
        setTimeout(() => $dialog.addClass('show'), 100);
    },

    // ========================================================================
    // LOCAL STORAGE MANAGEMENT
    // ========================================================================

    // Local storage management
    saveCartToStorage() {
        try {
            const cartState = {
                data: this.state.cartData,
                timestamp: Date.now()
            };
            localStorage.setItem('cncraft_cart', JSON.stringify(cartState));
        } catch (error) {
            console.warn('Failed to save cart to storage:', error);
        }
    },

    loadCartFromStorage() {
        try {
            const stored = localStorage.getItem('cncraft_cart');
            if (stored) {
                const cartState = JSON.parse(stored);
                const age = Date.now() - cartState.timestamp;
                
                // Only use stored data if less than 1 hour old
                if (age < 3600000) {
                    this.state.cartData = cartState.data;
                }
            }
        } catch (error) {
            console.warn('Failed to load cart from storage:', error);
        }
    },

    // ========================================================================
    // ACCESSIBILITY FEATURES
    // ========================================================================

    // Accessibility enhancements
    initializeAccessibility() {
        // Add ARIA live regions for screen readers
        if (!$('#cart-live-region').length) {
            $('body').append('<div id="cart-live-region" aria-live="polite" aria-atomic="true" class="sr-only"></div>');
        }
        
        // Enhance quantity controls with better ARIA labels
        $('.quantity-input').each((index, element) => {
            const $input = $(element);
            const productName = $input.closest('.cart-item').find('.product-name').text().trim();
            $input.attr('aria-label', `Quantity for ${productName}`);
        });
        
        // Add keyboard shortcuts info
        this.addKeyboardShortcutsInfo();
    },

    addKeyboardShortcutsInfo() {
        // Add a help button for keyboard shortcuts
        if (!$('.keyboard-help-btn').length) {
            const $helpBtn = $(`
                <button type="button" class="keyboard-help-btn" aria-label="View keyboard shortcuts">
                    <i class="fas fa-keyboard"></i>
                </button>
            `);
            
            $helpBtn.on('click', this.showKeyboardShortcuts.bind(this));
            $('.cart-header').append($helpBtn);
        }
    },

    showKeyboardShortcuts() {
        const shortcuts = [
            { key: '↑ / +', action: 'Increase quantity' },
            { key: '↓ / -', action: 'Decrease quantity' },
            { key: 'Ctrl + Delete', action: 'Remove item' },
            { key: 'Tab', action: 'Navigate between controls' },
            { key: 'Enter', action: 'Update quantity' }
        ];
        
        const shortcutList = shortcuts.map(s => `<li><kbd>${s.key}</kbd> - ${s.action}</li>`).join('');
        
        this.showConfirmationDialog(
            'Keyboard Shortcuts',
            `<ul class="shortcuts-list">${shortcutList}</ul>`,
            () => {}
        );
    },

    // ========================================================================
    // ANIMATION INITIALIZATION
    // ========================================================================

    // Animation initialization
    initializeAnimations() {
        // Add CSS classes for animations
        $('<style>').text(`
            .cart-item.updating { opacity: 0.6; pointer-events: none; }
            .cart-item.removing { transform: scale(0.95); opacity: 0.5; }
            .value-updated { animation: valueUpdate 0.3s ease; }
            @keyframes valueUpdate { 0% { transform: scale(1); } 50% { transform: scale(1.05); color: #28a745; } 100% { transform: scale(1); } }
            .cart-notification { position: fixed; top: 20px; right: 20px; z-index: 10000; padding: 1rem; border-radius: 8px; transform: translateX(100%); transition: transform 0.3s ease; }
            .cart-notification.show { transform: translateX(0); }
            .cart-notification-success { background: #d4edda; border: 1px solid #c3e6cb; color: #155724; }
            .cart-notification-error { background: #f8d7da; border: 1px solid #f5c6cb; color: #721c24; }
            .cart-confirmation-dialog { position: fixed; top: 0; left: 0; width: 100%; height: 100%; z-index: 10001; display: flex; align-items: center; justify-content: center; opacity: 0; transition: opacity 0.3s ease; }
            .cart-confirmation-dialog.show { opacity: 1; }
            .dialog-backdrop { position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.6); backdrop-filter: blur(5px); }
            .dialog-content { background: white; padding: 2.5rem; border-radius: 16px; max-width: 450px; width: 90%; z-index: 1; box-shadow: 0 20px 60px rgba(0,0,0,0.3); transform: scale(0.9); transition: transform 0.3s ease; }
            .cart-confirmation-dialog.show .dialog-content { transform: scale(1); }
            .dialog-content h4 { color: #2c3e50; font-size: 1.5rem; font-weight: 700; margin-bottom: 1rem; text-align: center; }
            .dialog-content p { color: #6c757d; font-size: 1.1rem; line-height: 1.6; text-align: center; margin-bottom: 2rem; }
            .dialog-actions { display: flex; gap: 1rem; justify-content: center; }
            .btn-cancel, .btn-confirm { padding: 0.75rem 2rem; border-radius: 8px; font-weight: 600; font-size: 1rem; cursor: pointer; transition: all 0.3s ease; border: none; }
            .btn-cancel { background: #f8f9fa; color: #495057; border: 2px solid #dee2e6; }
            .btn-cancel:hover { background: #e9ecef; border-color: #adb5bd; }
            .btn-confirm { background: linear-gradient(135deg, #dc3545 0%, #c82333 100%); color: white; }
            .btn-confirm:hover { background: linear-gradient(135deg, #c82333 0%, #a71e2a 100%); transform: translateY(-1px); box-shadow: 0 4px 12px rgba(220,53,69,0.3); }
            .keyboard-help-btn { position: absolute; top: -10px; right: 0; background: transparent; border: 2px solid #0080ff; color: #0080ff; padding: 0.5rem; border-radius: 50%; transition: all 0.3s ease; }
            .keyboard-help-btn:hover { background: #0080ff; color: white; }
            .shortcuts-list { list-style: none; padding: 0; }
            .shortcuts-list li { padding: 0.5rem 0; }
            .shortcuts-list kbd { background: #f8f9fa; padding: 0.25rem 0.5rem; border-radius: 4px; font-family: monospace; }
        `).appendTo('head');
    },

    // ========================================================================
    // PAGE VISIBILITY HANDLING
    // ========================================================================

    // Page visibility handling
    handleVisibilityChange() {
        if (!document.hidden && this.state.updateQueue.size > 0) {
            // Process any pending updates when page becomes visible
            this.state.updateQueue.forEach((timeoutId, productId) => {
                clearTimeout(timeoutId);
                const $input = $(`.quantity-input[data-product-id="${productId}"]`);
                const quantity = parseInt($input.val()) || this.config.minQuantity;
                this.processPriceUpdate(productId, quantity);
            });
            this.state.updateQueue.clear();
        }
    }
};

// ============================================================================
// INITIALIZATION & GLOBAL EXPOSURE
// ============================================================================

// Initialize when DOM is ready
$(document).ready(() => {
    // Add loading state to body during initialization
    $('body').addClass('cart-initializing');
    
    // Initialize cart manager
    CartManager.init();
    
    // Remove loading state
    setTimeout(() => {
        $('body').removeClass('cart-initializing');
    }, 500);
});

// Expose CartManager globally for debugging and external access
window.CartManager = CartManager;