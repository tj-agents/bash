"""Exercise the scaffold's command interface and its no-overwrite boundary."""

from __future__ import annotations

import importlib.util
import os
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

SCRIPT = (
    Path(__file__).resolve().parents[1] / "bash/utility/scaffold/scripts/scaffold.py"
)
SPEC = importlib.util.spec_from_file_location("bash_scaffold", SCRIPT)
assert SPEC is not None and SPEC.loader is not None
scaffold = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(scaffold)


def bash_executable() -> str:
    """Use Git Bash on Windows, avoiding the unconfigured WSL system alias."""
    if os.name == "nt":
        git = shutil.which("git")
        if git is not None:
            candidate = Path(git).resolve().parents[1] / "bin/bash.exe"
            if candidate.is_file():
                return str(candidate)
        raise RuntimeError("These tests require native Git Bash on Windows")
    executable = shutil.which("bash")
    if executable is None:
        raise RuntimeError("These tests require Bash")
    return executable


class ScaffoldTests(unittest.TestCase):
    def test_generated_command_in_path_with_spaces(self) -> None:
        with tempfile.TemporaryDirectory(prefix="bash project ") as directory:
            target = scaffold.create(Path(directory), "report")
            command = target / "bin/report"
            bash = bash_executable()
            syntax = subprocess.run([bash, "-n", command.as_posix()], check=False)
            self.assertEqual(syntax.returncode, 0)
            for arguments in ([], ["--help"]):
                result = subprocess.run(
                    [bash, command.as_posix(), *arguments],
                    capture_output=True,
                    text=True,
                    check=False,
                )
                self.assertEqual(result.returncode, 0)
                self.assertEqual(result.stdout, "Usage: report [--help]\n")
                self.assertEqual(result.stderr, "")
            for arguments in (["bad"], ["--help", "extra"], [""]):
                result = subprocess.run(
                    [bash, command.as_posix(), *arguments],
                    capture_output=True,
                    text=True,
                    check=False,
                )
                self.assertEqual(result.returncode, 2)
                self.assertEqual(result.stdout, "")
                self.assertIn("Usage:", result.stderr)

    def test_existing_project_is_preserved(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            target = scaffold.create(Path(directory), "report")
            command = target / "bin/report"
            command.write_text("user content", encoding="utf-8")
            with self.assertRaises(FileExistsError):
                scaffold.create(Path(directory), "report")
            self.assertEqual(command.read_text(encoding="utf-8"), "user content")

    def test_invalid_name_creates_nothing(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            for name in ("../escape", "a/b", "", "Bad Name", "-option"):
                with self.assertRaises(ValueError):
                    scaffold.create(Path(directory), name)
            self.assertEqual(list(Path(directory).iterdir()), [])

    def test_existing_symlink_is_not_followed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            actual = root / "actual"
            actual.mkdir()
            try:
                (root / "report").symlink_to(actual, target_is_directory=True)
            except OSError:
                self.skipTest("symlink creation unavailable")
            with self.assertRaises(FileExistsError):
                scaffold.create(root, "report")
            self.assertEqual(list(actual.iterdir()), [])


if __name__ == "__main__":
    unittest.main()
