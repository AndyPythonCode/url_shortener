from pydantic import BaseModel, AnyHttpUrl


class SchemaShortener(BaseModel):
    url: AnyHttpUrl

    class Config:
        schema_extra = {
            "example": {
                "url": "https://example.com",
            }
        }

class SchemaResponseShortener(BaseModel):
    url: AnyHttpUrl
    redirect: AnyHttpUrl
