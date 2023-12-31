from pytube import YouTube

def download_video(outputDir: str, link: str):
    #Remove enters.
    link = str.replace(link, "\n", "")

    #Fetch the video.
    print("Downloading video: ", link)
    ytVideo = YouTube(link).streams.get_highest_resolution()
    
    #Save the video.
    ytVideo.download(outputDir)
    print("Completed:", ytVideo.title, end="\n\n")


def download_audio(outputDir: str, link: str):
    #Remove enters.
    link = str.replace(link, "\n", "")

    #Fetch the audio.
    print("Downloading audio: ", link)
    ytAudio = YouTube(link).streams.get_audio_only()
    fileName = ytAudio.default_filename.replace("mp4", "mp3")

    #Save the audio.
    ytAudio.download(outputDir, fileName)
    print("Completed:", ytAudio.title, end="\n\n")