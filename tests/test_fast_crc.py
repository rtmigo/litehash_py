import io
import unittest
from io import BytesIO
from itertools import islice
from pathlib import Path

from coarse_hash import coarse_file_crc32
from coarse_hash._new import _iter_fibonacci_bytes_file, _fibonacci_sequence, \
    _iter_fibonacci_bytes_io

file = Path(__file__).parent / "data" / "public-domain-image.jpg"


class TestCoarse32(unittest.TestCase):
    def test_str(self):
        self.assertEqual(
            coarse_file_crc32(str(file)),
            1654288293)

    def test(self):
        self.assertEqual(
            coarse_file_crc32(file),
            1654288293)


class TestIterFibo(unittest.TestCase):

    def test_fibonacci(self):
        self.assertEqual(
            list(islice(_fibonacci_sequence(), 10)),
            [1, 2, 3, 5, 8, 13, 21, 34, 55, 89])

    def test_iter_bytes_stream(self):
        with BytesIO() as stream:
            for x in range(256):
                stream.write(bytes((x,)))
            stream.seek(0, io.SEEK_SET)
            data = list(_iter_fibonacci_bytes_io(stream))
        self.assertEqual(
            data,
            [0, 2, 5, 9, 15, 24, 38, 60, 95, 151, 241])

    def test_iter_bytes_file(self):
        data = list(_iter_fibonacci_bytes_file(file))
        self.assertEqual(
            data,
            [255, 255, 16, 70, 72, 69, 0, 0, 0, 0, 0, 3, 0, 110, 248, 72, 182,
             214, 100, 93, 111, 233, 196, 11, 24])
        # self.assertEqual(
        #   coarse_file_crc32(file),
        #    3478595573)
