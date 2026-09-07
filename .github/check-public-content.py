"""Reject internal planning artifacts and references in the public source tree."""
from pathlib import Path
import re
import subprocess

root = Path(__file__).resolve().parents[1]
public_repositories = {"claude-plugin", "openclaw-plugin", "tap", "scoop-bucket"}
files = subprocess.check_output(["git", "ls-files", "-z"], cwd=root).decode().split("\0")
for name in filter(None, files):
    path = root / name
    assert not ({"plans", "superpowers", "graphify-out"} & set(path.relative_to(root).parts)), f"Non-product artifact: {name}"
    if not path.exists() or path == Path(__file__).resolve():
        continue
    text = path.read_text()
    for repository in re.findall(r"github\.com/kastra-labs/([A-Za-z0-9_-]+)", text):
        assert repository in public_repositories, f"Unreviewed repository reference in {name}"
    assert not re.search(r"/(?:Users|private/tmp)/|\.\./docs/|\bIF-\d+\b|docs/(?:plans|superpowers)/", text), f"Internal reference in {name}"
print("Public content checks passed.")
