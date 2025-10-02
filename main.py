from openai import OpenAI
import sys
from deepgram import (
    DeepgramClient,
    PrerecordedOptions,
    FileSource,
)
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI()

# SOAP instruction for the developer role
SOAP_INSTRUCTION = """
.....
"""

def transcribe_audio(audio_file):
    # STEP 1: Create a Deepgram client using the API key
    deepgram = DeepgramClient()

    with open(audio_file, "rb") as file:
        buffer_data = file.read()

    payload: FileSource = {
        "buffer": buffer_data
    }

    # STEP 2: Configure Deepgram options for audio analysis
    options = PrerecordedOptions(
        model="nova-3-medical", # Specify the medical transcription model
        smart_format=True,      # Automatically add punctuation
        diarize=True            # Identify speakers in the conversation
    )

    # STEP 3: Call the transcribe_file method with the text payload and options
    response = deepgram.listen.rest.v("1").transcribe_file(payload, options)

    data = response["results"]["channels"][0]["alternatives"][0]["paragraphs"]["transcript"]

    return data

def generate_note_and_save(transcript, output_file):
    pass

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <audio_file_path>")
        sys.exit(1)

    audio_file = sys.argv[1]
    output_file = "generated_soap_note.txt"

    print("Starting transcription...")
    transcript = transcribe_audio(audio_file)
    print(transcript)
    print("Transcription completed.")

    # print("Generating SOAP note...")
    # generate_note_and_save(transcript, output_file)
    # print("SOAP note generation completed.")

if __name__ == "__main__":
    main()