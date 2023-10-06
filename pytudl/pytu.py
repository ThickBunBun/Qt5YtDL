import ffmpeg
import os


# downloading video part for future ffmpeg merg
def video_ytdl(yt, download_path, vid_tittle, q_tag,):

    print("Downloading video...")
    yt.streams.get_by_itag(q_tag).download(
        filename=os.path.join(download_path, f"{vid_tittle}_video.mp4"))
    audio_ytdl(yt, download_path, vid_tittle)
    ffmpeg_merg(download_path, vid_tittle)


def max_qldl(yt, download_path, vid_tittle):  # downloading max video quality
    print("Downloading...")
    yt.streams.filter(adaptive=True).first().download(
        filename=os.path.join(download_path, f"{vid_tittle}_video.mp4"))
    audio_ytdl(yt, download_path, vid_tittle)
    ffmpeg_merg(download_path, vid_tittle)


def audio_ytdl(yt, download_path, vid_tittle):
    # Downloading audio for future ffmpeg merge
    print("Downloading audio...")
    yt.streams.filter(only_audio=True).first().download(
        filename=os.path.join(download_path, f"{vid_tittle}_audio.mp4"))


def ffmpeg_merg(download_path, vid_tittle):  # Video and audio merge
    video_stream = ffmpeg.input(
        os.path.join(download_path, f"{vid_tittle}_video.mp4"))
    audio_stream = ffmpeg.input(
        os.path.join(download_path, f"{vid_tittle}_audio.mp4"))
    print("Merging...")
    ffmpeg.output(audio_stream, video_stream,
                  os.path.join(download_path, vid_tittle+".mp4"),
                  codec='copy').run()

    os.remove(os.path.join(download_path, f"{vid_tittle}_video.mp4"))
    os.remove(os.path.join(download_path, f"{vid_tittle}_audio.mp4"))
