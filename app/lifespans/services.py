from app.clients.whisper_client import WhisperClient
from app.clients.ner_client import NERClient
class Services:
    def __init__(self):
        self.whisper = WhisperClient()
        self.ner = NERClient()
        