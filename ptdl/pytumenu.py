
from pytube import YouTube
import re
import os
from pytu import max_qldl, audio_ytdl, video_ytdl
from pytube.exceptions import RegexMatchError


def ql_filter(yt):
    ql_list = []
    linkfilter = re.compile(r'itag=["\w]+ mime_type="video/mp4" res=["\w]+')
    stream_ls = yt.streams.filter(adaptive=True)
    quality = linkfilter.findall(f'{stream_ls}')
    for ql in quality:
        ql_list.append(str(ql).replace('mime_type="video/mp4"', ''))
    return ql_list


def link_input():
    quit_list = ['q', 'quit', 'exit']
    u_input = ''

    while u_input.lower() not in (quit_list):
        u_input = input("Input a video link: ")

        if u_input in quit_list:
            quit()

        try:
            YouTube(u_input)

        except RegexMatchError:
            print("Please input a valid youtube link")

        else:
            youtube_link = u_input
            return youtube_link


def dir_input():
    quit_list = ['q', 'quit', 'exit']
    u_input = ''

    while u_input.lower() not in (quit_list):
        u_input = input("Enter downloadpath, blank for default:")

        if u_input in quit_list:
            quit()

        if os.path.isdir(u_input):
            dir_path = u_input

            return dir_path
        elif u_input == "":
            dir_path = os.path.expanduser('~')

            return dir_path

        elif u_input not in quit_list:
            print("This dir, does not exist.")


def input_option(link, dir):

    print("Please wait...")
    yt = YouTube(link, use_oauth=True, allow_oauth_cache=True)
    vid_tittle = fr"{yt.title}".replace('/', '／').replace('~', '～')
    quit_list = ['q', 'quit', 'exit']
    audio_only_opitons = ['a', 'audio_only']
    max_ql_options = ['m', 'max', 'highest']
    ql_selection_options = ql_filter(yt)
    options = [f'Only audio download: {", ".join(audio_only_opitons)}',
               f'Max quality: {", ".join(max_ql_options)}',
               f'Quality selecion(itag value only):\
               {", ".join(ql_selection_options)}',
               f'Quit {", ".join(quit_list)}']
    u_input = ""
    yt = YouTube(link, use_oauth=True, allow_oauth_cache=True)
    vid_tittle = fr"{yt.title}".replace('/', '／').replace('~', '～')

    print()
    print(yt.title)
    print()
    print("Options")
    print()
    for option in options:
        print(f"{option}")
    print()

    while u_input.lower() not in (quit_list):
        u_input = input("Select the option: ")

        if u_input in quit_list:
            quit()

        if u_input in max_ql_options:
            max_qldl(yt, dir, vid_tittle)
            print("Done")

            return None

        elif u_input in audio_only_opitons:
            audio_ytdl(yt, dir, vid_tittle)
            print("Done")

            return None

        else:
            try:
                video_ytdl(yt, dir, vid_tittle, u_input)
                print("Done")

                return None

            except ValueError:
                print("Select a valid option")
            except AttributeError:
                print("Select a valid itag")


def main():
    print("QtPyTube ver0.0.4a")
    link = link_input()
    dir = dir_input()
    input_option(link, dir)


if __name__ == "__main__":
    main()
