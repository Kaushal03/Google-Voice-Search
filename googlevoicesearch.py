import googletrans
import speech_recognition as sr
import gtts
import webbrowser

recognizer = sr.Recognizer()
translator = googletrans.Translator()
input_lang = 'en-IN'
output_lang = 'hi'
with sr.Microphone() as source:
    print('Speak Now')
    recognizer.adjust_for_ambient_noise(source)
    voice = recognizer.listen(source)
    print(voice)
    print('Recognizing your voice')
    text = recognizer.recognize_google(voice, language=input_lang)
    webbrowser.open('https://www.google.com/search?q=' + str(text))
    print('Wait....')
    print(text)