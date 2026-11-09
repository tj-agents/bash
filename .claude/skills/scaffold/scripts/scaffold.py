"""Create a minimal Bash command project without replacing existing files."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


def create(destination: Path, name: str) -> Path:
    """Create a new project; reject invalid names and any existing target."""
    if re.fullmatch(r"[a-z][a-z0-9-]*", name) is None:
        raise ValueError("name must be a lowercase command name")
    parent = destination.expanduser().resolve(strict=True)
    target = parent / name
    target.mkdir()
    templates = Path(__file__).resolve().parents[1] / "templates"
    for source, relative in (
        ("command.bash", f"bin/{name}"),
        ("editorconfig", ".editorconfig"),
        ("shellcheckrc", ".shellcheckrc"),
    ):
        output = target / relative
        output.parent.mkdir(parents=True, exist_ok=True)
        text = (templates / source).read_text(encoding="utf-8")
        with output.open("x", encoding="utf-8", newline="\n") as stream:
            stream.write(text.replace("@COMMAND@", name))
        if source == "command.bash":
            output.chmod(output.stat().st_mode | 0o111)
    return target


def main() -> int:
    """Parse explicit destination/name inputs and report creation failures."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--destination", type=Path, required=True)
    parser.add_argument("--name", required=True)
    arguments = parser.parse_args()
    try:
        target = create(arguments.destination, arguments.name)
    except (OSError, ValueError) as error:
        parser.exit(1, f"Scaffold failed: {error}\n")
    print(target)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
