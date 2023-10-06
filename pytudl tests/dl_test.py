import pytest
import os
from pytube import YouTube
from pytu import max_qldl
from pytu import audio_ytdl
from pytu import video_ytdl


@pytest.fixture
def credentials(tmp_path):
    d = tmp_path
    d.mkdir
    link = 'https://www.youtube.com/watch?v=FnuRPX5km0Y'
    download_path = d
    yt = YouTube(link)
    vid_title = fr"{yt.title}".replace('/', '／').replace('~', '～')

    return download_path, yt, vid_title


def test_maxdl(credentials):
    download_path, yt, vid_title = credentials
    max_qldl(yt, download_path, vid_title)
    assert os.path.isfile(os.path.join(download_path, vid_title+'.mp4'))


def test_audiodl(credentials):
    download_path, yt, vid_title = credentials
    audio_ytdl(yt, download_path, vid_title)
    assert os.path.isfile(os.path.join(download_path, vid_title+'_audio.mp4'))


def test_viddl(credentials):
    download_path, yt, vid_title = credentials
    video_ytdl(yt, download_path, vid_title, q_tag='137')
    assert os.path.isfile(os.path.join(download_path, vid_title+'.mp4'))
