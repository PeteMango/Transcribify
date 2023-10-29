import subprocess

def convert_mp4_to_wav(input_path, output_path):
    """
    Convert MP4 video to WAV audio using ffmpeg.

    Args:
    - input_path (str): Path to the input MP4 file.
    - output_path (str): Path to the output WAV file.

    Returns:
    - None
    """
    command = [
        'ffmpeg',
        '-i', input_path,
        '-vn',         # No video.
        '-acodec', 'pcm_s16le',  # Set audio codec to pcm_s16le.
        '-ar', '44100',   # Set audio rate to 44100.
        '-ac', '2',       # Set number of audio channels to 2.
        output_path
    ]

    subprocess.run(command, check=True)

if __name__ == "__main__":
    input_file = "videos/climb.mp4"
    output_file = "transcripts/climb.wav"

    convert_mp4_to_wav(input_file, output_file)
