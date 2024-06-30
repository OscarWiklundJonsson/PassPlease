document.getElementById('searchForm').addEventListener('submit', function(event) {
    // Prevent the form from being submitted normally
    event.preventDefault();

    // Get form data
    var websiteURL = document.getElementById('searchWebsiteURL').value;

    // Create a FormData object
    var formData = new FormData();
    formData.append('searchWebsiteURL', websiteURL);

    // Send a POST request to the server
    fetch('/search_password', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        // Create a table
        var table = document.createElement('table');
        table.className = 'table';

        // Create table header
        var thead = document.createElement('thead');
        var headerRow = document.createElement('tr');
        var headers = ['Account Name', 'Website URL', 'Password', 'Notes'];
        headers.forEach(header => {
            var th = document.createElement('th');
            th.textContent = header;
            headerRow.appendChild(th);
        });
        thead.appendChild(headerRow);
        table.appendChild(thead);

        // Create table body
        var tbody = document.createElement('tbody');
        data.forEach(row => {
            var tr = document.createElement('tr');
            row.forEach(cell => {
                var td = document.createElement('td');
                td.textContent = cell;
                tr.appendChild(td);
            });
            tbody.appendChild(tr);
        });
        table.appendChild(tbody);

        // Insert the table into the DOM
        var searchResultsDiv = document.getElementById('searchResults');
        searchResultsDiv.innerHTML = '';  // Clear previous search results
        searchResultsDiv.appendChild(table);
    })
    .catch(error => console.error('Error:', error));
});