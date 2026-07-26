from app.clients.ner_client import NERClient
from app.clients.whisper_client import WhisperClient


class Services:
    def __init__(self):
        self.whisper = WhisperClient()
        self.ner = NERClient()
