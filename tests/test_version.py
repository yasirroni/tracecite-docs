import importlib.metadata
import subprocess
import sys

import tracecite_docs


def test_runtime_version_surfaces_match_distribution_metadata() -> None:
    expected = importlib.metadata.version("tracecite-docs")

    assert tracecite_docs.__version__ == expected

    result = subprocess.run(
        [sys.executable, "-m", "tracecite_docs", "--version"],
        check=True,
        capture_output=True,
        text=True,
    )
    assert result.stdout == f"TraceCite Docs {expected}\n"
