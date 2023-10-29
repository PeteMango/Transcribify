# main.py
import sys
from src.youtube import download_audio_from_youtube
from src.convert import convert_mp4_to_wav
from src.transcribe import transcribe_local_sphinx
from src.summarize import summarize_transcription
from config.settings import *

def main(youtube_url):
    # Step 1: Download audio from YouTube
    audio_filename = "videos/downloaded_audio.mp4"
    download_audio_from_youtube(youtube_url, audio_filename)
    print("STEP 1 Completed: Downloaded audio from YouTube")

    # Step 2: Convert the downloaded audio to WAV format
    wav_filename = "transcripts/downloaded_audio.wav"
    convert_mp4_to_wav(audio_filename, wav_filename)
    print("STEP 2 Completed: Converted audio to WAV format")

    # Step 3: Transcribe the WAV audio
    transcription = transcribe_local_sphinx(wav_filename)
    with open("transcripts/transcription.txt", "w") as f:
        f.write(transcription)
    print("STEP 3 Completed: Transcribe the WAV audio to text")

    # Step 4: Summarize the transcription
    summarized_text = summarize_transcription(transcription)
    print("Original Transcription:")
    print(transcription)
    print("\n\nSummarized Text:")
    print(summarized_text)
    print("STEP 4 Completed: Summarize the Transcription")


if __name__ == "__main__":
    youtube_url = "https://www.youtube.com/watch?v=2ka6us5caTk"
    main(youtube_url)
