# SPDX-FileCopyrightText: (c) 2021 Artёm IG <github.com/rtmigo>
# SPDX-License-Identifier: MIT

import unittest
from io import BytesIO, SEEK_SET
from pathlib import Path

from coarse_hash import file_equidistant_crc32
from coarse_hash._equidistant import _equidistant_bytes

file = Path(__file__).parent / "data" / "public-domain-image.jpg"


class TestCoarse32(unittest.TestCase):
    def test_iter_shifted(self):
        SIZE = 256
        with BytesIO() as stream:
            for x in range(SIZE):
                stream.write(bytes((x,)))
            stream.seek(0, SEEK_SET)
            data = list(_equidistant_bytes(stream, SIZE, 10))
        self.assertEqual(
            data,
            [0, 28, 57, 85, 113, 142, 170, 198, 227, 255])

    def test_str(self):
        self.assertEqual(
            file_equidistant_crc32(str(file)),
            1959944246)

    def test(self):
        self.assertEqual(
            file_equidistant_crc32(file),
            1959944246)
