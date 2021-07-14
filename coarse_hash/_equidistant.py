# SPDX-FileCopyrightText: (c) 2021 Artёm IG <github.com/rtmigo>
# SPDX-License-Identifier: MIT

from pathlib import Path
from typing import List, BinaryIO, Iterable, Union
from zlib import crc32

from coarse_hash._common import _iter_positioned_bytes


def _equidistant_positions(size: int, n: int) -> List[int]:
    """We have a file sized `size` and we want to read the `n` of
    bytes from it, located at an equal distance from each other.
    The function returns the indexes of these bytes inside the file."""

    if n <= 0:
        raise ValueError(n)

    if size <= 0:
        return []

    result: List[int] = list()

    step = (size - 1) / (n - 1)

    for i in range(n):
        pos = round(i * step)
        assert 0 <= pos < size
        if result and pos <= result[-1]:
            continue
        result.append(pos)

    return result


def _equidistant_bytes(stream: BinaryIO, size: int, n: int) -> Iterable[int]:
    return _iter_positioned_bytes(stream, _equidistant_positions(size, n))


def file_equidistant_crc32(file: Union[Path, str], n: int = 8) -> int:
    file = Path(file)

    size = file.stat().st_size

    size_as_bytes = size.to_bytes(8, byteorder="big")
    with file.open("rb") as f:
        data_bytes = bytes(_equidistant_bytes(stream=f, size=size, n=n))

    crc = crc32(data_bytes)
    crc = crc32(size_as_bytes, crc)

    return crc
