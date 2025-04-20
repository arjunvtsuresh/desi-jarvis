from TTS.api import TTS

# DEFAULT MODEL
DEFAULT_MODEL:str = "tts_models/en/ljspeech/tacotron2-DDC"

class TextToSpeech:

    def __init__(self, progressBar: bool, gpu: bool, model_name:str =DEFAULT_MODEL):
        self.model_name = model_name
        self.progressBar = progressBar
        self.gpu = gpu
    
    def get_tts(self):
        tts = TTS(model_name=self.model_name, progress_bar=self.progressBar, gpu=self.gpu)
        return tts