document.getElementById('quality').addEventListener('change', function () {
    var videoPlayer = document.getElementById('movie-video');
    var newQuality = this.value;
    videoPlayer.src = newQuality;
    videoPlayer.play();
});
