# Contributing

Thank you for helping improve Anime Video Link Parser Kit. Contributions are
accepted through Pull Requests only.

## Workflow

1. Open an issue for a bug, provider format change or proposed feature when
   the scope is not obvious.
2. Fork the repository and create a focused branch from the default branch.
3. Add or update tests and redacted fixtures that reproduce the behavior.
4. Run the test suite and compile check locally.
5. Open a Pull Request with a clear explanation of the provider, payload shape
   and compatibility impact.

Maintainers review every Pull Request. A maintainer may request changes,
additional fixtures or documentation before merging. Do not push directly to
the default branch.

## Fixture and security rules

- Remove tokens, cookies, personal identifiers and private hostnames.
- Do not commit links that require an account or bypass access controls.
- Do not add copyrighted media files to the repository.
- Prefer the smallest JSON payload that reproduces the parser behavior.
- Keep provider-specific behavior inside the matching adapter.

## Pull Request checklist

- The change is limited to one coherent purpose.
- Tests cover new parsing or validation behavior.
- `python -m compileall src tests` passes.
- Documentation and examples are updated when the public behavior changes.
- The description explains any upstream provider assumptions.
