class BaseError(Exception):
    """An error that occurred during validation."""

    pass


class UnsupportedMediaTypeError(BaseError):
    """Invalid Media Type"""

    pass
