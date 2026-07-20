"""Recursive image folder scanning — shared by IOController and ProjectController."""

import os
from pathlib import Path

IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".bmp", ".tif", ".tiff"}


def scan_images(directory: str) -> list:
    """Recursively find images under *directory*.

    Returns a sorted list of POSIX-style paths relative to *directory*
    (e.g. ``"nest1/nest2.png"``; a file directly in *directory* has no
    prefix, e.g. ``"root.png"``). Directories starting with ``"."`` are
    skipped. Symlinks are not followed (matches ``os.walk``'s default,
    avoiding cycles).

    Args:
        directory (str): Absolute path to the folder to scan.

    Returns:
        list: Sorted relative image paths, POSIX-separated.
    """
    root = Path(directory)
    results = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if not d.startswith(".")]
        for fname in filenames:
            if Path(fname).suffix.lower() in IMAGE_EXTENSIONS:
                rel = Path(dirpath, fname).relative_to(root).as_posix()
                results.append(rel)
    return sorted(results)
