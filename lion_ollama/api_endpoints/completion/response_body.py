from typing import Optional
from pydantic import Field
from ..data_models import OllamaEndpointResponseBody


class OllamaStreamCompletionResponseBody(OllamaEndpointResponseBody):
    model: str = Field(description="The model name")

    created_at: str = Field(description="The timestamp when the response was created")

    response: str = Field(description="he partial or full response generated by the model")

    done: bool = Field(description="A flag indicating whether the response generation is complete")


class OllamaCompletionResponseBody(OllamaStreamCompletionResponseBody):
    total_duration: int = Field(description="Time spent generating the response")

    load_duration: int = Field(description="Time spent in nanoseconds loading the model")

    prompt_eval_count: int = Field(description="number of tokens in the prompt")

    prompt_eval_duration: int = Field(description="time spent in nanoseconds evaluating the prompt")

    eval_count: int = Field(description="number of tokens in the response")

    eval_duration: int = Field(description="time in nanoseconds spent generating the response")

    context: Optional[list] = Field(
        None,
        description="an encoding of the conversation used in this response, "
                    "this can be sent in the next request to keep a conversational memory"
    )