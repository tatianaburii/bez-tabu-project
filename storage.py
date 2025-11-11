# storage.py
from __future__ import annotations
from typing import Protocol, Any, Mapping

from address_book import AddressBook


class Serializer(Protocol):

    def dumps_book(self, book: AddressBook) -> Mapping[str, Any]:
        # your implementation
        pass

    def loads_book(self, payload: Mapping[str, Any]) -> AddressBook:
        # your implementation
        pass