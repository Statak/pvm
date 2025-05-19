import logging
import pathlib
from typing import Any

try:
    import tomllib  # Python 3.11+
except ModuleNotFoundError:
    import tomli as tomllib  # type: ignore # For Python <3.11

log = logging.getLogger('pvm')


def load_config_from_pyproject() -> dict:
    """Load the PVM tool config from pyproject.toml, if it exists in the user's working directory.

    Returns an empty dictionary if the file or expected section does not exist.
    """
    pyproject_path = pathlib.Path.cwd() / 'pyproject.toml'

    if not pyproject_path.is_file():
        return {}

    try:
        with pyproject_path.open('rb') as f:
            pyproject_data = tomllib.load(f)

        return pyproject_data.get('tool', {}).get('pvm', {})
    except Exception as e:
        # Optional: log or handle parsing errors
        log.exception(f"Failed to load pyproject.toml: {e}")
        return {}


def _get_changelog_file(default: Any) -> str:
    config: dict = load_config_from_pyproject()

    file = config.get('changelog-file', 'CHANGELOG.md')
    if isinstance(file, str):
        path = pathlib.Path(file)
        if not file.endswith('/') and path.name != '':
            return file
    fallback = default if default else 'CHANGELOG.md'
    log.error(f'[-] changelog-file must be a valid file name. Using default value: {fallback}')
    return fallback


def get(var: str, default: Any | None = None) -> Any | None:
    config = load_config_from_pyproject()
    defaults = {
        'mode': default,
        'bump-target': default,
        'prerelease': default,
        'build': default,
        'changelog': False,
        'tag': default if default is not None else False,
        'prerelease-token': default if default is not None else 'rc',
        'build-token': default if default is not None else 'build',
        'tag-prefix': default if default is not None else 'v',
    }

    if var in defaults:
        return config.get(var, defaults[var])
    elif var in ('changelog_file', 'changelog-file'):
        return _get_changelog_file(default)
    else:
        return default
