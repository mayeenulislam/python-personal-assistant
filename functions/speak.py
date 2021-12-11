import pyttsx3

# Solve PyAudio problem on Windows by installing necessary .whl file
# https://stackoverflow.com/a/55630212/1743124

# sapi5 is the Microsoft SpeechAPI (SAPI), and we're using v5x
engine = pyttsx3.init('sapi5')

# Set Rate
engine.setProperty('rate', 120)

# Set Volume
engine.setProperty('volume', 1.5)

# Set Voice (Female)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# Text to Speech Conversion
def speak(text):
    """Used to speak whatever text is passed to it"""

    engine.say(text)
    engine.runAndWait()
