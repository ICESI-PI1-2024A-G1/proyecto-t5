// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = 'Nunito', '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#858796';



// Pie Chart Example
var ctx = document.getElementById("manager_chart_pie");
var myPieChart = new Chart(ctx, {
  type: 'doughnut',
  data: {
    labels: ["Solicitudes Aprobadas", "Solicitudes Solicitudes En revision", "Solicitudes por validar"],
    datasets: [{
      data: [parseInt(document.getElementById("solicitudes_aprobadas_manager").innerText), parseInt(document.getElementById("solicitudes_en_revision_manager").innerText), parseInt(document.getElementById("solicitudes_por_validar_manager").innerText)],
      backgroundColor: ['#1cc88a', '#f6c23e', '#e74a3b'],
      hoverBackgroundColor: ['#188f64', '#c99f33', '#9d342a'],
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
