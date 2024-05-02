var monthlyRequestLineChart;

function createOrUpdateMonthlyRequestChart() {
    var chartCanvas = document.getElementById("monthly_requests_line_chart");
    
    // Eliminar el gráfico anterior si existe
    if (monthlyRequestLineChart) {
        monthlyRequestLineChart.destroy();
    }
    
    // Crear el nuevo gráfico
    var ctx = chartCanvas.getContext('2d');
    var daily_requests = eval(document.getElementById("daily_requests").innerText);
    var dataSelect = document.getElementById('month_select');
    var selected_month = dataSelect.value.replace(/[\[\]']/g, '').split(',');
    var labels = [];
    var cex_dataset = [{label: "CEX", data: [], borderColor: "#1cc88a", fill: false}];
    var monitoria_dataset = [{label: "Monitoria", data: [], borderColor: "#f6c23e", fill: false}];
    var pos_dataset = [{label: "Prestacion de Servicios", data: [], borderColor: "#5a5c69", fill: false}];
    for (var i = 0; i < daily_requests.length; i++) {
        if(daily_requests[i][0].split('-')[0] + "-" + daily_requests[i][0].split('-')[1] == selected_month[0]){
            labels.push(daily_requests[i][0].split('-')[2]);
            cex_dataset[0].data.push(daily_requests[i][1]);
            monitoria_dataset[0].data.push(daily_requests[i][2]);
            pos_dataset[0].data.push(daily_requests[i][3]);
        }
    }
    
    monthlyRequestLineChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: labels,
            datasets: cex_dataset.concat(monitoria_dataset).concat(pos_dataset),
        },
        options: {
            maintainAspectRatio: false,
            tooltips: {
                backgroundColor: "rgb(255,255,255)",
                bodyFontColor: "#858796",
                borderColor: '#dddfeb',
                borderWidth: 1,
                xPadding: 15,
                yPadding: 15,
                displayColors: false,
                caretPadding: 10,
            },
            legend: {
                display: true, // Display the legend
                labels: {
                    fontColor: '#333', // Set legend label color
                }
            },
            scales: {
                xAxes: [{
                    scaleLabel: {
                        display: true,
                        labelString: 'Dia del mes' // X-axis label
                    }
                }],
                yAxes: [{
                    scaleLabel: {
                        display: true,
                        labelString: 'Numero de solicitudes' // Y-axis label
                    }
                }]
            }
        },
    });
}

