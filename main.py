import pyttsx3, PyPDF2
import googletrans
from googletrans import Translator

"""
PDF to audio converter
Creates a mp3 file of it
"""

print(googletrans.LANGUAGES)
translator = Translator()

pdfreader = PyPDF2.PdfReader(open('doc.pdf', 'rb'))
speaker = pyttsx3.init()


# test function for types of voices available (OS voices)
def test_voices():
    voices = speaker.getProperty('voices')
    for voice in voices:
        print(voice, voice.id)
        speaker.setProperty('voice', voice.id)
        speaker.say("Hello World!")
        speaker.runAndWait()
        speaker.stop()

for page_num in range(len(pdfreader.pages)):
    text = pdfreader.pages[page_num].extract_text()
    clean_text = text.strip().replace('\n', ' ')
print(clean_text)
speaker.save_to_file(clean_text, 'doc_audio.mp3')
speaker.setProperty('voice', 0)
speaker.setProperty('rate', 200)  # words per minute
speaker.say(clean_text)
speaker.runAndWait()
speaker.stop()