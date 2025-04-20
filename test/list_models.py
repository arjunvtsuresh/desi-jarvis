from TTS.api import TTS

# Create an instance of TTS
tts_instance = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC")

# Call list_models on the instance
print(tts_instance.list_models())