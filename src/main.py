import speech_recognition as sr
from TTS.api import TTS
import requests
from llm.texttospeech import TextToSpeech
from llm.model import OllamModel
from respond.speak import Speak
import pyfiglet

# setup reconizer Modules
reconginzer = sr.Recognizer()

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%%%%%%%%%%%%%STARTING JARVIS%%%%%%%%%%%%%
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

print(pyfiglet.figlet_format("MALLU-JARVIS", font="slant"))

try:
    while True:
        with sr.Microphone() as source:
            print("Listening...")
            audio = reconginzer.listen(source)
            text = reconginzer.recognize_google(audio)
            print("You said:", text)
            model = OllamModel(model_name="llama3.2", prompt=text)
            response = model.get_response()
            print("Response:", response)
            output = Speak(response)
            # print("Response:", response)
            output.speak()
except KeyboardInterrupt:
    print("Stopped by User")
except sr.UnknownValueError:
    print("Could not understand the audio")
except sr.RequestError as e:
    print(f"Could not request results; {e}")
except Exception as e:
    print(f"An error occurred: {e}")