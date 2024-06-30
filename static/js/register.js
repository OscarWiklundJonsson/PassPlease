function registerUser() {
    const registerForm = document.querySelector('form');

    registerForm.addEventListener('submit', function(event) {
        event.preventDefault();

        const username = document.querySelector('input[name="username"]').value;
        const email = document.querySelector('input[name="email"]').value;
        const password = document.querySelector('input[name="password"]').value;

        const xhttp = new XMLHttpRequest();
        xhttp.open("POST", "/register", true);
        xhttp.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");

        xhttp.onreadystatechange = function() {
            if (this.readyState === 4 && this.status === 200) {
                // Redirect the user to the login page
                showSuccess("Account created successfully")
                window.location.href = '/login';
            } else if (this.readyState === 4 && this.status === 409) {
                // Show an alert when the email is already taken
                showAlert("Wrong Email, or Password", "error");
            }
        };

        const params = 'username=' + encodeURIComponent(username) + '&email=' + encodeURIComponent(email) + '&password=' + encodeURIComponent(password);
        xhttp.send(params);
    });
}

document.addEventListener('DOMContentLoaded', function() {
   registerUser(); // Call this on the registration page
});