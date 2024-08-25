
document.addEventListener("DOMContentLoaded", function () {
    var typedTextElement = document.getElementById('typed-text');

    var typed = new Typed(typedTextElement, {
        strings: [ "Industrial Engineer", "Web App Dev", "Data Analyst"],
        typeSpeed: 80,
        backSpeed: 35,
        loop: true,
        showCursor: false,
    });
});