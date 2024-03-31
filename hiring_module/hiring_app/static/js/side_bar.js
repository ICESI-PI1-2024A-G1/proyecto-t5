document.addEventListener("DOMContentLoaded", function() {
    const toggleBtn = document.getElementById('toggleAside');
    const sidebar = document.getElementById('asideMenu');
    const mainContent = document.getElementById('main');

    toggleBtn.addEventListener('click', function() {
        sidebar.classList.toggle('hidden');
        mainContent.classList.toggle('expanded');
        mainContent.classList.toggle('nonExpanded');
    });
});
