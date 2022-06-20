# SPDX-FileCopyrightText: (c) 2021 Artёm IG <github.com/rtmigo>
# SPDX-License-Identifier: MIT

import unittest
from io import BytesIO, SEEK_SET

from litehash._fibonacci import _iter_fibo


class TestFibonacciPositions(unittest.TestCase):
    def test_iter_shifted(self):
        with BytesIO() as stream:
            for x in range(256):
                stream.write(bytes((x,)))
            stream.seek(0, SEEK_SET)
            data = list(_iter_fibo(stream, 1))
        self.assertEqual(
            data,
            [0, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233])
