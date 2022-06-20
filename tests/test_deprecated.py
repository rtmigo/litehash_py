import unittest
from pathlib import Path

from litehash import file_equidistant_md5, file_equidistant_crc32, \
    file_fibonacci_md5, file_fibonacci_crc32

file = Path(__file__).parent / "data" / "public-domain-image.jpg"


class TestDeprecated(unittest.TestCase):
    # noinspection PyDeprecation
    def test(self):
        with self.assertWarns(DeprecationWarning):
            self.assertEqual(
                file_equidistant_md5(file),
                '16d3a8bd9cc513b4eb6a30c675253f0f')
            self.assertEqual(
                file_equidistant_md5(file, n=2),
                '789eff904cc1fe9db32def64dcd4cbd0')

    def test_crc(self):
        with self.assertWarns(DeprecationWarning):
            self.assertEqual(
                file_equidistant_crc32(str(file)),
                1959944246)
        with self.assertWarns(DeprecationWarning):
            self.assertEqual(
                file_equidistant_crc32(file),
                1959944246)

    def test_outdated_md5(self):
        with self.assertWarns(DeprecationWarning):
            self.assertEqual(file_fibonacci_md5(file),
                             '2733248e623e759bb1e7737ab4b97e4a')
            self.assertEqual(file_fibonacci_md5(file, 2),
                             '4a8994806624aeabf601b3094f7e28e2')


class TestFibonacciOldCrc32(unittest.TestCase):
    def test_str(self):
        with self.assertWarns(DeprecationWarning):
            self.assertEqual(
                file_fibonacci_crc32(str(file)),
                2955844558)

    def test(self):
        with self.assertWarns(DeprecationWarning):
            self.assertEqual(
                file_fibonacci_crc32(file),
                2955844558)

    def test_speedup(self):
        with self.assertWarns(DeprecationWarning):
            self.assertEqual(
                file_fibonacci_crc32(file, speedup=2),
                3310035330)
            self.assertEqual(
                file_fibonacci_crc32(file, speedup=3),
                3834401308)
