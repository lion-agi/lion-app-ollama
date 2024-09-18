from typing import Optional, List, Literal
from pydantic import Field
from ..data_models import OllamaEndpointRequestBody
from ..option_models import Option


class OllamaCompletionRequestBody(OllamaEndpointRequestBody):
    model: str = Field(description="The model name")

    prompt: str = Field(None, description="The prompt to generate a response for")

    suffix: Optional[str] = Field(None, description="The text after the model response")

    images: Optional[List[str]] = Field(
        None,
        description="A list of base64-encoded images (for multimodal models such as 'llava')"
    )

    format: Optional[Literal["json"]] = Field(
        None,
        description="The format to return a response in. Currently the only accepted value is 'json'"
    )

    options: Optional[Option | dict] = Field(
        None,
        description="Additional model parameters listed in the documentation for the 'Modelfile'"
    )

    system: Optional[str] = Field(
        None,
        description="System message to (overrides what is defined in the 'Modelfile')"
    )

    template: Optional[str] = Field(
        None,
        description="The prompt template to use (overrides what is defined in the 'Modelfile')"
    )

    context: Optional[List[int]] = Field(
        None,
        description="The context parameter returned from a previous request to '/generate', "
                    "this can be used to keep a short conversational memory"
    )

    stream: bool = Field(
        True,
        description="If 'false' the response will be returned as a single response object, "
                    "rather than a stream of objects"
    )

    raw: bool = Field(
        False,
        description="if 'true' no formatting will be applied to the prompt. "
                    "You may choose to use the 'raw' parameter if you are specifying a full templated "
                    "prompt in your request to the API"
    )

    keep_alive: str = Field(
        "5m",
        description="Controls how long the model will stay loaded into memory following the request."
    )
