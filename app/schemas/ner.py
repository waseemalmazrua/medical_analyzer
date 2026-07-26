from pydantic import BaseModel


class Entity(BaseModel):
    text: str
    label: str
    score: float


class NEROutput(BaseModel):
    entities: list[Entity]


class NerRequest(BaseModel):
    text: str
