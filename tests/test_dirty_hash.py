import unittest
from pathlib import Path

from fast_file_hash import dirty_fast_file_crc64

file = Path(__file__).parent / "data" / "public-domain-image.jpg"


class TestDirtyHash(unittest.TestCase):
    def test_str(self):
        self.assertEqual(
            dirty_fast_file_crc64(str(file)),
            6722160219219441570)

    def test(self):
        self.assertEqual(
            dirty_fast_file_crc64(file),
            6722160219219441570)

        self.assertEqual(
            dirty_fast_file_crc64(file, bytes_to_read=10),
            787582093389868693)


