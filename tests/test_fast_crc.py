import unittest
from pathlib import Path

from coarse_hash import coarse_file_crc32

file = Path(__file__).parent / "data" / "public-domain-image.jpg"


class TestDirtyHash(unittest.TestCase):
    def test_str(self):
        self.assertEqual(
            coarse_file_crc32(str(file)),
            3478595573)

    def test(self):
        self.assertEqual(
            coarse_file_crc32(file),
            3478595573)




