from typing import Any

import requests

from graphql_client.client.base import GraphQLBaseClient


class GraphQLClient(GraphQLBaseClient):
    def send(
        self,
        *,
        query: str,
        operation_name: str,
        variables: str | dict[str, Any],
        headers: dict[str, Any] | None = None,
        cookies: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Send request to outer Graphql service and return received data."""
        if headers is None:
            headers = dict()
        if cookies is None:
            cookies = dict()
        headers.update(self._headers)
        cookies.update(self._cookies)

        request_data = self._build_send_data(
            query=query, operation_name=operation_name, variables=variables
        )

        response = requests.post(
            self._url,
            data=request_data,
            headers=headers,
            cookies=cookies,
            timeout=self._timeout,
        )

        return response.json()
