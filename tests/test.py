import unittest

from coarse_hash._old import _iter_nonzero_bytes


class TestNonzero(unittest.TestCase):
    def test_iterNonzeroBytes(self):
        assert list(_iter_nonzero_bytes(0x0)) == []
        assert list(_iter_nonzero_bytes(0x1122)) == [0x22, 0x11]
        assert list(_iter_nonzero_bytes(0x11220033)) == [0x33, 0x00, 0x22, 0x11]
