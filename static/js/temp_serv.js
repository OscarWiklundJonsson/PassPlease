document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("generate-name-btn").addEventListener("click", function(event) {
        event.preventDefault();
        fetch('/temp-services/name')
            .then(response => response.json())
            .then(data => {
                document.getElementById("generated-name").textContent = "Generated Name: " + data.name;
            });
    });

    document.getElementById("generate-address-btn").addEventListener("click", function(event) {
        event.preventDefault();
        fetch('/temp-services/address')
            .then(response => response.json())
            .then(data => {
                document.getElementById("generated-address").textContent = "Generated Address: " + data.address;
            });
    });
});