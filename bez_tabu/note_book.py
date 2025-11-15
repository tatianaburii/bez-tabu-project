from bez_tabu.note import Note
from typing import List, Optional


class NoteBook:
    def __init__(self):
        self.notes = []

    def add_note(self, note: Note) -> bool:
        self.notes.append(note)
        return True

    def get_all_notes(self) -> List[Note]:
        return self.notes
