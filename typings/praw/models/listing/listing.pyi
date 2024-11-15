"""
This type stub file was generated by pyright.
"""

from typing import Any

from ..base import PRAWBase

"""Provide the Listing class."""
class Listing(PRAWBase):
    """A listing is a collection of :class:`.RedditBase` instances."""
    AFTER_PARAM = ...
    CHILD_ATTRIBUTE = ...
    def __getitem__(self, index: int) -> Any:
        """Return the item at position index in the list."""
        ...
    
    def __len__(self) -> int:
        """Return the number of items in the Listing."""
        ...
    
    def __setattr__(self, attribute: str, value: Any): # -> None:
        """Objectify the ``CHILD_ATTRIBUTE`` attribute."""
        ...
    


class FlairListing(Listing):
    """Special Listing for handling flair lists."""
    CHILD_ATTRIBUTE = ...
    @property
    def after(self) -> Any | None:
        """Return the next attribute or ``None``."""
        ...
    


class ModNoteListing(Listing):
    """Special Listing for handling :class:`.ModNote` lists."""
    AFTER_PARAM = ...
    CHILD_ATTRIBUTE = ...
    @property
    def after(self) -> Any | None:
        """Return the next attribute or None."""
        ...
    


class ModeratorListing(Listing):
    """Special Listing for handling moderator lists."""
    CHILD_ATTRIBUTE = ...


class ModmailConversationsListing(Listing):
    """Special Listing for handling :class:`.ModmailConversation` lists."""
    CHILD_ATTRIBUTE = ...
    @property
    def after(self) -> str | None:
        """Return the next attribute or ``None``."""
        ...
    


