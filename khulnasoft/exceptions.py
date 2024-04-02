class KhulnasoftError(Exception):
    """Base class for all custom exceptions in the Khulnasoft application."""


class BadRequestError(KhulnasoftError):
    """Exception raised for HTTP 400 Bad Request errors."""


class AuthenticationError(KhulnasoftError):
    """Exception raised for HTTP 401 Unauthorized errors."""


class PermissionDeniedError(KhulnasoftError):
    """Exception raised for HTTP 403 Forbidden errors."""


class NotFoundError(KhulnasoftError):
    """Exception raised for HTTP 404 Not Found errors."""


class ConflictError(KhulnasoftError):
    """Exception raised for HTTP 409 Conflict errors."""


class UnprocessableEntityError(KhulnasoftError):
    """Exception raised for HTTP 422 Unprocessable Entity errors."""


class RateLimitError(KhulnasoftError):
    """Exception raised for HTTP 429 Too Many Requests errors."""


class InternalServerError(KhulnasoftError):
    """Exception raised for HTTP 500 Internal Server Error errors."""


status_error_map = {
    400: BadRequestError,
    401: AuthenticationError,
    403: PermissionDeniedError,
    404: NotFoundError,
    409: ConflictError,
    422: UnprocessableEntityError,
    429: RateLimitError,
    500: InternalServerError,
}
