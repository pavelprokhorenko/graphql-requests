class GraphQLError(Exception):
    """Base exception for GraphQL clients."""

    def __init__(self, errors: list[dict]) -> None:
        message = "\n".join(
            error.get("message") or "\n".join(error.get("messages")) for error in errors
        )
        super().__init__(message)
