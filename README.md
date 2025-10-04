# Python Demo of Nova-3-Medical-Speech-To-Text

## Installation and Setup

Assuming you have Python3 installed, run:
`python3 -m venv venv`
This will create a virtual environment called venv. You can name the second venv in the command anything you'd like to name the virtual env something different.

Run:
`source venv/bin/activate`
venv is the name of the virtual environment. Adjust accordingly.

`pip install deepgram-sdk python-dotenv openai`
OR
`pip install -r requirements.txt`

Put this in a .env file:
TODO: link to documentation for API key setup

`DEEPGRAM_API_KEY= [Your Deepgram API Key goes here]`
`OPENAI_API_KEY= [Your OpenAI API Key goes here]`

# Prerecorded audio file of diff voices

When I show a prerecorded audio file of two obvious differently sounding voices, I get a pretty acurrate transcription, but some of the words from Speaker1 carry over to Speaker 0 and vice vice versa.
A run is in the picture below:

# Prerecorded audio file of same voice

However, when I show a prerecorded audio of the same voice even though I intended to have two speakers, a doctor, and a patient, the transcription labeled the entire conversation with one speaker, Speaker 0 as in the following picture below:
