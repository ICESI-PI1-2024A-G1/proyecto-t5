const toggleButton = document.getElementById("toggleAside");
const asideMenu = document.getElementById("asideMenu");
const mainHeader = document.getElementById("mainHeader");
const main = document.getElementById("main");
let isAsideVisible = false;
var comment = "";

document
    .getElementById("acceptButton")
    .addEventListener("click", function () {
        // Aquí puedes realizar cualquier acción que necesites con el comentario
        var comment = document.getElementById("comment").value;
        console.log("Comentario ingresado:", comment);

        // Después de realizar las acciones necesarias, oculta el campo de comentario
        document.getElementById("commentSection").classList.add("hidden");
        // Limpia el contenido de la caja de texto
        document.getElementById("comment").value = "";

        // Muestra el mensaje emergente
        document
            .getElementById("commentSuccessMessage")
            .classList.remove("hidden");

        // Oculta el mensaje emergente después de 1.5 segundos
        setTimeout(function () {
            document
                .getElementById("commentSuccessMessage")
                .classList.add("hidden");
        }, 1500);
    });

function toggleDropdownStatus() {
    var dropdown = document.getElementById("dropdownStatus");
    dropdown.classList.toggle("hidden");
}

function changeOptionStatus(option) {
    var selectedOption = document.getElementById("selectedOptionStatus");
    previousOption = selectedOption.textContent; // Guarda el estado anterior
    selectedOption.textContent = option;

    // Si la opción seleccionada es "Contrato cancelado", muestra el campo de comentario y botón de aceptar
    if (option === "Contrato cancelado" || option == "Datos faltantes") {
        document.getElementById("commentSection").classList.remove("hidden");
    } else {
        document.getElementById("commentSection").classList.add("hidden");
        // Muestra el mensaje emergente
        document
            .getElementById("stateSuccessMessage")
            .classList.remove("hidden");
        // Oculta el mensaje emergente después de 1.5 segundos
        setTimeout(function () {
            document
                .getElementById("stateSuccessMessage")
                .classList.add("hidden");
        }, 1500);
    }

    toggleDropdownStatus(); // Oculta el menú desplegable después de seleccionar una opción
}

// Función para deshacer cambios con Ctrl + Z
document.addEventListener("keydown", function (event) {
    if (event.ctrlKey && event.key === "z") {
        var selectedOption = document.getElementById("selectedOption");
        selectedOption.textContent = previousOption;
    }
});

toggleButton.addEventListener("click", function () {
    // Verifica si el aside está oculto
    if (!isAsideVisible) {
        // Si está oculto, muéstralo
        asideMenu.classList.remove("hidden");
        asideMenu.classList.add("w-40");
        asideMenu.classList.add("w-[27%]");

        // Mueve el header a la derecha
        mainHeader.classList.add("ml-[27%]"); // 1/8 de 100%

        //Mueve el main a la derecha
        main.classList.add("ml-[27%]");

        // Actualiza el estado del aside
        isAsideVisible = true;
    } else if (isAsideVisible || window.innerWidth >= 1280) {
        // Si está visible, ocúltalo
        asideMenu.classList.add("hidden");
        asideMenu.classList.remove("w-40");
        asideMenu.classList.remove("w-[27%]");

        // Mueve el header a la izquierda
        mainHeader.classList.remove("ml-[27%]");

        //Mueve el main a la izquierda
        main.classList.remove("ml-[27%]");

        // Actualiza el estado del aside
        isAsideVisible = false;
    }
});
