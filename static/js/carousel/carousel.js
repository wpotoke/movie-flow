let currentIndex = 0;

function moveCarousel(direction) {
    const track = document.querySelector('.carousel-track');
    const items = document.querySelectorAll('.carousel-item');
    const itemsPerView = 5; // Количество видимых элементов в карусели
    const totalItems = items.length;

    currentIndex += direction * itemsPerView;
    if (currentIndex < 0) {
        currentIndex = 0;
    } else if (currentIndex >= totalItems) {
        currentIndex = totalItems - itemsPerView;
    }

    track.style.transform = `translateX(${-currentIndex * 20}%)`;
}
