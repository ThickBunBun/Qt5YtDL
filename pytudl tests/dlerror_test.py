import pytest
from pytube import YouTube
from pytube.exceptions import RegexMatchError, VideoUnavailable


def test_plaintextinput():
    link = "simpletext"
    with pytest.raises(RegexMatchError):
        yt = YouTube(link)


def test_fakelink():
    link = "https://www.youtube.com/watch?v=SLfjsdgnl"
    with pytest.raises(RegexMatchError):
        yt = YouTube(link)


def test_incurrectlink():
    link = "https://www.youtube.com/watch?v=ARnOo7eLW6m"
    yt = YouTube(link)
    with pytest.raises(VideoUnavailable):
        print(yt.title)
