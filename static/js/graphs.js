async function createTotalPasswordsChart() {
    // Fetch data from the server
    const response = await fetch('/get_password_data');  // Replace with your actual server route
    const dbData = await response.json();

    // Process the data to fit the format needed for the chart
    const labels = dbData.map(item => item.month);
    const data = dbData.map(item => item.totalPasswords);

    const totalPasswordsData = {
        labels: labels,
        datasets: [{
            label: 'Total Passwords registered this year',
            data: data,
            backgroundColor: 'rgba(0, 123, 255, 0.5)',
            borderColor: 'rgba(0, 123, 255, 1)',
            borderWidth: 0.5,
        }]
    };
    const totalPasswordsConfig = {
        type: 'line',
        data: totalPasswordsData,
        options: {
            responsive: true,
            animation: {
                duration: 1000, // general animation time
            },
            hover: {
                animationDuration: 1000, // duration of animations when hovering an item
            },
            responsiveAnimationDuration: 1000, // animation duration after a resize
            elements: {
                line: {
                    tension: 0 // disables bezier curves
                }
            },
            tooltips: {
                mode: 'index',
                intersect: false,
                backgroundColor: 'rgba(0, 0, 0, 0.7)', // change tooltip background color here
                titleFontColor: '#ffffff', // change tooltip title color here
                bodyFontColor: '#ffffff', // change tooltip body color here
                borderColor: '#333333', // change tooltip border color here
                borderWidth: 1, // change tooltip border width here
            },
            scales: {
                y: {
                    ticks: {
                        precision: 0
                    }
                }
            }
        }
    };

    const totalPasswordsChart = new Chart(
        document.getElementById('totalPasswordsChart'),
        totalPasswordsConfig
    );
}

// Call the function to create the chart
createTotalPasswordsChart();