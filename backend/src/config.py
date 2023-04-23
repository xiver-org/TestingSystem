from os import getenv
from typing import NoReturn
from dataclasses import dataclass


__all__ = ('config',)


class EnvVariableUndefined(Exception):
    """Raise when cannot read env variable and getenv return None."""

    def __init__(self, env_name: str) -> None:
        msg = f'Env name="{env_name}"'
        super().__init__(msg)


class CannotRecognizeBoolEnv(Exception):
    """Raise when cannot recognize bool env as python bool varialble."""

    def __init__(self, env_name: str, env_value: str) -> None:
        msg = f'Env name="{env_name}" env value="{env_value}"'
        super().__init__(msg)


def get_bool_env(env_name: str, default: bool | None = None) -> bool | NoReturn:
    env_value = getenv(env_name, None)
    if env_value is None and default is None:
        raise EnvVariableUndefined(env_name)

    if default:
        return default

    if env_value.lower() in ("1", "true", "t", "y", "yes"):
        return True

    if env_value.lower() in ("0", "false", "f", "n", "no"):
        return False

    raise CannotRecognizeBoolEnv(env_name, env_value)


def get_str_env(env_name: str, default: str | None = None) -> str | NoReturn:
    env_value = getenv(env_name, None)
    if env_value is None and default is None:
        raise EnvVariableUndefined(env_name)

    if env_value is None and default is not None:
        return default

    return env_value


def get_int_env(env_name: str, default: int | None = None) -> str | NoReturn:
    env_value = getenv(env_name, None)
    if env_value is None and default is None:
        raise EnvVariableUndefined(env_name)

    if env_value is None and default is not None:
        return default

    return int(env_value)


@dataclass(slots=True, frozen=True)
class Config:
    """Config class."""
    ip: str = get_str_env('IP', '0.0.0.0')
    port: int = 5001
    source_path: str = get_str_env('SOURCE_PATH', '/app/testing-system/frontend/source')
    log_level: str = get_str_env('LOG_LEVEL', 'debug')
    debug: bool = get_bool_env('DEBUG', False)

    mail_server: str = get_str_env('MAIL_SERVICE')
    email: str = get_str_env('EMAIL')
    mail_password: str = get_str_env('MAIL_PASSWORD')


config = Config()
