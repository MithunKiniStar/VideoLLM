
# -*- coding: utf-8 -*-
"""
AudioTranscribe Script

This script performs the following tasks:
1. Installs required dependencies for audio processing and transcription.
2. Converts a video file to MP3 format using ffmpeg.
3. Transcribes the MP3 file using OpenAI's Whisper model.
"""

import os
import subprocess

# --------------------------
# Helper Functions
# --------------------------

def install_dependencies():
    """Installs the necessary libraries and tools."""
    try:
        print("Installing Whisper...")
        subprocess.run(["pip", "install", "git+https://github.com/openai/whisper.git"], check=True)
        print("Installing ffmpeg...")
        subprocess.run(["sudo", "apt", "update"], check=True)
        subprocess.run(["sudo", "apt", "install", "-y", "ffmpeg"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Dependency installation failed: {e}")
        raise

def convert_video_to_mp3(input_file, output_file):
    """Converts a video file to an MP3 audio file using ffmpeg.

    Args:
        input_file (str): Path to the input video file.
        output_file (str): Path to the output MP3 file.
    """
    ffmpeg_cmd = [
        "ffmpeg",
        "-i", input_file,
        "-vn",
        "-acodec", "libmp3lame",
        "-ab", "192k",
        "-ar", "44100",
        "-y",
        output_file
    ]
    try:
        subprocess.run(ffmpeg_cmd, check=True)
        print(f"Conversion successful: {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Conversion failed: {e}")
        raise

def transcribe_audio(audio_file, model="medium.en"):
    """Transcribes an audio file using Whisper.

    Args:
        audio_file (str): Path to the MP3 audio file.
        model (str): Whisper model to use for transcription (default: "medium.en").
    """
    whisper_cmd = ["whisper", audio_file, "--model", model]
    try:
        subprocess.run(whisper_cmd, check=True)
        print(f"Transcription completed for: {audio_file}")
    except subprocess.CalledProcessError as e:
        print(f"Transcription failed: {e}")
        raise

# --------------------------
# Main Execution Workflow
# --------------------------

def main():
    """Main workflow for the script."""
    # Install required dependencies
    # Uncomment this if running in a fresh environment
    # install_dependencies()

    # Define file paths
    input_video = "./source/videoplayback.1731774252515.publer.io.mp4"
    output_audio = "./source/Jamie_audio.mp3"

    # Convert video to audio
    print("Starting video-to-audio conversion...")
    convert_video_to_mp3(input_video, output_audio)

    # Transcribe the audio
    print("Starting audio transcription...")
    transcribe_audio(output_audio)

if __name__ == "__main__":
    main()
