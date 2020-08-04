# ### Google Text To Speech ###

# ==============================
from gtts import gTTS

mytext = 'Hello World'
language = 'en'

output = gTTS(text=mytext, lang=language, slow=False)

with open('tts-en-hello-world.mp3', 'wb') as file:
    output.write_to_fp(file)

url = output.get_urls()
print(url)

output.save('output.mp3')

# ------------------------------
# get_urls() - Get TTS API request URL(s) that would be sent to the TTS API.
# save(file_name.extension) - Do the TTS API request and write result to file.
# write_to_fp(file_name.extension) - Do the TTS API request(s) and write bytes to a file-like object.
