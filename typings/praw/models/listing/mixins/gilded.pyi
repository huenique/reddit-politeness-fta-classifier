"""
This type stub file was generated by pyright.
"""

from typing import Any, Iterator

from ...base import PRAWBase

"""Provide the GildedListingMixin class."""
class GildedListingMixin(PRAWBase):
    """Mixes in the gilded method."""
    def gilded(self, **generator_kwargs: str | int | dict[str, str]) -> Iterator[Any]:
        """Return a :class:`.ListingGenerator` for gilded items.

        Additional keyword arguments are passed in the initialization of
        :class:`.ListingGenerator`.

        For example, to get gilded items in r/test:

        .. code-block:: python

            for item in reddit.subreddit("test").gilded():
                print(item.id)

        """
        ...
    


