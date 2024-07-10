document.getElementById('searchForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const websiteURL = document.getElementById('searchWebsiteURL').value;

    const formData = new FormData();
    formData.append('searchWebsiteURL', websiteURL);

    // Send a POST request to the server
    fetch('/search_password', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        // Create a table
        const table = document.createElement('table');
        table.className = 'table';

        // Create table header
        const thead = document.createElement('thead');
        const headerRow = document.createElement('tr');
        const headers = ['Account Name', 'Website URL', 'Password', 'Notes'];
        headers.forEach(header => {
            var th = document.createElement('th');
            th.textContent = header;
            headerRow.appendChild(th);
        });
        thead.appendChild(headerRow);
        table.appendChild(thead);

        const tbody = document.createElement('tbody');
        data.forEach(row => {
            const tr = document.createElement('tr');
            row.forEach(cell => {
                const td = document.createElement('td');
                td.textContent = cell;
                tr.appendChild(td);
            });
            tbody.appendChild(tr);
        });
        table.appendChild(tbody);

        const searchResultsDiv = document.getElementById('searchResults');
        searchResultsDiv.innerHTML = '';  // Clear previous search results
        searchResultsDiv.appendChild(table);
    })
    .catch(error => console.error('Error:', error));
});