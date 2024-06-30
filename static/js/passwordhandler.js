document.getElementById('addPasswordForm').addEventListener('submit', function(event) {
    // Prevent the form from being submitted normally
    event.preventDefault();

    // Get form data
    const accountName = document.getElementById('accountName').value;
    const websiteURL = document.getElementById('websiteURL').value;
    const password = document.getElementById('password').value;
    const notes = document.getElementById('notes').value;

    // Create a FormData object
    const formData = new FormData();
    formData.append('accountName', accountName);
    formData.append('websiteURL', websiteURL);
    formData.append('password', password);
    formData.append('notes', notes);

    // Send a POST request to the server
    fetch('/add_password', {
        method: 'POST',
        body: formData
    })
    .then(response => response.text())
    .then(data => alert(data))
    .catch(error => console.error('Error:', error));
});