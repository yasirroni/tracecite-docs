# tracecite-docs

Table normalisation, citable documentation and inspection-site builds for the TraceCite family.
The shared [TraceCite documentation](https://yasirroni.github.io/tracecite/) covers evidence retrieval, normalised tables and their source citations together.
This package has no separate documentation site.

## Installation and use

```bash
uv pip install tracecite-docs                # After the first release.
uv pip install 'tracecite-docs[docs,evidence]'
tracecite-docs build docs
tracecite-docs table normalise table.md
tracecite-docs table check docs/build
```

The `docs` extra enables Python/Jupyter page execution; `evidence` enables documentation indexing and retrieval through the core package.
Pandas table authoring is available with `tracecite-docs[pandas]` and is included in `docs` and `test`.
Quarto/Pandoc and Julia remain external tools when the selected inputs require them.

```python
from tracecite_docs import knowledge_table
from tracecite_docs.docs import build_docs, stage_docs, sync_docs_index
```

The executable is also available as `python -m tracecite_docs`.
Former `tracecite docs` subcommands are top-level commands here; `table`, `document` and `prepare` retain their structure.
The former table-validation command is `tracecite-docs table check`; documentation contract checking is `tracecite-docs check --docs-config ...`.
Core evidence commands continue to use `tracecite`.
Existing configuration names, table markers, source links and normaliser identities are preserved.

## Development

```bash
uv sync --locked --extra docs --extra evidence --extra test
uvx pre-commit run --all-files --show-diff-on-failure
uvx pre-commit run pyright --all-files --hook-stage manual
uv run --no-sync pytest -q -rs
```

The implementation and behavioural tests were extracted from TraceCite commit `a942f138ba8534536b7aaa8f4b2062d1ba84c27d`, preserving its MIT licence.
The uv source pin selects that same core revision for development.
`requirements.txt` is derived with `uv export --all-extras --no-emit-project --no-hashes --output-file requirements.txt`.

**Release prerequisite:** the published core `tracecite==0.0.2` lacks the indexing APIs used by this source revision.
Before publishing, select and verify a compatible core release, update both core requirements, remove the development source pin, regenerate the lock/export and repeat clean artefact installation tests.
The current `>=0.0.2` requirement is provisional and is not a verified release compatibility claim.

```bash
uv pip install --upgrade build
uv build
uv pip install --upgrade twine
uvx twine check dist/*
uv build --no-sources
uvx twine check --strict dist/*
# After the release prerequisite and upload configuration are satisfied:
uvx twine upload --repository tracecite-docs dist/*
```

The upload alias names a private Twine configuration section; it does not select a project name.
Inspect and smoke-test the exact wheel and sdist before uploading.
