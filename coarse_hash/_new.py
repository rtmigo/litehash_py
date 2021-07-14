import io
from pathlib import Path
from typing import Iterable, Union, BinaryIO
from zlib import crc32


def _fibonacci_sequence() -> Iterable[int]:
    # https://stackoverflow.com/questions/494594/how-to-write-the-fibonacci-sequence
    a, b = 1, 2
    while True:
        yield a
        (a, b) = (b, a + b)


def _iter_fibonacci_bytes_io(f: BinaryIO) -> Iterable[int]:
    for byte_pos in _fibonacci_sequence():
        d = f.read(1)
        if len(d) <= 0:
            break
        yield d[0]
        f.seek(byte_pos, io.SEEK_CUR)


def _iter_fibonacci_bytes_file(file: Path) -> Iterable[int]:
    with file.open('rb') as f:
        for x in _iter_fibonacci_bytes_io(f):
            yield x


def coarse_file_crc32(filename: Union[Path, str]) -> int:
    filename = Path(filename)

    size_as_bytes = filename.stat().st_size.to_bytes(8, byteorder="big")
    data_bytes = bytes(_iter_fibonacci_bytes_file(filename))

    crc = crc32(data_bytes)
    crc = crc32(size_as_bytes, crc)

    return crc
