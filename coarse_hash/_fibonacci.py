# SPDX-FileCopyrightText: (c) 2021 Artёm IG <github.com/rtmigo>
# SPDX-License-Identifier: MIT

from pathlib import Path
from typing import Union, BinaryIO, Iterable
from zlib import crc32

from coarse_hash._common import _iter_positioned_bytes


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


def file_fibonacci_crc32(file: Union[Path, str], speedup: int = 1) -> int:
    file = Path(file)

    size_as_bytes = file.stat().st_size.to_bytes(8, byteorder="big")
    with file.open("rb") as f:
        data_bytes = bytes(_iter_fibo(f, speedup))

    crc = crc32(data_bytes)
    crc = crc32(size_as_bytes, crc)

    return crc
