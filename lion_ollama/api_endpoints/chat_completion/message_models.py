from typing import Optional, List
from pydantic import BaseModel, Field
from enum import Enum


class Role(str, Enum):
    SYSTEM = "system"
    USER = "user"
    ASSISTANT = "assistant"
    TOOL = "tool"


class Message(BaseModel):
    role: Role = Field(description="The role of the message, either 'system', 'user', 'assistant', or 'tool'")

    content: str = Field(description="The content of the message")

    images: Optional[List[str]] = Field(
        None,
        description="a list of images to include in the message (for multimodal models such as 'llava')"
    )

    tool_calls: Optional[list] = Field(None, description="a list of tools the model wants to use")
