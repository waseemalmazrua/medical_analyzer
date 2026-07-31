from pydantic import BaseModel


class PingResponse(BaseModel):
    status: str