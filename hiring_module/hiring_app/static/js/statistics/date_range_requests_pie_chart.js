var rangeRequestChart;

function createOrUpdateDateRangeRequestChart() {
  var chartCanvas = document.getElementById("date_range_requests_pie_chart");

  // Eliminar el gráfico anterior si existe
  if (rangeRequestChart) {
    rangeRequestChart.destroy();
  }

  // Crear el nuevo gráfico
  var ctx = chartCanvas.getContext("2d");
  rangeRequestChart = new Chart(ctx, {
    type: "doughnut",
    data: {
      labels: ["Solicitudes CEX", "Solicitudes Monitoria", "Solicitudes POS"],
      datasets: [
        {
          data: [
            parseInt(document.getElementById("contratos_cex").innerText),
            parseInt(document.getElementById("contratos_monitoria").innerText),
            parseInt(document.getElementById("contratos_pos").innerText),
          ],
          backgroundColor: ["#1cc88a", "#f6c23e", "#5a5c69"],
          hoverBackgroundColor: ["#188f64", "#c99f33", "#3c3e49"],
          hoverBorderColor: "rgba(234, 236, 244, 1)",
        },
      ],
    },
    options: {
      maintainAspectRatio: false,
      tooltips: {
        backgroundColor: "rgb(255,255,255)",
        bodyFontColor: "#858796",
        borderColor: "#dddfeb",
        borderWidth: 1,
        xPadding: 15,
        yPadding: 15,
        displayColors: true,
        caretPadding: 10,
      },
      legend: {
        display: true,
      },
      cutoutPercentage: 80,
    },
  });
}
