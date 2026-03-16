// Image hover zoom
function bigImg(x) {
    x.style.height = "500px";
    x.style.width = "350px";
}

function normalImg(x) {
    x.style.height = "300px";
    x.style.width = "200px";
}

// Slider (AUTO)
let slideIndex = 0;

document.addEventListener("DOMContentLoaded", function () {
    showSlides();
});

function showSlides() {
    let i;
    let slides = document.getElementsByClassName("mySlides");

    if (slides.length === 0) return; // safety check

    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }

    slideIndex++;
    if (slideIndex > slides.length) {
        slideIndex = 1;
    }

    slides[slideIndex - 1].style.display = "block";

    setTimeout(showSlides, 2000); // 2 seconds
}
