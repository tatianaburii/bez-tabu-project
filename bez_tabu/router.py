from typing import Callable, Sequence, Optional
from bez_tabu.address_book import AddressBook
from bez_tabu.note_book import NoteBook

from bez_tabu.handler import (
    add_contact, edit_contact, delete_contact, find_contacts, show_contact, list_contacts, upcoming_birthdays, add_note,
    search_notes, edit_note, delete_note, list_notes, help_command,
)

Handler = Callable[[Sequence[str], AddressBook, NoteBook], Optional[str]]

COMMANDS: dict[str, Handler] = {
    # contacts
    "add": add_contact,
    "edit": edit_contact,
    "delete": delete_contact,
    "find": find_contacts,
    "show": show_contact,
    "all": list_contacts,
    "birthdays": upcoming_birthdays,

    # notes
    "note-add": add_note,
    "note-search": search_notes,
    "note-edit": edit_note,
    "note-delete": delete_note,
    "notes": list_notes,

    # help
    "help": help_command,
}

ALIASES: dict[str, str] = {
    # contacts
    "add-contact": "add",
    "remove": "delete",
    "ls": "all",
    "show-contact": "show",
    "search": "find",

    # notes
    "add-note": "note-add",
    "find-notes": "note-search",
    "edit-note": "note-edit",
    "rm-note": "note-delete",

    # misc
    "?": "help",
    "h": "help",
    "q": "exit",
    "quit": "exit",
}

TERMINATE = {"exit", "close"}


def normalize(cmd: str) -> str:
    cmd = cmd.strip().lower()
    return ALIASES.get(cmd, cmd)


def dispatch(command: str, args: Sequence[str], book: AddressBook, note_book: NoteBook) -> Optional[str]:
    cmd = normalize(command)
    if cmd in TERMINATE:
        return "__EXIT__"
    handler = COMMANDS.get(cmd)
    if not handler:
        return "Invalid command. Type 'help' to see available commands."
    
    if cmd in {"note-add", "note-search", "note-edit", "note-delete", "notes"}:
        return handler(args, note_book)

    return handler(args, book)
