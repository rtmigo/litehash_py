# SPDX-FileCopyrightText: (c) 2021 Artёm IG <github.com/rtmigo>
# SPDX-License-Identifier: MIT

import unittest
from io import BytesIO, SEEK_SET
from pathlib import Path

from coarse_hash import file_fibonacci_crc32
from coarse_hash._fibonacci import _iter_fibo

file = Path(__file__).parent / "data" / "public-domain-image.jpg"


class TestCoarse32(unittest.TestCase):
    def test_iter_shifted(self):
        with BytesIO() as stream:
            for x in range(256):
                stream.write(bytes((x,)))
            stream.seek(0, SEEK_SET)
            data = list(_iter_fibo(stream, 1))
        self.assertEqual(
            data,
            [0, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233])

    def test_str(self):
        self.assertEqual(
            file_fibonacci_crc32(str(file)),
            2955844558)

    def test(self):
        self.assertEqual(
            file_fibonacci_crc32(file),
            2955844558)

    def test_speedup(self):
        self.assertEqual(
            file_fibonacci_crc32(file, speedup=2),
            3310035330)
        self.assertEqual(
            file_fibonacci_crc32(file, speedup=3),
            3834401308)

