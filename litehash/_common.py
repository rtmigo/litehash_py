import io
from enum import auto, Enum
from hashlib import md5, sha256
from typing import BinaryIO, Iterable
from zlib import crc32


def _iter_positioned_bytes(f: BinaryIO, positions: Iterable[int]) \
        -> Iterable[int]:
    for pos in positions:
        f.seek(pos, io.SEEK_SET)
        d = f.read(1)
        if not d:
            break
        yield d[0]


class HashAlgo(Enum):
    crc32 = auto()
    md5 = auto()
    sha256 = auto()


def _uint32_to_hexdigest(x: int) -> str:
    if not 0 <= x <= 0xFFFFFFFF:
        raise ValueError(x)
    return hex(x)[2:].rjust(8, '0')


def bytes_to_digest(data: bytes, algo: HashAlgo) -> str:
    if algo == HashAlgo.crc32:
        return _uint32_to_hexdigest(crc32(data))
    elif algo == HashAlgo.md5:
        return md5(data).hexdigest()
    elif algo == HashAlgo.sha256:
        return sha256(data).hexdigest()
    else:
        raise ValueError(algo)
