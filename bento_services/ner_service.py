# bento_services/ner_service.py

import bentoml
from gliner import GLiNER
import torch
import logfire
import os
from dotenv import load_dotenv
from app.schemas.NER import NEROutput , NerRequest

# Load .env
load_dotenv()

token = os.getenv("LOGFIRE_TOKEN")
if token is None:
    raise ValueError("token logfire not available")

# Logfire Configuration
logfire.configure(
    token=token,
    service_name="NERService",
    distributed_tracing=True,
)

image = (
    bentoml.images.Image(
        base_image="python:3.11-slim"
    )
    .run(
        "pip install --no-cache-dir torch torchvision torchaudio "
        "--index-url https://download.pytorch.org/whl/cu124"
    )
    .python_packages(
        "bentoml==1.4.38",
        "gliner==0.2.24",
        "logfire==4.32.1",
        "python-dotenv>=1.2.2",
    )
    .run(
        'python -c "from gliner import GLiNER; '
        'GLiNER.from_pretrained(\'Ihor/gliner-biomed-large-v1.0\')"'
    )
)
# Hugging Face Token
token = os.getenv("HF_TOKEN")
if token is None:
    raise ValueError("Hugging Face token not available")


# Starting the BentoML Service
@bentoml.service(
    image=image,
    resources={"gpu": 1},
    traffic={"timeout": 300},
)
class NERService:
    def __init__(self):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"

        self.model = GLiNER.from_pretrained(
            "Ihor/gliner-biomed-large-v1.0",
            token=token,
        )

        self.model.to(self.device)

        # Put the model in inference/evaluation mode
        self.model.eval()

        logfire.info(
            "GliNER Initialization",
            torch=torch.__version__,
            CUDA_build=torch.version.cuda,
            CUDA_available=torch.cuda.is_available(),
            GLiNER_loaded_on=self.device,
        )

        self.labels = [
            "disease",
            "medication",
            "symptom",
            "lab test",
            "lab test value",
            "dosage",
            "drug frequency",
            "demographic information",
        ]

    # GLiNER predict
    @bentoml.api
    def extract_entities(self, NerRequest: NerRequest) -> NEROutput:
        with logfire.span(
            "Gliner predict",
            text_length=len(NerRequest.text),
        ):
            # Disable gradient tracking during inference
            with torch.inference_mode():
                entities = self.model.predict_entities(
                    NerRequest.text,
                    self.labels,
                    threshold=0.5,
                )

            return NEROutput(entities=entities)