from typing import Optional
from pydantic import Field
from ..data_models import OllamaEndpointRequestBody


class OllamaShowModelRequestBody(OllamaEndpointRequestBody):
    name: str = Field(description="Name of the model to show")

    verbose: Optional[bool] = Field(None, description="If set to true, returns full data for verbose response fields")
