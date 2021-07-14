import os
import warnings
from pathlib import Path
from typing import List, Union, Iterable

from ._crc64 import crc64bytes


def _equally_distributed_indices(file_size: int, max_bytes_count: int) \
        -> List[int]:
    """we have a fileSize file and we want to read the maxBytesCount of
    individual bytes in it, located at an equal distance from each other.
    The function returns the indexes of these bytes inside the file."""

    import math

    result = set()
    result.add(0)

    for i in range(1, max_bytes_count):
        result.add(math.floor(i * (file_size - 1) / (max_bytes_count - 1)))

    result_list = sorted(result)
    assert 1 <= len(result_list) <= max_bytes_count

    return result_list


def _iter_equally_distributed_bytes(filename: str, count: int) -> Iterable[int]:
    fileSize = os.path.getsize(filename)

    if fileSize > 0:
        with open(filename, "rb") as f:
            for idx in _equally_distributed_indices(fileSize, count):
                f.seek(idx)
                byte = f.read(1)
                assert byte != b''
                yield byte[0]


def _iter_nonzero_bytes(integer):
    # 0x112233 -> 0x33, 0x22, 0x11
    while integer != 0:
        yield integer & 0xFF
        integer = (integer >> 8)


def fastHashCRC64(filename: Union[Path, str],
                  bytes_to_read: int = 4) -> int:
    warnings.warn("Kept for compatibility only", DeprecationWarning)

    filename = str(filename)

    data = list()
    data.extend(_iter_nonzero_bytes(os.path.getsize(filename)))
    data.extend(
        c for c in _iter_equally_distributed_bytes(filename, bytes_to_read))

    return crc64bytes(data)

#    FULL32 = 0xFFFFFFFF

#    initial = (FULL32 ^ filename.stat().st_size) & FULL32



#    return crc32(bytes(_iter_fibonacci_placed_bytes(filename)), initial)
