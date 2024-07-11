document.addEventListener("DOMContentLoaded", function() {
    // Generate Name
    document.getElementById("generate-name-btn").addEventListener("click", function(event) {
        event.preventDefault();
        fetch('/temp-services/name')
            .then(response => response.json())
            .then(data => {
                document.getElementById("generated-name").textContent = data.name;
            });
    });

    // Generate Address
    document.getElementById("generate-address-btn").addEventListener("click", function(event) {
        event.preventDefault();
        fetch('/temp-services/address')
            .then(response => response.json())
            .then(data => {
                document.getElementById("generated-address").textContent =  data.address;
            });
    });

    // Generate ID
    document.getElementById("generate-id-btn").addEventListener("click", function(event) {
        event.preventDefault();
        fetch('/temp-services/id')
            .then(response => response.json())
            .then(data => {
                const list = document.getElementById("generated-id-list");
                list.innerHTML = '';
                list.appendChild(createListItem(`Name: ${data.name}`));
                list.appendChild(createListItem(`DOB: ${data.dob}`));
                list.appendChild(createListItem(`Phone Number: ${data.phone_number}`));
                list.appendChild(createListItem(`Address: ${data.address}`));
                list.appendChild(createListItem(`Email: ${data.email}`));
                list.appendChild(createListItem(`Credit Card: `));
                list.appendChild(createListItem(`\tProvider: ${data.credit_card.provider}`));
                list.appendChild(createListItem(`\tNumber: ${data.credit_card.number}`));
                list.appendChild(createListItem(`\tExpire: ${data.credit_card.expire}`));
                list.appendChild(createListItem(`\tSecurity Code: ${data.credit_card.security_code}`));
            });
    });

    function createListItem(text) {
        const item = document.createElement('li');
        item.textContent = text;
        return item;
    }
});
