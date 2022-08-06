from typing import Any

import requests

from graphql_requests.client.base import GraphQLBaseClient
from graphql_requests.errors import GraphQLError


class GraphQLClient(GraphQLBaseClient):
    """
    Synchronous GraphQL client
    """

    def send(
        self,
        url: str | None = None,
        *,
        query: str,
        operation_name: str = None,
        variables: str | dict[str, Any] = None,
        headers: dict[str, Any] | None = None,
        cookies: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        """
        Send request to outer Graphql service and return received data
        """
        if headers is None:
            headers = dict()
        if cookies is None:
            cookies = dict()
        headers.update(self._headers or {})
        cookies.update(self._cookies or {})

        if url is not None:
            url = self._base_url.rstrip("/") + "/" + url.lstrip("/")
        else:
            url = self._base_url

        request_data = self._build_send_data(
            query=query, operation_name=operation_name, variables=variables
        )

        response = requests.post(
            url,
            data=request_data,
            headers=headers,
            cookies=cookies,
            timeout=self._timeout,
        )
        response_data = response.json()

        if errors := response_data.get("errors"):
            raise GraphQLError(errors=errors)

        return response_data["data"]
