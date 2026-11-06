# tracecite-docs

Build citable documentation with normalised tables and source links.

```bash
uv pip install tracecite-docs
tracecite-docs build docs
tracecite-docs table normalise table.md
tracecite-docs table check docs/build
```

Install `tracecite-docs[docs,evidence]` for Python execution, indexing, and search.
Site builds need Quarto; Markdown tables need Pandoc or Quarto.
Julia pages also need Julia.

[Documentation](https://yasirroni.github.io/tracecite/)
