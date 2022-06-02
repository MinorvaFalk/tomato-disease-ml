from pydantic import BaseModel

class RequestImageBase64(BaseModel):
    imageString: str