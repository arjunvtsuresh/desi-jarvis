from llm.texttospeech import TextToSpeech
from TTS.utils.manage import ModelManager


class Manager(TextToSpeech):
    def __init__(self, model_name: str, progressBar: bool, gpu: bool):
        super().__init__(model_name=model_name, progressBar=progressBar, gpu=gpu)
        self.model_name = model_name
        self.progressBar = progressBar
        self.gpu = gpu
        self.tts_module = self
    
    def change_model(self, model_name: str):
        self.model_name = model_name
        super().__init__(model_name=model_name, progressBar=self.progressBar, gpu=self.gpu)
    
    # def get_tts(self):
    #     return self.tts_module

    def list_models(self):
        manager = ModelManager()
        models = manager.list_tts_models()
        return models