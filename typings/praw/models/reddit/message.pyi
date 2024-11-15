"""
This type stub file was generated by pyright.
"""

from typing import TYPE_CHECKING, Any

import praw.models

from .base import RedditBase
from .mixins import FullnameMixin, InboxableMixin, ReplyableMixin

"""Provide the Message class."""
if TYPE_CHECKING:
    ...
class Message(InboxableMixin, ReplyableMixin, FullnameMixin, RedditBase):
    """A class for private messages.

    .. include:: ../../typical_attributes.rst

    =============== ================================================================
    Attribute       Description
    =============== ================================================================
    ``author``      Provides an instance of :class:`.Redditor`.
    ``body``        The body of the message, as Markdown.
    ``body_html``   The body of the message, as HTML.
    ``created_utc`` Time the message was created, represented in `Unix Time`_.
    ``dest``        Provides an instance of :class:`.Redditor`. The recipient of the
                    message.
    ``id``          The ID of the message.
    ``name``        The full ID of the message, prefixed with ``t4_``.
    ``subject``     The subject of the message.
    ``was_comment`` Whether or not the message was a comment reply.
    =============== ================================================================

    .. _unix time: https://en.wikipedia.org/wiki/Unix_time

    """
    STR_FIELD = ...
    @classmethod
    def parse(cls, data: dict[str, Any], reddit: praw.Reddit) -> Message | SubredditMessage:
        """Return an instance of :class:`.Message` or :class:`.SubredditMessage` from ``data``.

        :param data: The structured data.
        :param reddit: An instance of :class:`.Reddit`.

        """
        ...
    
    @property
    def parent(self) -> praw.models.Message | None:
        """Return the parent of the message if it exists."""
        ...
    
    @parent.setter
    def parent(self, value: praw.models.Message | None): # -> None:
        ...
    
    def __init__(self, reddit: praw.Reddit, _data: dict[str, Any]) -> None:
        """Initialize a :class:`.Message` instance."""
        ...
    
    def delete(self): # -> None:
        """Delete the message.

        .. note::

            Reddit does not return an indication of whether or not the message was
            successfully deleted.

        For example, to delete the most recent message in your inbox:

        .. code-block:: python

            next(reddit.inbox.all()).delete()

        """
        ...
    


class SubredditMessage(Message):
    """A class for messages to a subreddit.

    .. include:: ../../typical_attributes.rst

    =============== =================================================================
    Attribute       Description
    =============== =================================================================
    ``author``      Provides an instance of :class:`.Redditor`.
    ``body``        The body of the message, as Markdown.
    ``body_html``   The body of the message, as HTML.
    ``created_utc`` Time the message was created, represented in `Unix Time`_.
    ``dest``        Provides an instance of :class:`.Redditor`. The recipient of the
                    message.
    ``id``          The ID of the message.
    ``name``        The full ID of the message, prefixed with ``t4_``.
    ``subject``     The subject of the message.
    ``subreddit``   If the message was sent from a subreddit, provides an instance of
                    :class:`.Subreddit`.
    ``was_comment`` Whether or not the message was a comment reply.
    =============== =================================================================

    .. _unix time: https://en.wikipedia.org/wiki/Unix_time

    """
    def mute(self): # -> None:
        """Mute the sender of this :class:`.SubredditMessage`.

        For example, to mute the sender of the first :class:`.SubredditMessage` in the
        authenticated users' inbox:

        .. code-block:: python

            from praw.models import SubredditMessage

            msg = next(
                message for message in reddit.inbox.all() if isinstance(message, SubredditMessage)
            )
            msg.mute()

        """
        ...
    
    def unmute(self): # -> None:
        """Unmute the sender of this :class:`.SubredditMessage`.

        For example, to unmute the sender of the first :class:`.SubredditMessage` in the
        authenticated users' inbox:

        .. code-block:: python

            from praw.models import SubredditMessage

            msg = next(
                message for message in reddit.inbox.all() if isinstance(message, SubredditMessage)
            )
            msg.unmute()

        """
        ...
    


