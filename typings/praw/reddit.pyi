"""
This type stub file was generated by pyright.
"""

from typing import IO, TYPE_CHECKING, Any, Generator, Iterable

import praw.models
import prawcore
from prawcore import Requestor

from . import models
from .util import _deprecate_args
from .util.token_manager import BaseTokenManager

"""Provide the Reddit class."""
UPDATE_CHECKER_MISSING = ...
if TYPE_CHECKING:
    ...
Comment = models.Comment
Redditor = models.Redditor
Submission = models.Submission
Subreddit = models.Subreddit
logger = ...
class Reddit:
    """The Reddit class provides convenient access to Reddit's API.

    Instances of this class are the gateway to interacting with Reddit's API through
    PRAW. The canonical way to obtain an instance of this class is via:

    .. code-block:: python

        import praw

        reddit = praw.Reddit(
            client_id="CLIENT_ID",
            client_secret="CLIENT_SECRET",
            password="PASSWORD",
            user_agent="USERAGENT",
            username="USERNAME",
        )

    """
    update_checked = ...
    _ratelimit_regex = ...
    @property
    def read_only(self) -> bool:
        """Return ``True`` when using the ``ReadOnlyAuthorizer``."""
        ...
    
    @read_only.setter
    def read_only(self, value: bool): # -> None:
        """Set or unset the use of the ReadOnlyAuthorizer.

        :raises: :class:`.ClientException` when attempting to unset ``read_only`` and
            only the ``ReadOnlyAuthorizer`` is available.

        """
        ...
    
    @property
    def validate_on_submit(self) -> bool:
        """Get validate_on_submit.

        .. deprecated:: 7.0

            If property :attr:`.validate_on_submit` is set to ``False``, the behavior is
            deprecated by Reddit. This attribute will be removed around May-June 2020.

        """
        ...
    
    @validate_on_submit.setter
    def validate_on_submit(self, val: bool): # -> None:
        ...
    
    def __enter__(self): # -> Self:
        """Handle the context manager open."""
        ...
    
    def __exit__(self, *_: object): # -> None:
        """Handle the context manager close."""
        ...
    
    @_deprecate_args("site_name", "config_interpolation", "requestor_class", "requestor_kwargs", "token_manager")
    def __init__(self, site_name: str | None = ..., *, config_interpolation: str | None = ..., requestor_class: type[prawcore.requestor.Requestor] | None = ..., requestor_kwargs: dict[str, Any] | None = ..., token_manager: BaseTokenManager | None = ..., **config_settings: str | bool | int | None) -> None:
        """Initialize a :class:`.Reddit` instance.

        :param site_name: The name of a section in your ``praw.ini`` file from which to
            load settings from. This parameter, in tandem with an appropriately
            configured ``praw.ini``, file is useful if you wish to easily save
            credentials for different applications, or communicate with other servers
            running Reddit. If ``site_name`` is ``None``, then the site name will be
            looked for in the environment variable ``praw_site``. If it is not found
            there, the ``DEFAULT`` site will be used (default: ``None``).
        :param config_interpolation: Config parser interpolation type that will be
            passed to :class:`.Config` (default: ``None``).
        :param requestor_class: A class that will be used to create a requestor. If not
            set, use ``prawcore.Requestor`` (default: ``None``).
        :param requestor_kwargs: Dictionary with additional keyword arguments used to
            initialize the requestor (default: ``None``).
        :param token_manager: When provided, the passed instance, a subclass of
            :class:`.BaseTokenManager`, will manage tokens via two callback functions.
            This parameter must be provided in order to work with refresh tokens
            (default: ``None``).

        Additional keyword arguments will be used to initialize the :class:`.Config`
        object. This can be used to specify configuration settings during instantiation
        of the :class:`.Reddit` instance. For more details, please see
        :ref:`configuration`.

        Required settings are:

        - ``client_id``
        - ``client_secret`` (for installed applications set this value to ``None``)
        - ``user_agent``

        The ``requestor_class`` and ``requestor_kwargs`` allow for customization of the
        requestor :class:`.Reddit` will use. This allows, e.g., easily adding behavior
        to the requestor or wrapping its |Session|_ in a caching layer. Example usage:

        .. |Session| replace:: ``Session``

        .. _session: https://2.python-requests.org/en/master/api/#requests.Session

        .. code-block:: python

            import json

            import betamax
            import requests
            from prawcore import Requestor

            from praw import Reddit


            class JSONDebugRequestor(Requestor):
                def request(self, *args, **kwargs):
                    response = super().request(*args, **kwargs)
                    print(json.dumps(response.json(), indent=4))
                    return response


            my_session = betamax.Betamax(requests.Session())
            reddit = Reddit(
                ..., requestor_class=JSONDebugRequestor, requestor_kwargs={"session": my_session}
            )

        """
        ...
    
    @_deprecate_args("id", "url")
    def comment(self, id: str | None = ..., *, url: str | None = ...) -> models.Comment:
        """Return a lazy instance of :class:`.Comment`.

        :param id: The ID of the comment.
        :param url: A permalink pointing to the comment.

        .. note::

            If you want to obtain the comment's replies, you will need to call
            :meth:`~.Comment.refresh` on the returned :class:`.Comment`.

        """
        ...
    
    @_deprecate_args("path", "data", "json", "params")
    def delete(self, path: str, *, data: dict[str, str | Any] | bytes | IO | str | None = ..., json: dict[Any, Any] | list[Any] | None = ..., params: str | dict[str, str] | None = ...) -> Any:
        """Return parsed objects returned from a DELETE request to ``path``.

        :param path: The path to fetch.
        :param data: Dictionary, bytes, or file-like object to send in the body of the
            request (default: ``None``).
        :param json: JSON-serializable object to send in the body of the request with a
            Content-Type header of application/json (default: ``None``). If ``json`` is
            provided, ``data`` should not be.
        :param params: The query parameters to add to the request (default: ``None``).

        """
        ...
    
    def domain(self, domain: str) -> models.DomainListing:
        """Return an instance of :class:`.DomainListing`.

        :param domain: The domain to obtain submission listings for.

        """
        ...
    
    @_deprecate_args("path", "params")
    def get(self, path: str, *, params: str | dict[str, str | int] | None = ...) -> Any:
        """Return parsed objects returned from a GET request to ``path``.

        :param path: The path to fetch.
        :param params: The query parameters to add to the request (default: ``None``).

        """
        ...
    
    @_deprecate_args("fullnames", "url", "subreddits")
    def info(self, *, fullnames: Iterable[str] | None = ..., subreddits: Iterable[praw.models.Subreddit | str] | None = ..., url: str | None = ...) -> Generator[praw.models.Subreddit | praw.models.Comment | praw.models.Submission, None, None,]:
        """Fetch information about each item in ``fullnames``, ``url``, or ``subreddits``.

        :param fullnames: A list of fullnames for comments, submissions, and/or
            subreddits.
        :param subreddits: A list of subreddit names or :class:`.Subreddit` objects to
            retrieve subreddits from.
        :param url: A url (as a string) to retrieve lists of link submissions from.

        :returns: A generator that yields found items in their relative order.

        Items that cannot be matched will not be generated. Requests will be issued in
        batches for each 100 fullnames.

        .. note::

            For comments that are retrieved via this method, if you want to obtain its
            replies, you will need to call :meth:`~.Comment.refresh` on the yielded
            :class:`.Comment`.

        .. note::

            When using the URL option, it is important to be aware that URLs are treated
            literally by Reddit's API. As such, the URLs ``"youtube.com"`` and
            ``"https://www.youtube.com"`` will provide a different set of submissions.

        """
        ...
    
    @_deprecate_args("path", "data", "json")
    def patch(self, path: str, *, data: dict[str, str | Any] | bytes | IO | str | None = ..., json: dict[Any, Any] | list[Any] | None = ..., params: str | dict[str, str] | None = ...) -> Any:
        """Return parsed objects returned from a PATCH request to ``path``.

        :param path: The path to fetch.
        :param data: Dictionary, bytes, or file-like object to send in the body of the
            request (default: ``None``).
        :param json: JSON-serializable object to send in the body of the request with a
            Content-Type header of application/json (default: ``None``). If ``json`` is
            provided, ``data`` should not be.
        :param params: The query parameters to add to the request (default: ``None``).

        """
        ...
    
    @_deprecate_args("path", "data", "files", "params", "json")
    def post(self, path: str, *, data: dict[str, str | Any] | bytes | IO | str | None = ..., files: dict[str, IO] | None = ..., json: dict[Any, Any] | list[Any] | None = ..., params: str | dict[str, str] | None = ...) -> Any:
        """Return parsed objects returned from a POST request to ``path``.

        :param path: The path to fetch.
        :param data: Dictionary, bytes, or file-like object to send in the body of the
            request (default: ``None``).
        :param files: Dictionary, filename to file (like) object mapping (default:
            ``None``).
        :param json: JSON-serializable object to send in the body of the request with a
            Content-Type header of application/json (default: ``None``). If ``json`` is
            provided, ``data`` should not be.
        :param params: The query parameters to add to the request (default: ``None``).

        """
        ...
    
    @_deprecate_args("path", "data", "json")
    def put(self, path: str, *, data: dict[str, str | Any] | bytes | IO | str | None = ..., json: dict[Any, Any] | list[Any] | None = ...) -> Any:
        """Return parsed objects returned from a PUT request to ``path``.

        :param path: The path to fetch.
        :param data: Dictionary, bytes, or file-like object to send in the body of the
            request (default: ``None``).
        :param json: JSON-serializable object to send in the body of the request with a
            Content-Type header of application/json (default: ``None``). If ``json`` is
            provided, ``data`` should not be.

        """
        ...
    
    @_deprecate_args("nsfw")
    def random_subreddit(self, *, nsfw: bool = ...) -> praw.models.Subreddit:
        """Return a random lazy instance of :class:`.Subreddit`.

        :param nsfw: Return a random NSFW (not safe for work) subreddit (default:
            ``False``).

        """
        ...
    
    @_deprecate_args("name", "fullname")
    def redditor(self, name: str | None = ..., *, fullname: str | None = ...) -> praw.models.Redditor:
        """Return a lazy instance of :class:`.Redditor`.

        :param name: The name of the redditor.
        :param fullname: The fullname of the redditor, starting with ``t2_``.

        Either ``name`` or ``fullname`` can be provided, but not both.

        """
        ...
    
    @_deprecate_args("method", "path", "params", "data", "files", "json")
    def request(self, *, data: dict[str, str | Any] | bytes | IO | str | None = ..., files: dict[str, IO] | None = ..., json: dict[Any, Any] | list[Any] | None = ..., method: str, params: str | dict[str, str | int] | None = ..., path: str) -> Any:
        """Return the parsed JSON data returned from a request to URL.

        :param data: Dictionary, bytes, or file-like object to send in the body of the
            request (default: ``None``).
        :param files: Dictionary, filename to file (like) object mapping (default:
            ``None``).
        :param json: JSON-serializable object to send in the body of the request with a
            Content-Type header of application/json (default: ``None``). If ``json`` is
            provided, ``data`` should not be.
        :param method: The HTTP method (e.g., ``"GET"``, ``"POST"``, ``"PUT"``,
            ``"DELETE"``).
        :param params: The query parameters to add to the request (default: ``None``).
        :param path: The path to fetch.

        """
        ...
    
    @_deprecate_args("id", "url")
    def submission(self, id: str | None = ..., *, url: str | None = ...) -> praw.models.Submission:
        """Return a lazy instance of :class:`.Submission`.

        :param id: A Reddit base36 submission ID, e.g., ``"2gmzqe"``.
        :param url: A URL supported by :meth:`.Submission.id_from_url`.

        Either ``id`` or ``url`` can be provided, but not both.

        """
        ...
    
    def username_available(self, name: str) -> bool:
        """Check to see if the username is available.

        For example, to check if the username ``bboe`` is available, try:

        .. code-block:: python

            reddit.username_available("bboe")

        """
        ...
    


