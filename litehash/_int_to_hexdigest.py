# SPDX-FileCopyrightText: (c) 2022 Artёm IG <github.com/rtmigo>
# SPDX-License-Identifier: MIT

import unittest

from litehash._common import _uint32_to_hexdigest


class IntHexdigestTest(unittest.TestCase):
    def test(self):
        self.assertEqual(_uint32_to_hexdigest(0), '00000000')
        self.assertEqual(_uint32_to_hexdigest(1), '00000001')
        self.assertEqual(_uint32_to_hexdigest(1535277435), '5b82797b')
        self.assertEqual(_uint32_to_hexdigest(0xFFFFFFFF), 'ffffffff')
        with self.assertRaises(ValueError):
            _uint32_to_hexdigest(153527743555)
        with self.assertRaises(ValueError):
            _uint32_to_hexdigest(-1)
