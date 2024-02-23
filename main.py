import PyPDF2
import googletrans
import pyttsx3
from googletrans import Translator

"""
PDF to audio converter
Creates a mp3 file of it
"""

print(googletrans.LANGUAGES)
translator = Translator()

pdfreader = PyPDF2.PdfReader(open('doc.pdf', 'rb'))
speaker = pyttsx3.init()
voices = speaker.getProperty('voices')


# test function for types of voices available (OS voices)
def test_voices():
    print("Available voices: \n")
    for voice in voices:
        print(voice.name)
        speaker.setProperty('voice', voice.id)
        speaker.say("Hello World!")
    speaker.runAndWait()
    speaker.stop()


test_voices()
# run_test()
for page_num in range(len(pdfreader.pages)):
    text = pdfreader.pages[page_num].extract_text()
    clean_text = text.strip().replace('\n', ' ')

print(clean_text)
voices = speaker.getProperty('voices')
# setting English as the TTS language in case it is not default already
for voice in voices:
    if voice.name.find("English") != -1:
        pickedvoice = voice.id
speaker.setProperty('voice', pickedvoice)
speaker.setProperty('rate', 200)  # words per minute
speaker.save_to_file(clean_text, 'doc_audio.mp3')
speaker.say(clean_text)
speaker.runAndWait()
speaker.stop()