document.addEventListener("DOMContentLoaded", function() {
    const slides = document.querySelector(".slides");
    const slide = document.querySelectorAll(".slide");
    const prev = document.querySelector(".prev");
    const next = document.querySelector(".next");
    let currentIndex = 0;
    let slideInterval;

    function goToSlide(index) {
        if (index < 0) {
            index = slide.length - 1;
        } else if (index >= slide.length) {
            index = 0;
        }
        slides.style.transform = `translateX(-${index * 100}%)`;
        currentIndex = index;
    }

    function startSlideShow() {
        stopSlideShow(); // Сначала остановим текущее слайд-шоу
        slideInterval = setInterval(function() {
            goToSlide(currentIndex + 1);
        }, 5000); // Change slide every 5 seconds
    }

    function stopSlideShow() {
        clearInterval(slideInterval);
    }

    prev.addEventListener("click", function() {
        goToSlide(currentIndex - 1);
        startSlideShow(); // Перезапускаем слайд-шоу после переключения
    });

    next.addEventListener("click", function() {
        goToSlide(currentIndex + 1);
        startSlideShow(); // Перезапускаем слайд-шоу после переключения
    });

    const bannerSlider = document.querySelector(".banner-slider");

    // Останавливаем слайд-шоу при наведении на баннер или стрелки
    bannerSlider.addEventListener("mouseenter", stopSlideShow);
    bannerSlider.addEventListener("mouseleave", startSlideShow);

    prev.addEventListener("mouseenter", stopSlideShow);
    prev.addEventListener("mouseleave", startSlideShow);

    next.addEventListener("mouseenter", stopSlideShow);
    next.addEventListener("mouseleave", startSlideShow);

    startSlideShow();
});
