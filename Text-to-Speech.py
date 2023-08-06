from googletrans import Translator, constants
from pprint import pprint
from playsound import playsound
from gtts import gTTS
def trnslate():
    tr = Translator()
    lan = input('Please enter your desired language:\n')
    phrase = input('Say something here:\n')
    translated = tr.translate(phrase, dest = lan)
    aud = gTTS(translated.text, lang = lan)
    aud.save('trantest.mp3')
    playsound('trantest.mp3')

trnslate()
