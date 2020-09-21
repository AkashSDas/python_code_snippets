# ###### import speech_recognition ######

# =================================
import speech_recognition as sr

# ---------------------------------
# ### Recognizer ###

# Recognizer method will work as recognizer to recognize our audio
r = sr.Recognizer()
# ---------------------------------
# ### Microphone ###

# Initializing our source using the Microphone method

with sr.Microphone() as source:
    print("Speak Anything: ")
    audio = r.listen(source)  # r.listen listen's to source 
    
    try:
        text = r.recognize_google(audio)  
        print("You Said: {}".format(text))
    except:
        print("Sorry could not recognize your voice")
        
# There are other options, other than recognize_google such as recognize_bing, recognize_google_cloud, recognize_ibm, etc        
# =================================
# ### Packages for speech recognition in Python ###

# 1. apiai
# 2. assemblyai
# 3. Google-cloud-speech
# 3. SpeechRecognition
# 4. Pocketsphinx
# 5. Watson-developer-cloud
# 6. wit        
# =================================
# ### Using the below API's we can record audio from different sources ###

# recognize_bing()
# recognize_google()
# recognize_google_cloud() # It requries installation of google cloud speech package
# recognize_houndify()
# recognize_ibm()
# recognize_sphinx() # It requries installation of pocket sphinx, it can also be used to run speech recognition offline
# recognize_wit()
# =================================
# ### Working with microphone ###

# To work with microphones we will install PyAudio package in python
# =================================
# ### Use Case ###

# - Converting speech to text using speech recognition
# - Using the text to open URL using web browser
# - Searching a query using speech inside the URL
# =================================
# ### Here we are opening webpage ###

import speech_recognition as sr
import webbrowser

r1 = sr.Recognizer()
r2 = sr.Recognizer()
r3 = sr.Recognizer()

with sr.Microphone() as source:
    print("Search #: search youtube")
    print("Speak Now: ")
    audio = r3.listen(source)
    
if "#" in r2.recognize_google(audio):
    r2 = sr.Recognizer()
    url = 'https://www.#.com'
    with sr.Microphone() as source:
        print('Search your query')
        audio = r2.listen(source)
        
        try:
            get = r2.recognize_google(audio)
            print(get)
            wb.get().open_new(url+get)
        except sr.UnknownValueError:
            print("Error")
        except sr.RequestError as e:
            print("failed".format(e))
# =================================
### Here we can directly open videos in YouTube ###            

import speech_recognition as sr
import webbrowser

r1 = sr.Recognizer()
r2 = sr.Recognizer()
r3 = sr.Recognizer()

with sr.Microphone() as source:
    print("Search #: search youtube")
    print("Speak Now: ")
    audio = r3.listen(source)
    
if video in r2.recognize_google(audio):
    r1 = sr.Recognizer()
    url = 'https://www.youtube.com/results?search query='
    with sr.Microphone() as source:
        print('Search your query')
        audio = r1.listen(source)
        
        try:
            get = r1.recognize_google(audio)
            print(get)
            wb.get().open_new(url+get)
        except sr.UnknownValueError:
            print("Error")
        except sr.RequestError as e:
            print("failed".format(e))            
