import unittest
from pathlib import Path

from coarse_hash import fastHashCRC64

file = Path(__file__).parent / "data" / "public-domain-image.jpg"


class TestDirtyHash(unittest.TestCase):
    def test_str(self):
        self.assertEqual(
            fastHashCRC64(str(file)),
            6722160219219441570)

    def test(self):
        self.assertEqual(
            fastHashCRC64(file),
            6722160219219441570)

        self.assertEqual(
            fastHashCRC64(file, bytes_to_read=10),
            787582093389868693)


