# SPDX-FileCopyrightText: (c) 2022 Artёm IG <github.com/rtmigo>
# SPDX-License-Identifier: MIT

import unittest
from pathlib import Path

from coarse_hash import file_fibonacci_md5

file = Path(__file__).parent / "data" / "public-domain-image.jpg"


class TestFibonacciMd5(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(
            file_fibonacci_md5(file),
            '2733248e623e759bb1e7737ab4b97e4a')

    def test_speedup(self):
        self.assertEqual(
            file_fibonacci_md5(file, 2),
            '4a8994806624aeabf601b3094f7e28e2')
