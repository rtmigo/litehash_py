# SPDX-FileCopyrightText: (c) 2021 Artёm IG <github.com/rtmigo>
# SPDX-License-Identifier: MIT
import warnings
from pathlib import Path
from typing import List, BinaryIO, Iterable, Union
from zlib import crc32

from litehash._common import _iter_positioned_bytes, bytes_to_digest, \
    HashAlgo


def _equidistant_positions(size: int, n: int) -> List[int]:
    """We have a file sized `size` and we want to read the `n` of
    bytes from it, located at an equal distance from each other.
    The function returns the indexes of these bytes inside the file."""

    if size <= 0 or n <= 0:
        return []

    if n == 1:
        return [round((size - 1) / 2)]

    result: List[int] = list()

    step = (size - 1) / (n - 1)

    for i in range(n):
        pos = round(i * step)
        assert 0 <= pos < size
        if result and pos <= result[-1]:
            continue
        pos = min(pos, size - 1)
        assert 0 <= pos < size
        result.append(pos)

    return result


def _equidistant_bytes(stream: BinaryIO, size: int, n: int) -> Iterable[int]:
    return _iter_positioned_bytes(stream, _equidistant_positions(size, n))


def _equidistant_hashable(file: Path, n: int) -> bytes:
    size = file.stat().st_size
    size_as_bytes = size.to_bytes(8, byteorder="big")
    with file.open("rb") as f:
        data_bytes = bytes(_equidistant_bytes(stream=f,
                                              size=size,
                                              n=min(size, n)))
    return data_bytes + size_as_bytes


def file_equidistant_crc32(file: Union[Path, str], n: int = 8) -> int:
    warnings.warn("Use file_to_hash_equidistant",
                  DeprecationWarning,
                  stacklevel=2)
    if n <= 0:
        raise ValueError(n)
    return crc32(_equidistant_hashable(Path(file), n=n))


def file_equidistant_md5(file: Union[Path, str], n: int = 8) -> str:
    warnings.warn("Use file_to_hash_equidistant",
                  DeprecationWarning,
                  stacklevel=2)
    if n <= 0:
        raise ValueError(n)
    return bytes_to_digest(_equidistant_hashable(Path(file), n=n),
                           HashAlgo.md5)


def file_to_hash_equidistant(file: Path,
                             algo: HashAlgo = HashAlgo.md5,
                             n: int = 8) -> str:
    if n <= 0:
        raise ValueError(n)
    return bytes_to_digest(_equidistant_hashable(Path(file), n=n), algo)
