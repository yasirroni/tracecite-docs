from __future__ import annotations

from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

from tracecite_docs import cli


def test_docs_mode_dispatch_passes_contract_arguments_and_status(capsys) -> None:
    args = cli.build_parser().parse_args(
        ["check", "--docs-config", "config.toml", "--repo-root", "repo"]
    )
    contract = object()
    ok = SimpleNamespace(
        mode="check", ok=True, manifest_path=Path("manifest"), diagnostics=()
    )
    with (
        patch.object(cli, "load_docs_contract", return_value=contract) as load,
        patch.object(cli, "check_docs", return_value=ok) as operation,
    ):
        assert cli._docs_mode(args, cli.check_docs) == 0
    load.assert_called_once_with(Path("config.toml"), repo_root=Path("repo"))
    operation.assert_called_once_with(
        contract, config_path=Path("config.toml"), repo_root=Path("repo")
    )
    assert "Documentation mode: check" in capsys.readouterr().out

    stale = SimpleNamespace(
        mode="check",
        ok=False,
        manifest_path=Path("manifest"),
        diagnostics=("stale: docs/x.md",),
    )
    with (
        patch.object(cli, "load_docs_contract", return_value=contract),
        patch.object(cli, "check_docs", return_value=stale),
    ):
        assert cli._docs_mode(args, cli.check_docs) == 1
    assert "stale: docs/x.md" in capsys.readouterr().err


def test_docs_index_exits_1_and_names_a_skipped_source(capsys) -> None:
    from tracecite.evidence.sync import SyncReport

    args = cli.build_parser().parse_args(
        ["index", "--docs-config", "config.toml", "--repo-root", "repo"]
    )
    report = SyncReport(skipped_sources={"bad.md": "cannot parse: invalid UTF-8"})
    result = SimpleNamespace(
        profile=SimpleNamespace(input_root=Path("in"), database_path=Path("db")),
        tables_normalized=0,
        sync_report=report,
    )
    with (
        patch.object(cli, "load_docs_contract"),
        patch.object(cli, "sync_docs_index", return_value=result),
    ):
        assert cli._docs_index(args) == 1
    out = capsys.readouterr().out
    assert "status: incomplete\n" in out
    assert "skipped: bad.md: cannot parse: invalid UTF-8\n" in out
