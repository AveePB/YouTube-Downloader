from pytube.exceptions import RegexMatchError
import util.youtube_downloader as yt

#Constants:
OUTPUT_MP3_DIR = "./downloads/mp3s"
OUTPUT_MP4_DIR = "./downloads/mp4s"
MP3s_FILE_NAME = "./mp3s.txt"
MP4s_FILE_NAME = "./mp4s.txt"
READER_MODE = "r"


def main():
    print("YouTube Downloader (by AveePB)")

    #Open the input streams.
    mp3sReader = open(MP3s_FILE_NAME, READER_MODE) 
    mp4sReader = open(MP4s_FILE_NAME, READER_MODE)

    #Fetch all links.
    mp3Links = mp3sReader.readlines()
    mp4Links = mp4sReader.readlines()

    #Close the input bytes stream.
    mp3sReader.close()
    mp4sReader.close()

    #Download audios.
    print("Started downloading mp3s...")
    for link in mp3Links:
        try:
            yt.download_audio(OUTPUT_MP3_DIR, link)
        except RegexMatchError:
            print("Invalid URL!")
    print("Completed downloading mp3s", end="\n\n")

    #Download videos.
    print("Started downloading mp4s...")
    for link in mp4Links:
        try:
            yt.download_video(OUTPUT_MP4_DIR, link)
        except RegexMatchError:
            print("Invalid URL!")
    print("Completed downloading mp4s", end="\n\n")

    input("Press enter...")

if (__name__ == "__main__"):
    try:
        main()
    except FileNotFoundError as ex:
        print(ex)