// Signup page JavaScript functionality
document.addEventListener('DOMContentLoaded', function() {
    // Password toggle functionality
    const password1Toggle = document.getElementById('password1-toggle');
    const password1Input = document.getElementById('id_password1');
    const password1Icon = document.getElementById('password1-icon');
    
    const password2Toggle = document.getElementById('password2-toggle');
    const password2Input = document.getElementById('id_password2');
    const password2Icon = document.getElementById('password2-icon');
    
    // Password 1 toggle
    if (password1Toggle && password1Input) {
        password1Toggle.addEventListener('click', function() {
            const type = password1Input.getAttribute('type') === 'password' ? 'text' : 'password';
            password1Input.setAttribute('type', type);
            
            if (type === 'text') {
                password1Icon.className = 'fas fa-eye-slash';
                password1Toggle.setAttribute('title', 'Hide password');
            } else {
                password1Icon.className = 'fas fa-eye';
                password1Toggle.setAttribute('title', 'Show password');
            }
        });
    }
    
    // Password 2 toggle
    if (password2Toggle && password2Input) {
        password2Toggle.addEventListener('click', function() {
            const type = password2Input.getAttribute('type') === 'password' ? 'text' : 'password';
            password2Input.setAttribute('type', type);
            
            if (type === 'text') {
                password2Icon.className = 'fas fa-eye-slash';
                password2Toggle.setAttribute('title', 'Hide password');
            } else {
                password2Icon.className = 'fas fa-eye';
                password2Toggle.setAttribute('title', 'Show password');
            }
        });
    }
    
    // Real-time password matching validation
    if (password1Input && password2Input) {
        password1Input.addEventListener('input', validatePasswords);
        password2Input.addEventListener('input', validatePasswords);
    }
    
    // Real-time email validation
    const emailInput = document.getElementById('id_email');
    if (emailInput) {
        emailInput.addEventListener('input', validateEmail);
    }
    
    // Form submission validation
    const signupForm = document.querySelector('form');
    if (signupForm) {
        signupForm.addEventListener('submit', function(e) {
            const firstName = document.getElementById('id_first_name').value.trim();
            const lastName = document.getElementById('id_last_name').value.trim();
            const email = document.getElementById('id_email').value.trim();
            const password1 = document.getElementById('id_password1').value;
            const password2 = document.getElementById('id_password2').value;
            
            // Clear previous errors
            clearErrors();
            
            let hasErrors = false;
            
            // First name validation
            if (!firstName) {
                showError('id_first_name', 'First name is required');
                hasErrors = true;
            }
            
            // Last name validation
            if (!lastName) {
                showError('id_last_name', 'Last name is required');
                hasErrors = true;
            }
            
            // Email validation
            if (!email) {
                showError('id_email', 'Email is required');
                hasErrors = true;
            } else if (!isValidEmail(email)) {
                showError('id_email', 'Please enter a valid email address');
                hasErrors = true;
            }
            
            // Password validation
            if (!password1) {
                showError('id_password1', 'Password is required');
                hasErrors = true;
            } else if (password1.length < 8) {
                showError('id_password1', 'Password must be at least 8 characters long');
                hasErrors = true;
            }
            
            if (!password2) {
                showError('id_password2', 'Please confirm your password');
                hasErrors = true;
            } else if (password1 !== password2) {
                showError('id_password2', 'Passwords do not match');
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
    
    function validatePasswords() {
        const password1 = password1Input.value;
        const password2 = password2Input.value;
        
        // Clear previous password errors
        clearFieldError('id_password1');
        clearFieldError('id_password2');
        
        // Password 1 validation
        if (password1 && password1.length < 8) {
            showError('id_password1', 'Password must be at least 8 characters long');
        }
        
        // Password matching validation
        if (password2 && password1 !== password2) {
            showError('id_password2', 'Passwords do not match');
        }
        
        // Show success state if passwords match and are valid
        if (password1 && password2 && password1 === password2 && password1.length >= 8) {
            showSuccess('id_password1', 'Password is valid');
            showSuccess('id_password2', 'Passwords match');
        }
    }
    
    function validateEmail() {
        const email = emailInput.value.trim();
        
        // Clear previous email errors
        clearFieldError('id_email');
        
        if (email && !isValidEmail(email)) {
            showError('id_email', 'Please enter a valid email address');
        } else if (email && isValidEmail(email)) {
            showSuccess('id_email', 'Email format is valid');
        }
    }
    
    function showError(fieldId, message) {
        const field = document.getElementById(fieldId);
        if (field) {
            field.classList.remove('is-valid');
            field.classList.add('is-invalid');
            
            // Remove existing error message
            const existingError = findValidationMessageContainer(field).querySelector('.error-message');
            if (existingError) {
                existingError.remove();
            }
            
            // Add new error message
            const errorDiv = document.createElement('div');
            errorDiv.className = 'error-message';
            errorDiv.innerHTML = `<i class="fas fa-exclamation-circle"></i>${message}`;
            findValidationMessageContainer(field).appendChild(errorDiv);
        }
    }
    
    function showSuccess(fieldId, message) {
        const field = document.getElementById(fieldId);
        if (field) {
            field.classList.remove('is-invalid');
            field.classList.add('is-valid');
            
            // Remove existing messages
            const container = findValidationMessageContainer(field);
            const existingError = container.querySelector('.error-message');
            const existingSuccess = container.querySelector('.success-message');
            if (existingError) existingError.remove();
            if (existingSuccess) existingSuccess.remove();
            
            // Add success message
            const successDiv = document.createElement('div');
            successDiv.className = 'success-message';
            successDiv.innerHTML = `<i class="fas fa-check-circle"></i>${message}`;
            container.appendChild(successDiv);
        }
    }
    
    function clearFieldError(fieldId) {
        const field = document.getElementById(fieldId);
        if (field) {
            field.classList.remove('is-invalid', 'is-valid');
            const container = findValidationMessageContainer(field);
            const errorMessage = container.querySelector('.error-message');
            const successMessage = container.querySelector('.success-message');
            if (errorMessage) errorMessage.remove();
            if (successMessage) successMessage.remove();
        }
    }
    
    // Helper function to find the correct container for validation messages
    function findValidationMessageContainer(field) {
        // For all fields, find the closest form-group to ensure messages appear below the input
        const formGroup = field.closest('.form-group');
        if (formGroup) {
            return formGroup;
        }
        // Fallback to parent node if no form-group found
        return field.parentNode;
    }
    
    function clearErrors() {
        // Remove all error classes and messages
        document.querySelectorAll('.is-invalid, .is-valid').forEach(field => {
            field.classList.remove('is-invalid', 'is-valid');
        });
        
        // Remove all validation messages from form groups and other containers
        document.querySelectorAll('.error-message, .success-message').forEach(message => {
            message.remove();
        });
    }
});
