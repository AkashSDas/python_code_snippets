# ###### pyttsx3 ######

# ==============================
# Using this module we can convert text to speech when we are offline
# ==============================
# ### Importing pyttsx3 module ###
import pyttsx3
# ==============================
# ### Basics ###

engine = pyttsx3.init()
engine.say("I will speak this text")
engine.runAndWait()
# ==============================
# ### To get the available voices ###

voices = engine.getProperty('voices')
# ==============================
# ### To get a less robotic voice we can try to change the voice as follows ###

engine.setProperty('voice', voice.id)
# ==============================
# ### Looping over all voices ###

voices = engine.getProperty('voices')
for voice in voices:
   engine.setProperty('voice', voice.id)  # changes the voice
   print(voice.id)
   engine.say('The quick brown fox jumped over the lazy dog.')
engine.runAndWait()
# ==============================
# ### We don't have to cycle, we can set voice id without a for loop ###

engine = pyttsx3.init()
voice_id = 'com.apple.speech.synthesis.voice.Alex'
engine.setProperty('voice', voice_id)  # We can use whatever voice_id we like
engine.say('I will speak this text')
engine.runAndWait()
# ==============================
# pttsx3 supports three TTS engines:
#     - sapi5 – SAPI5 on Windows
#     - nsss – NSSpeechSynthesizer on Mac OS X
#     - espeak – eSpeak on every other platform
# ==============================
# ### To change dirver ###

pyttsx3.init(driverName='sapi5')
