# SPDX-FileCopyrightText: (c) 2021 Artёm IG <github.com/rtmigo>
# SPDX-License-Identifier: MIT

import unittest

from lighthash._equidistant import _equidistant_positions


class TestEqual(unittest.TestCase):

    def test(self):
        self.assertEqual(
            _equidistant_positions(1000, 5),
            [0, 250, 500, 749, 999])
        self.assertEqual(
            _equidistant_positions(1000, 11),
            [0, 100, 200, 300, 400, 500, 599, 699, 799, 899, 999])

    def test_n1(self):
        self.assertEqual(_equidistant_positions(0, 1), [])
        self.assertEqual(_equidistant_positions(1, 1), [0])
        self.assertEqual(_equidistant_positions(2, 1), [0])
        self.assertEqual(_equidistant_positions(3, 1), [1])
        self.assertEqual(_equidistant_positions(4, 1), [2])
        self.assertEqual(_equidistant_positions(10, 1), [4])

    def test_size_zero(self):
        self.assertEqual(
            _equidistant_positions(0, 5),
            [])

    def test_size_one(self):
        self.assertEqual(
            _equidistant_positions(1, 5),
            [0])

    def test_size_two(self):
        self.assertEqual(
            _equidistant_positions(2, 5),
            [0, 1])

    def test_size_five(self):
        self.assertEqual(
            _equidistant_positions(5, 5),
            [0, 1, 2, 3, 4])

        self.assertEqual(
            _equidistant_positions(5, 50),
            [0, 1, 2, 3, 4])


if __name__ == "__main__":
    unittest.main()
