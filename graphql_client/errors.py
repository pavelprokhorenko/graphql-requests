class GraphQLError(Exception):
    """Base exception for GraphQL clients."""

    def __init__(self, errors: list[dict]):
        message = "\n".join(
            error.get("message") or "\n".join(error.get("messages"))
            for error in errors
            if error
        )

        super().__init__(message)
