# tracecite-docs

Build Quarto sites from executable Python (`.py`) and Julia (`.jl`) pages.
Preserve raw tables and source links alongside normalised text for citation and search.
Also supports HTML tables produced by Literate.jl and Documenter.jl.

```bash
uv pip install tracecite-docs
tracecite-docs build docs
tracecite-docs table normalise table.md
tracecite-docs table check docs/build
```

Install `tracecite-docs[docs,evidence]` for Python execution, indexing, and search.
Site builds need Quarto; Markdown tables need Pandoc or Quarto.
Julia pages also need Julia.

## Runnable examples

| Pages | Example project |
|---|---|
| Python only | [Quarto](https://github.com/yasirroni/tracecite/tree/main/docs_quarto_py) |
| Julia only | [Literate.jl / Documenter.jl](https://github.com/yasirroni/tracecite/tree/main/docs_jl) |
| Python and Julia | [Mixed Quarto](https://github.com/yasirroni/tracecite/tree/main/docs) |

[Documentation](https://yasirroni.github.io/tracecite/)
