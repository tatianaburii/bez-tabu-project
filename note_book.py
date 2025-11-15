from __future__ import annotations
from typing import List, Optional, Iterable
from note import Note


class NoteBook:
    def __init__(self) -> None:
        self.notes: List[Note] = []

    def add_note(self, note: Note) -> str:
        self.notes.append(note)
        return "Note added."

    def get_all_notes(self) -> List[Note]:
        return list(self.notes)

    def find_by_id(self, note_id: str) -> Optional[Note]:
        for n in self.notes:
            if getattr(n, "id", None) == note_id:
                return n
        return None

    def edit_note_text(self, note_id: str, new_text: str) -> bool:
        n = self.find_by_id(note_id)
        if not n:
            return False
        n.text = new_text
        return True

    def set_note_tags(self, note_id: str, tags: Iterable[str]) -> bool:
        n = self.find_by_id(note_id)
        if not n:
            return False
        n._tags.clear()
        for t in tags:
            if t and t.strip():
                n._tags.add(t.strip().lower())
        return True

    def delete_note(self, note_id: str) -> bool:
        n = self.find_by_id(note_id)
        if not n:
            return False
        self.notes.remove(n)
        return True

    # Search & sort
    def find_notes_by_text(self, query: str) -> List[Note]:
        q = (query or "").lower()
        if not q:
            return []
        return [n for n in self.notes if q in n.text.lower()]

    def find_notes_by_tags(self, tags: Iterable[str], match_all: bool = False) -> List[Note]:
        wanted = {t.strip().lower() for t in (tags or []) if t and t.strip()}
        if not wanted:
            return []
        res: List[Note] = []
        for n in self.notes:
            note_tags = set(n.tags)
            if match_all and wanted.issubset(note_tags):
                res.append(n)
            elif not match_all and note_tags.intersection(wanted):
                res.append(n)
        return res

    def sort_notes_by_tags(self, mode: str = "alphabetical") -> List[Note]:
        if mode == "count":
            return sorted(self.notes, key=lambda n: (-len(n.tags), n.tags[0] if n.tags else "~~~~"))
        return sorted(self.notes, key=lambda n: (n.tags[0] if n.tags else "~~~~", n.text.lower()))

    def format_notes(self, notes: List[Note]) -> str:
        if not notes:
            return "No notes."
        return "\n".join(str(n) for n in notes)
