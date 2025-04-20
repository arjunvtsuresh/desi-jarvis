import requests

class OllamModel:
    def __init__(self, model_name: str , prompt:str):
        self.model_name = model_name
        self.prompt = prompt

    def get_response(self):
        response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": "llama3.2", "prompt": self.prompt, "stream": False}
        )
        return response.json()["response"]
