from pytube import YouTube

def download_audio_from_youtube(url, output_filename):
    yt = YouTube(url)
    video = yt.streams.filter(only_audio=True).first()
    video.download(output_filename)
