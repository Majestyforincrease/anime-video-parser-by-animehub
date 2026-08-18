class ParserError(Exception):
    """Base error for parsing and validation failures."""


class UnsupportedProvider(ParserError):
    """Raised when no adapter is registered for a provider."""


class InvalidVideoUrl(ParserError):
    """Raised when a candidate URL fails provider allow-list checks."""

