
# VideoLLM

## Prerequisites
- **Python 3.10 and above**
- Install the required library for Whisper:
  ```bash
  pip install git+https://github.com/openai/whisper.git
  ```
- Install `ffmpeg` (required for audio processing):
  ```bash
  sudo apt update && sudo apt install ffmpeg
  ```

## Usage

1. **Generate Transcripts**  
   Run the following command to process a video and generate transcripts:
   ```bash
   python audio_transcribe.py
   ```

2. **Run the Application**  
   Use Streamlit to launch the application:
   ```bash
   streamlit run app.py
   ```

   This will start the Streamlit app in your browser.
