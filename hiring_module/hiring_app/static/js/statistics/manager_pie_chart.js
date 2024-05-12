var managerChart;

function createOrUpdateManagerChart() {
    var chartCanvas = document.getElementById("manager_chart_pie");

    // Eliminar el gráfico anterior si existe
    if (managerChart) {
        managerChart.destroy();
    }
    
    // Crear el nuevo gráfico
    var ctx = chartCanvas.getContext('2d');
    managerChart = new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: ["Solicitudes Aprobadas", "Solicitudes En revisión", "Solicitudes por validar", "Solicitudes canceladas"],
            datasets: [{
                data: [
                    parseInt(document.getElementById("solicitudes_aprobadas_manager").innerText),
                    parseInt(document.getElementById("solicitudes_en_revision_manager").innerText),
                    parseInt(document.getElementById("solicitudes_por_validar_manager").innerText),
                    parseInt(document.getElementById("solicitudes_canceladas_manager").innerText)
                ],
                backgroundColor: ['#1cc88a', '#f6c23e', '#e74a3b','#858795'],
                hoverBackgroundColor: ['#188f64', '#c99f33', '#9d342a','#666873'],
                hoverBorderColor: "rgba(234, 236, 244, 1)",
            }],
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
                display: false
            },
            cutoutPercentage: 80,
        },
    });
}
