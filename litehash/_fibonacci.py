# SPDX-FileCopyrightText: (c) 2021 Artёm IG <github.com/rtmigo>
# SPDX-License-Identifier: MIT

import warnings
from pathlib import Path
from typing import Union, BinaryIO, Iterable
from zlib import crc32

from litehash._common import _iter_positioned_bytes, HashAlgo, \
    bytes_to_digest


def fibonacci_sequence(factor: int = 1) -> Iterable[int]:
    """Returns fibonacci sequence with non-repeating numbers:
    0, 1, 2, 3, 5, 8, 13, 21, 34, 55...
    """

    yield 0
    a, b = 1, 2
    while True:
        yield a * factor
        (a, b) = (b, a + b)


def _iter_fibo(f: BinaryIO, speedup: int):
    if speedup <= 0:
        raise ValueError(speedup)
    return _iter_positioned_bytes(f, fibonacci_sequence(speedup))


def _fibobytes(file: Path, speedup: int) -> bytes:
    size_as_bytes = file.stat().st_size.to_bytes(8, byteorder="big")
    with file.open("rb") as f:
        data_bytes = bytes(_iter_fibo(f, speedup))
    return data_bytes + size_as_bytes


def file_to_hash_fibonacci(file: Path,
                           algo: HashAlgo = HashAlgo.md5,
                           speedup: int = 1) -> str:
    if speedup < 1:
        raise ValueError(speedup)
    return bytes_to_digest(_fibobytes(Path(file), speedup), algo)


def file_fibonacci_crc32(file: Union[Path, str], speedup: int = 1) -> int:
    warnings.warn("Use file_to_hash_fibonacci",
                  DeprecationWarning,
                  stacklevel=2)
    if speedup < 1:
        raise ValueError(speedup)
    return crc32(_fibobytes(Path(file), speedup))


def file_fibonacci_md5(file: Union[Path, str], speedup: int = 1) -> str:
    warnings.warn("Use file_to_hash_fibonacci",
                  DeprecationWarning,
                  stacklevel=2)
    if speedup < 1:
        raise ValueError(speedup)
    return bytes_to_digest(_fibobytes(Path(file), speedup),
                           HashAlgo.md5)
