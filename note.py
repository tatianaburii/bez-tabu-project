import uuid
from typing import Iterable, List, Set


class Note:
    def __init__(self, text: str, tags: Iterable[str] | None = None):
        self.id = str(uuid.uuid4())[:8]
        self.text = text
        self._tags: Set[str] = set(t.strip().lower() for t in (tags or []) if t and t.strip())

    @property
    def tags(self) -> List[str]:
        return sorted(self._tags)

    def add_tags(self, *tags: str) -> str:
        for t in tags:
            if t and t.strip():
                self._tags.add(t.strip().lower())
        return "Tags added"

    def remove_tags(self, *tags: str) -> str:
        for t in tags:
            if t:
                self._tags.discard(t.strip().lower())
        return "Tags removed"

    def has_tag(self, tag: str) -> bool:
        return tag.strip().lower() in self._tags if tag else False

    def __str__(self) -> str:
        tags_part = f" #{' #'.join(self.tags)}" if self._tags else ""
        return f"[{self.id}]: {self.text}{tags_part}"
