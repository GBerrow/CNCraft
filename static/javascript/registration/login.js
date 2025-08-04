// Login page JavaScript functionality
document.addEventListener('DOMContentLoaded', function() {
    // Password toggle functionality
    const passwordToggle = document.getElementById('password-toggle');
    const passwordInput = document.getElementById('id_password');
    const passwordIcon = document.getElementById('password-icon');
    
    if (passwordToggle && passwordInput) {
        passwordToggle.addEventListener('click', function() {
            const type = passwordInput.getAttribute('type') === 'password' ? 'text' : 'password';
            passwordInput.setAttribute('type', type);
            
            // Toggle icon
            if (type === 'text') {
                passwordIcon.className = 'fas fa-eye-slash';
                passwordToggle.setAttribute('title', 'Hide password');
            } else {
                passwordIcon.className = 'fas fa-eye';
                passwordToggle.setAttribute('title', 'Show password');
            }
        });
    }
    
    // Form validation
    const loginForm = document.querySelector('form');
    if (loginForm) {
        loginForm.addEventListener('submit', function(e) {
            const email = document.getElementById('id_login').value.trim();
            const password = document.getElementById('id_password').value;
            
            // Clear previous errors
            clearErrors();
            
            let hasErrors = false;
            
            // Email validation
            if (!email) {
                showError('id_login', 'Email is required');
                hasErrors = true;
            } else if (!isValidEmail(email)) {
                showError('id_login', 'Please enter a valid email address');
                hasErrors = true;
            }
            
            // Password validation
            if (!password) {
                showError('id_password', 'Password is required');
                hasErrors = true;
            }
            
            if (hasErrors) {
                e.preventDefault();
            }
        });
    }
    
    // Helper functions
    function isValidEmail(email) {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return emailRegex.test(email);
    }
    
    function showError(fieldId, message) {
        const field = document.getElementById(fieldId);
        if (field) {
            field.classList.add('is-invalid');
            
            // Remove existing error message
            const existingError = field.parentNode.querySelector('.error-message');
            if (existingError) {
                existingError.remove();
            }
            
            // Add new error message
            const errorDiv = document.createElement('div');
            errorDiv.className = 'error-message';
            errorDiv.innerHTML = `<i class="fas fa-exclamation-circle"></i>${message}`;
            field.parentNode.appendChild(errorDiv);
        }
    }
    
    function clearErrors() {
        // Remove all error classes and messages
        document.querySelectorAll('.is-invalid').forEach(field => {
            field.classList.remove('is-invalid');
        });
        
        document.querySelectorAll('.error-message').forEach(error => {
            error.remove();
        });
    }
});
