"""Upload plugin rsync."""

from pathlib import Path

from builder.utils import run_command


def upload(local: Path, remote: str) -> None:
    """Upload wheels from folder to remote rsync server."""
    run_command(
        f"rsync --human-readable --recursive --progress --checksum {local}/* {remote}/",
    )
    uhost, fpath = remote.split(":", 1)
    run_command(
        f"ssh {uhost} \'\n"
        f"python3 -m venv index-503.venv\n"
        f"source index-503.venv/bin/activate\n"
        f"pip install index-503\n"
        f"pushd {fpath} && index-503 musllinux && popd\n"
        "\'"
    )
