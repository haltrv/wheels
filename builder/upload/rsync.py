"""Upload plugin rsync."""

from pathlib import Path

from builder.utils import run_command


def upload(local: Path, remote: str, index: str, wheels_index: str) -> None:
    """Upload wheels from folder to remote rsync server."""
    lock_held = run_command(
        f"rsync --dry-run {remote}/.musllinux.index_503.lock"
    )
    print( f"lock_held={lock_held}" )
    run_command(
        f"index-503 --merge-with {wheels_index} {local}/musllinux"
    )
    run_command(
        f"rsync --human-readable --recursive --links --progress --checksum {local}/* {remote}/",
    )
