document.addEventListener('DOMContentLoaded', function() {
    // Selecciona todos los elementos que tienen clases específicas de ScrollReveal
    const elementos = document.querySelectorAll('.scrollreveal');

    // Recorre cada elemento y configura ScrollReveal individualmente
    elementos.forEach(elemento => {
        // Obtén el valor del atributo data-sr-delay y data-sr-origin
        const delay = elemento.getAttribute('data-sr-delay') || 200; // Valor predeterminado de 200ms si no se especifica
        const origin = elemento.getAttribute('data-sr-origin') || 'bottom'; // Valor predeterminado 'bottom' si no se especifica

        // Configuración de ScrollReveal para cada elemento
        ScrollReveal().reveal(elemento, {
            duration: 1000,
            distance: '50px',  // Puedes ajustar la distancia como desees
            origin: origin,    // Aplica la dirección específica del atributo data
            opacity: 0,
            reset: false,
            easing: 'ease-in-out',
            delay: parseInt(delay)  // Aplica el retraso específico del atributo data
        });
    });
});
