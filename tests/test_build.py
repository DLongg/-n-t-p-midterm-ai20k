"""
tests/test_build.py

Verifies that the Vite web application builds cleanly from source:
- Executes `npm run build` inside `vlearn-app`
- Asserts exit code is 0
- Confirms production artifacts are generated in `vlearn-app/dist/`
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import pytest


def test_vlearn_app_build(project_root: Path):
    vlearn_dir = project_root / "vlearn-app"
    package_json = vlearn_dir / "package.json"

    assert package_json.exists(), f"package.json missing at {package_json}"

    # Execute npm run build
    npm_cmd = "npm.cmd" if sys.platform == "win32" else "npm"

    proc = subprocess.run(
        [npm_cmd, "run", "build"],
        cwd=str(vlearn_dir),
        capture_output=True,
        text=True,
        timeout=120,
        shell=(sys.platform == "win32"),
    )

    stdout = proc.stdout
    stderr = proc.stderr

    assert proc.returncode == 0, (
        f"npm run build failed with exit code {proc.returncode}!\n"
        f"STDOUT:\n{stdout}\n"
        f"STDERR:\n{stderr}"
    )

    # Check dist output directory and artifacts
    dist_dir = vlearn_dir / "dist"
    index_html = dist_dir / "index.html"
    assets_dir = dist_dir / "assets"

    assert dist_dir.exists(), f"dist directory was not created at {dist_dir}"
    assert index_html.exists(), f"index.html missing in {dist_dir}"
    assert index_html.stat().st_size > 0, "index.html is empty"
    assert assets_dir.exists(), f"assets directory missing in {dist_dir}"
    assert len(list(assets_dir.glob("*.js"))) >= 1, "No compiled JS bundle found in assets directory"
