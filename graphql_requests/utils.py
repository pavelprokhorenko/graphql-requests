from os import path


def to_camel_case(snake_str: str) -> str:
    components = snake_str.split("_")
    return components[0] + "".join(x.title() for x in components[1:])


def dict_keys_to_camel_case_recursively(d: dict) -> dict:
    return {
        to_camel_case(key): dict_keys_to_camel_case_recursively(value)
        if isinstance(value, dict)
        else value
        for key, value in d.items()
    }


def read_scheme_from_file(file_path: str, *, encoding: str = "UTF-8") -> str:
    with open(file_path, "r+", encoding=encoding) as f:
        return f.read()


def get_dir_from_file_path(file_path: str) -> str:
    return path.dirname(path.realpath(file_path))
