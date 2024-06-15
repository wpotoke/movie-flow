from pathlib import Path
from typing import IO, Generator, Tuple, Union
from django.shortcuts import get_object_or_404
from django.http import HttpRequest
from movie_app.models import Movie


def ranged(
    file: IO[bytes],
    start: int = 0,
    end: int = None,
    block_size: int = 8192,
) -> Generator[bytes, None, None]:
    consumed = 0

    file.seek(start)
    while True:
        data_length = min(block_size, end - start - consumed) if end else block_size
        if data_length <= 0:
            break
        data = file.read(data_length)
        if not data:
            break
        consumed += data_length
        yield data

    if hasattr(file, "close"):
        file.close()


def open_file(
    request: HttpRequest, slug_film: str, quality: str
) -> Tuple[Union[IO[bytes], Generator[bytes, None, None]], int, int, str]:
    _video = get_object_or_404(Movie, slug=slug_film)  # Get film

    if quality == "480p":
        path = Path(_video.video_medium.path)
    elif quality == "720p":
        path = Path(_video.video_high.path)
    elif quality == "1080p":
        path = Path(_video.video_hd.path)
    else:
        path = Path(_video.video_hd.path)  # Default to HD if no quality specified

    file = path.open("rb")  # Reading file
    file_size = path.stat().st_size  # Get size of file

    content_length = file_size
    status_code = 200
    content_range = request.headers.get(
        "range"
    )  # Console has header range (count bytes), get count bytes

    if content_range is not None:
        content_ranges = (
            content_range.strip().lower().split("=")[-1]
        )  # Start count bytes
        range_start, range_end, *_ = map(
            str.strip, (content_ranges + "-").split("-")
        )  # Start and end range
        range_start = max(0, int(range_start)) if range_start else 0
        range_end = min(file_size - 1, int(range_end)) if range_end else file_size - 1
        content_length = (range_end - range_start) + 1
        file = ranged(file, start=range_start, end=range_end + 1)
        status_code = 206
        content_range = f"bytes {range_start}-{range_end}/{file_size}"
    else:
        content_range = None

    return file, status_code, content_length, content_range
