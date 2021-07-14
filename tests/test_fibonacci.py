# SPDX-FileCopyrightText: (c) 2021 Artёm IG <github.com/rtmigo>
# SPDX-License-Identifier: MIT

import unittest
from itertools import islice

from coarse_hash._fibonacci import fibonacci_sequence


class TestIterFibo(unittest.TestCase):

    def test_fibonacci(self):
        self.assertEqual(
            list(islice(fibonacci_sequence(), 10)),
            [0, 1, 2, 3, 5, 8, 13, 21, 34, 55])

        self.assertEqual(
            list(islice(fibonacci_sequence(2), 12)),
            [0, 2, 4, 6, 10, 16, 26, 42, 68, 110, 178, 288])
