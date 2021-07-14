import io
from typing import BinaryIO, Iterable


def _iter_positioned_bytes(f: BinaryIO, positions: Iterable[int]) \
        -> Iterable[int]:
    for pos in positions:
        f.seek(pos, io.SEEK_SET)
        d = f.read(1)
        if not d:
            break
        yield d[0]
