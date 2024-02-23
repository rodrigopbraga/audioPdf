PDF to Audio Converter

This Python script converts text from a PDF document into an audio file (MP3 format) using text-to-speech (TTS) technology. It utilizes the PyPDF2 library to extract text from the PDF file and the pyttsx3 library to generate audio output.
Features

    . Converts text from each page of a PDF document into audio.
    . Supports customization of voice selection and speech rate.
    . Provides options to save the audio output as an MP3 file.

How to Use

    . Ensure you have Python installed on your system.
    . Install the required libraries by running:
      pip install PyPDF2
      pip install pyttsx3
      pip install googletrans

Place the PDF document (doc.pdf) in the same directory as the script.
Open the script and ensure that the path to the PDF document is correctly specified ('doc.pdf').
Optionally, you can customize the voice selection and speech rate by modifying the test_voices() function and the setProperty() calls.
Run the script by executing the following command in your terminal or command prompt:

    python main.py

    The script will extract text from each page of the PDF document, convert it to audio, save the audio output as doc_audio.mp3 in the same directory and read it out loud.

Additional Notes

    . The script demonstrates how to use the PyPDF2 library to extract text from PDF files and the pyttsx3 library to generate audio output.
    . You can experiment with different voices and speech rates by modifying the script to suit your preferences.
      Currently setted to use the English voice if present in OS;
      Currently setted to read it at 200 (two hundred) words per minute;
    . You can listen as a test to all the voices installed in your OS with the test_voices() function.

If you encounter any issues or have suggestions for enhancements, please create an issue or submit a pull request.
