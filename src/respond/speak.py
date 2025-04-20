
import os
from TTS.api import TTS
from llm.model_manger import Manager
from llm.texttospeech import DEFAULT_MODEL

# Initialize TTS
tts_manager = Manager(model_name=DEFAULT_MODEL,progressBar=False, gpu=False)
tts = tts_manager.get_tts()

class Speak:

    def __init__(self, text):
        self.text = text

    def speak(self):
        output_file = "metadata/response.wav"
        tts.tts_to_file(text=self.text, file_path=output_file)
        os.system("start metadata/response.wav" if os.name == 'nt' else "afplay metadata/response.wav" if os.uname().sysname == 'Darwin' else "aplay metadata/response.wav")
