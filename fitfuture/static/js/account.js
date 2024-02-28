document.addEventListener('DOMContentLoaded', function() {
    // Get the form element
    const form = document.querySelector('form');

    // Add event listener for form submission
    form.addEventListener('submit', function(event) {
        // Prevent the default form submission behavior
        event.preventDefault();

        // Remove any existing error indicators
        const errorInputs = form.querySelectorAll('.is-invalid');
        errorInputs.forEach(function(input) {
            input.classList.remove('is-invalid');
        });

        // Validate form inputs
        let isValid = true;

        // Validate first name
        const firstnameInput = form.querySelector('input[name="firstname"]');
        if (!firstnameInput.value.trim()) {
            firstnameInput.classList.add('is-invalid');
            isValid = false;
        }

        // Validate last name
        const lastnameInput = form.querySelector('input[name="lastname"]');
        if (!lastnameInput.value.trim()) {
            lastnameInput.classList.add('is-invalid');
            isValid = false;
        }

        // Validate username
        const usernameInput = form.querySelector('input[name="username"]');
        if (!usernameInput.value.trim()) {
            usernameInput.classList.add('is-invalid');
            isValid = false;
        }

        // Validate height
        const heightInput = form.querySelector('input[name="height"]');
        if (!heightInput.value.trim()) {
            heightInput.classList.add('is-invalid');
            isValid = false;
        }

        // Validate weight
        const weightInput = form.querySelector('input[name="weight"]');
        if (!weightInput.value.trim()) {
            weightInput.classList.add('is-invalid');
            isValid = false;
        }

        // Validate gender
        const genderSelect = form.querySelector('select[name="gender"]');
        if (!genderSelect.value.trim()) {
            genderSelect.classList.add('is-invalid');
            isValid = false;
        }

        // Validate email
        const emailInput = form.querySelector('input[name="email"]');
        if (!emailInput.value.trim()) {
            emailInput.classList.add('is-invalid');
            isValid = false;
        }

        // Validate password
        const passwordInput = form.querySelector('input[name="password"]');
        if (!passwordInput.value.trim()) {
            passwordInput.classList.add('is-invalid');
            isValid = false;
        }

        // Validate confirm password
        const confirmPasswordInput = form.querySelector('input[name="confirm_password"]');
        if (!confirmPasswordInput.value.trim()) {
            confirmPasswordInput.classList.add('is-invalid');
            isValid = false;
        }

        // If form is valid, submit it
        if (isValid) {
            form.submit();
        }
    });
});
