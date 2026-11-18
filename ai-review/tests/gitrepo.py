"""Test helper: a throwaway git repository whose commits are built with plumbing (hash-object,
update-index, commit-tree), so file names a filesystem may refuse (tab, newline, bytes that are
not UTF-8) work anywhere. No checkout, no network, no user or system git config."""

from __future__ import annotations

import os
import subprocess
import tempfile
from pathlib import Path


class Repo:
    def __init__(self) -> None:
        self._tmp = tempfile.TemporaryDirectory(prefix="ai-review-test-")
        self.dir = Path(self._tmp.name)
        self.path = self.dir / "repo"
        self.env = {"PATH": os.environ.get("PATH", "/usr/bin:/bin"), "HOME": str(self.dir),
                    "GIT_CONFIG_NOSYSTEM": "1", "GIT_CONFIG_GLOBAL": os.devnull,
                    "GIT_AUTHOR_NAME": "t", "GIT_AUTHOR_EMAIL": "t@t", "GIT_COMMITTER_NAME": "t",
                    "GIT_COMMITTER_EMAIL": "t@t", "GIT_AUTHOR_DATE": "2026-01-01T00:00:00Z",
                    "GIT_COMMITTER_DATE": "2026-01-01T00:00:00Z"}
        self.git("init", "-q", str(self.path), cwd=self.dir)

    def git(self, *args, input_: bytes | None = None, cwd: Path | None = None, env: dict | None = None) -> str:
        r = subprocess.run(["git", *args], cwd=cwd or self.path, env={**self.env, **(env or {})},
                           input=input_, capture_output=True, check=True)
        return r.stdout.decode().strip()

    def commit(self, files: dict, parent: str | None = None) -> str:
        """A commit whose tree holds exactly `files` ({path: content}, str or bytes)."""
        index = {"GIT_INDEX_FILE": str(self.dir / "index.tmp")}
        Path(index["GIT_INDEX_FILE"]).unlink(missing_ok=True)
        for path, data in files.items():
            data = data.encode() if isinstance(data, str) else data
            sha = self.git("hash-object", "-w", "--stdin", input_=data)
            path = path.encode() if isinstance(path, str) else path
            self.git("update-index", "--add", "--cacheinfo", b"100644," + sha.encode() + b"," + path, env=index)
        tree = self.git("write-tree", env=index)
        return self.git("commit-tree", tree, *(["-p", parent] if parent else []), "-m", "x")

    def close(self) -> None:
        self._tmp.cleanup()
