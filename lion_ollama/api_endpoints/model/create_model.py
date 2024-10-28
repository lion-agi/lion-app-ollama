from typing import Optional
from pydantic import Field
from ..data_models import OllamaEndpointRequestBody, OllamaEndpointResponseBody


class OllamaCreateModelRequestBody(OllamaEndpointRequestBody):
    name: str = Field(description="name of the model to create")

    modelfile: Optional[str] = Field(None, description="Contents of the Modelfile")

    stream: Optional[bool] = Field(
        True,
        description="if 'false' the response will be returned as a single response object, "
                    "rather than a stream of objects")

    path: Optional[str] = Field(None, description="path to the Modelfile")


class OllamaCreateModelResponseBody(OllamaEndpointResponseBody):
    status: str = Field(None)
