// main.js

document.addEventListener('DOMContentLoaded', function() {
    const searchIconButton = document.querySelector('.search-icon-button');
    const searchInput = document.querySelector('.search-input');

    searchIconButton.addEventListener('click', function(event) {
        event.preventDefault();
        if (searchInput.value.trim() !== '') {
            searchInput.closest('form').submit();
        }
    });
});
