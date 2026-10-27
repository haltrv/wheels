"""Upload plugin rsync."""

from pathlib import Path

from builder.utils import run_command


def upload(local: Path, remote: str) -> None:
    """Upload wheels from folder to remote rsync server."""
    uhost, fpath = remote.split(":", 1)
    print(
        f"index-503 --merge-with-remote fpath={fpath} uhost={uhost} index={index} wheels_index={wheels_index}"
    )
    exit(1)
    run_command(
        f"rsync --human-readable --recursive --progress --checksum {local}/* {remote}/",
    )
