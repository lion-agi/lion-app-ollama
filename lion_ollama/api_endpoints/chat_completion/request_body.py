from typing import Optional, Literal, List
from pydantic import Field
from ..data_models import OllamaEndpointRequestBody
from .message_models import Message
from ..option_models import Option
from .tool_models import Tool


class OllamaChatCompletionRequestBody(OllamaEndpointRequestBody):
    model: str = Field(description="The model name")

    messages: List[Message] = Field(description="The messages of the chat, this can be used to keep a chat memory")

    tools: Optional[List[Tool]] = Field(
        None,
        description="Tools for the model to use if supported. Requires 'stream' to be set to false"
    )

    format: Optional[Literal["json"]] = Field(
        None,
        description="The format to return a response in. Currently the only accepted value is 'json'"
    )

    options: Optional[Option] = Field(
        None,
        description="Additional model parameters listed in the documentation for the Modelfile"
    )

    stream: bool = Field(
        True,
        description="If false the response will be returned as a single response object, "
                    "rather than a stream of objects"
    )

    keep_alive: str = Field(
        "5m",
        description="Controls how long the model will stay loaded into memory following the request."
    )
