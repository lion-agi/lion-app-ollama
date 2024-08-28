from ollama import AsyncClient

allowed_kwargs = [
    "model",
    "frequency_penalty",
    # "max_tokens",
    "n",
    "presence_penalty",
    "response_format",
    "seed",
    "stop",
    "stream",
    # "temperature",
    "top_p",
    "tools",
    "tool_choice",
    "user",
]


class OllamaService(BaseService):

    def __init__(self, model: str = model, **kwargs):
        super().__init__()
        self.model = model
        self.client = AsyncClient()
        self.allowed_kwargs = allowed_kwargs

    async def serve_chat(self, messages, **kwargs):
        config = {}
        for k, v in kwargs.items():
            if k in allowed_kwargs:
                config[k] = v

        self.ollama.pull(self.model)
        payload = {"messages": messages}
        if "model" not in config:
            config["model"] = self.model

        try:
            completion = await self.client.chat(messages=messages, **config)
            completion["choices"] = [{"message": completion.pop("message")}]
            return payload, completion
        except Exception as e:
            self.status_tracker.num_tasks_failed += 1
            raise e