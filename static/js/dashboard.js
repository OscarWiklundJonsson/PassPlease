document.getElementById('generatePasswordButton').addEventListener('click', function() {
    // Create a new XMLHttpRequest object
    var xhttp = new XMLHttpRequest();

    // Define a function to be called when the state of the XMLHttpRequest changes
    xhttp.onreadystatechange = function() {
        if (this.readyState === 4 && this.status === 200) {
            // This is where you handle the response from the Python script
            // For example, you could set the value of the password field to the response
            var response = JSON.parse(this.responseText);
            document.getElementById('passwordField').value = response.password;
        }
    };

    // Initiate a GET request to your Python script
    xhttp.open("GET", "/generate_password", true);
    xhttp.send();
});