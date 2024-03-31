
document.addEventListener("DOMContentLoaded", function () {
    const toggleButton = document.getElementById('toggleAside');
    const sidebar = document.getElementById('asideMenu');
    const mainContent = document.getElementById('main');

    toggleButton.addEventListener('click', function() {
        sidebar.classList.toggle('hidden');
        mainContent.classList.toggle('expanded');
        mainContent.classList.toggle('nonExpanded');
    });
});
