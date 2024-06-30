function loginUser() {
    const loginForm = document.querySelector('form');

    loginForm.addEventListener('submit', function(event) {
        event.preventDefault();

        const emailField = document.querySelector('input[name="email"]');
        const passwordField = document.querySelector('input[name="password"]');


        const email = emailField.value;
        const password = passwordField.value;

        const xhttp = new XMLHttpRequest();
        xhttp.open("POST", "/login", true);
        xhttp.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");

        xhttp.onreadystatechange = function() {
            if (this.readyState === 4 && this.status === 200) {
                // Redirect the user to the dashboard page
                window.location.href = '/dashboard';
            } else if (this.readyState === 4) {
                // Display an error message
                alert("Incorrect username or password");
            }
        };

        const params = 'email=' + encodeURIComponent(email) + '&password=' + encodeURIComponent(password);
        xhttp.send(params);
    });
}

document.addEventListener('DOMContentLoaded', function() {
   // registerUser(); // Call this on the registration page
    loginUser(); // Call this on the login page
});