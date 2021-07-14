import io
from pathlib import Path
from typing import Iterable, Union
from zlib import crc32


def _fibonacci_sequence() -> Iterable[int]:
    # https://stackoverflow.com/questions/494594/how-to-write-the-fibonacci-sequence
    a, b = 0, 1
    while True:  # First iteration:
        yield a  # yield 0 to start with and then
        a, b = b, a + b  # a will now be 1, and b will also be 1, (0 + 1)


def _iter_fibonacci_placed_bytes(file: Path) -> Iterable[int]:
    with file.open('rb') as f:
        for byte_pos in _fibonacci_sequence():
            if f.seek(byte_pos, io.SEEK_SET) != byte_pos:
                break
            d = f.read(1)
            if not d:
                break
            yield d[0]


def coarse_file_crc32(filename: Union[Path, str]) -> int:
    filename = Path(filename)

    size_as_bytes = filename.stat().st_size.to_bytes(8, byteorder="big")
    data_bytes = bytes(_iter_fibonacci_placed_bytes(filename))

    crc = crc32(data_bytes)
    crc = crc32(size_as_bytes, crc)

    return crc