import re
from typing import Any, Dict

from graphql_requests.utils import (
    dict_keys_to_camel_case_recursively,
    read_scheme_from_file,
)


class GraphQLRequest:
    def __init__(self, *, body: str, variables: Dict[str, Any]) -> None:
        """
        Build request send data for outer GraphQL service
        """
        self._body = body
        self._variables = dict_keys_to_camel_case_recursively(variables)

    def set_variables(self, variables: Dict[str, Any]) -> None:
        """
        Override variables to send
        """
        camel_case_variables = dict_keys_to_camel_case_recursively(variables)
        self._variables = camel_case_variables

    def extend_variables(self, additional_variables: Dict[str, Any]) -> None:
        """
        Add new variables to existing ones
        """
        camel_case_variables = dict_keys_to_camel_case_recursively(additional_variables)
        self._variables.update(camel_case_variables)

    def set_fragment(self, fragment: str) -> None:
        """
        Add GraphQL fragment to request body
        """
        clear_fragment = re.sub(r"[\n\r\s]{2,}", " ", fragment)
        self._body = "{} {}".format(self._body, clear_fragment)

    def set_scheme_from_file(self, file_path: str, *, encoding: str = "UTF-8") -> None:
        """
        Read scheme from file and set it to request body
        """
        self._body = read_scheme_from_file(file_path, encoding=encoding)

    @property
    def body(self) -> str:
        """
        Request scheme
        """
        return self._body

    @property
    def variables(self) -> Dict[str, Any]:
        """
        Request payload
        """
        return self._variables
