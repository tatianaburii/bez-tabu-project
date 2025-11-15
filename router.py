from typing import Callable, Sequence, Optional
from address_book import AddressBook
from note_book import NoteBook

from handler import (
    add_contact, edit_contact, delete_contact, find_contacts, show_contact, list_contacts, upcoming_birthdays,
    add_note, search_notes, edit_note, delete_note, list_notes, help_command,
    add_note_tags, remove_note_tags, search_notes_by_tags, sort_notes_by_tags
)

HandlerAB = Callable[[Sequence[str], AddressBook], Optional[str]]
HandlerNB = Callable[[Sequence[str], NoteBook], Optional[str]]
Handler = Callable[[Sequence[str], AddressBook, NoteBook], Optional[str]]

def adapt_ab(h: HandlerAB) -> Handler:
    def wrapper(args: Sequence[str], book: AddressBook, note_book: NoteBook) -> Optional[str]:
        return h(args, book)
    return wrapper

def adapt_nb(h: HandlerNB) -> Handler:
    def wrapper(args: Sequence[str], book: AddressBook, note_book: NoteBook) -> Optional[str]:
        return h(args, note_book)
    return wrapper

COMMANDS: dict[str, Handler] = {
    # contacts
    "add": adapt_ab(add_contact),
    "edit": adapt_ab(edit_contact),
    "delete": adapt_ab(delete_contact),
    "find": adapt_ab(find_contacts),
    "show": adapt_ab(show_contact),
    "all": adapt_ab(list_contacts),
    "birthdays": adapt_ab(upcoming_birthdays),

    # notes
    "note-add": adapt_nb(add_note),
    "note-search": adapt_nb(search_notes),
    "note-edit": adapt_nb(edit_note),
    "note-delete": adapt_nb(delete_note),
    "notes": adapt_nb(list_notes),

    # tags
    "note-tags-add": adapt_nb(add_note_tags),
    "note-tags-remove": adapt_nb(remove_note_tags),
    "note-tags-search": adapt_nb(search_notes_by_tags),
    "note-sort": adapt_nb(sort_notes_by_tags),

    # help
    "help": adapt_ab(help_command),
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

    # tag aliases
    "add-tags": "note-tags-add",
    "tag-add": "note-tags-add",
    "tags-add": "note-tags-add",

    "rm-tags": "note-tags-remove",
    "tag-rm": "note-tags-remove",
    "remove-tags": "note-tags-remove",

    "find-tags": "note-tags-search",
    "search-tags": "note-tags-search",
    "note-search-tags": "note-tags-search",

    "sort-notes": "note-sort",
    "notes-sort": "note-sort",

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
    return handler(args, book, note_book)
