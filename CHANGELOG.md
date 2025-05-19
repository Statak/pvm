# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [v0.1.1] - 2025-05-19

### Added

- Add GitHub Actions workflow for publishing to PyPI.

### Fixed

- Update project name to 'project-version-manager' in pyproject.toml.
- Correct pip command for installing uv package.

### Uncategorized

- Bump version to v0.1.1.
- Revert version to 0.1.0 in pyproject.toml and __init__.py.
- Merge branch 'hotfix/pyproject-path' into develop.
- Update uv.lock file.
- Integrate VersionSyncer for synchronizing version across specified files.
- Implement VersionSyncer for synchronizing version across multiple file formats.
- Improve error handling and add version-files retrieval in config loading.
- Update dependencies and improve project configuration.
- Bump version to v0.1.1-dev.1.
- Load pyproject.toml relative to user’s working directory.
- Resolve pyproject.toml path from current working directory.
- Add environment specification for publish job in GitHub Actions workflow.
- Automate changelog update and commit after version bump.
- Reorganize changelog structure and update entries for clarity.
- Remove environment specification from publish job in GitHub Actions workflow.

## [v0.1.0] - 2025-05-19

### Added

- Add GitHub Actions workflow for publishing to PyPI.
- Add CHANGELOG.md for project documentation.
- Add Makefile for project automation tasks.
- Add type hinting support with py.typed file.
- Add initial exception handling and hooks modules.
- Add pre-commit configuration for code quality checks.
- Implement main entry point for Project Version Manager (PVM).
- Show current and next version details.
- Generate changelogs from commit history.
- Add version bumping capabilities.
- Introduce cli for Project Version Manager (PVM).
- Implement changelog update functionality.

### Changed

- Organize git operations into a dedicated module.

### Fixed

- Uncomment current_version assignment for proper version handling.

### Uncategorized

- Update changelog file to include v0.1.0.
- Bump version to v0.1.0.
- Set up configuration management.
- Update name in `pyproject.toml`.
- Initial commit with project scaffold.



[unreleased]: https://github.com/DazzyMlv/pvm/compare/v0.1.1...HEAD
[v0.1.1]: https://github.com/DazzyMlv/pvm/compare/v0.1.0...v0.1.1
[v0.1.0]: https://github.com/DazzyMlv/pvm/releases/tag/v0.1.0
