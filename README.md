# pdoctest


## [Auto-Documentation Link](https://ethanmsl.github.io/pdoctest/pdoctest.html)

Updates to process:
added line to `pyproject.toml`:
```toml
[tool.pytest.ini_options]
...
addopts = "--doctest-modules"
...
```

change to `pre-commit` hook test line:
```bash
pytest --cov-report=term-missing --cov-fail-under=$test_coverage_min --cov=src/
```
(we removed the ` tests/` at the end, which was not needed for indicating proper coverage and for some reason caused the `--doctest-modules` to be ignored, whether manually inserted in a terminal call or via the `addopts` field in `pyproject.toml`)

Together these get succesful doctest testing :excite: :)


## Dev-Dependencies Specified
- formatting: `isort` & `black`
- linting: `pylint` & `ruff`
- lsp & typechecking: `pyright`
- testing: `pytest` + `coverage` (via `pytest-cov`)
- auto-documentation: `pdoc` (*not* ~~"pdoc3"~~, which should be strongly avoided)
- doc-tests: `doctest-cli`


## Run Pre-Commit Hook Manually
from anywhere in project:
```zsh
poetry shell
git hook run pre-commit
```
