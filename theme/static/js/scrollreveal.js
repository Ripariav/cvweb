document.addEventListener('DOMContentLoaded', function() {
    // Configuración de ScrollReveal
    ScrollReveal().reveal('.scrollrevealB', {
        duration: 1000,        // Duración de la animación en milisegundos
        distance: '50px',      // Distancia de desplazamiento del elemento
        origin: 'bottom',      // Dirección desde la que el elemento aparece ('top', 'bottom', 'left', 'right')
        opacity: 0,            // Opacidad inicial del elemento
        reset: false,           // Si la animación se debe reiniciar cada vez que se hace scroll
        easing: 'ease-in-out', // Tipo de animación (puede ser 'ease', 'ease-in-out', etc.)
        delay: 200             // Retraso antes de comenzar la animación en milisegundos
    });

    ScrollReveal().reveal('.scrollrevealNavBar', {
        duration: 1000,        // Duración de la animación en milisegundos
        distance: '25px',      // Distancia de desplazamiento del elemento
        origin: 'bottom',      // Dirección desde la que el elemento aparece ('top', 'bottom', 'left', 'right')
        opacity: 0,            // Opacidad inicial del elemento
        reset: false,           // Si la animación se debe reiniciar cada vez que se hace scroll
        easing: 'ease-in-out', // Tipo de animación (puede ser 'ease', 'ease-in-out', etc.)
        delay: 1800             // Retraso antes de comenzar la animación en milisegundos
    });

    ScrollReveal().reveal('.scrollrevealL', {
        duration: 1000,        // Duración de la animación en milisegundos
        distance: '500px',      // Distancia de desplazamiento del elemento
        origin: 'left',      // Dirección desde la que el elemento aparece ('top', 'bottom', 'left', 'right')
        opacity: 0,            // Opacidad inicial del elemento
        reset: false,           // Si la animación se debe reiniciar cada vez que se hace scroll
        easing: 'ease-in-out', // Tipo de animación (puede ser 'ease', 'ease-in-out', etc.)
        delay: 800             // Retraso antes de comenzar la animación en milisegundos
    });

    ScrollReveal().reveal('.scrollrevealR', {
        duration: 1000,        // Duración de la animación en milisegundos
        distance: '200px',      // Distancia de desplazamiento del elemento
        origin: 'rigth',      // Dirección desde la que el elemento aparece ('top', 'bottom', 'left', 'right')
        opacity: 0,            // Opacidad inicial del elemento
        reset: false,           // Si la animación se debe reiniciar cada vez que se hace scroll
        easing: 'ease-in-out', // Tipo de animación (puede ser 'ease', 'ease-in-out', etc.)
        delay: 800             // Retraso antes de comenzar la animación en milisegundos
    });
});