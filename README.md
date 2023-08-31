# pdoctest


## [Auto-Documentation Link](https://ethanmsl.github.io/pdoctest/pdoctest.html)



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
