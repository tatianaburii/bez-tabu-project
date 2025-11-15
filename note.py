import uuid

class Note:
    def __init__(self, text: str):
        self.id = str(uuid.uuid4())[:8]
        self.text = text

    def __str__(self) -> str:
        return f"[{self.id}]: {self.text}"
