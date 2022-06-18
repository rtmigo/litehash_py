# SPDX-FileCopyrightText: (c) 2022 Artёm IG <github.com/rtmigo>
# SPDX-License-Identifier: MIT

import unittest
from pathlib import Path

from lighthash._equidistant import file_equidistant_md5

file = Path(__file__).parent / "data" / "public-domain-image.jpg"


class TestEuaiMd5(unittest.TestCase):
    # noinspection PyDeprecation
    def test(self):
        self.assertEqual(
            file_equidistant_md5(file),
            '16d3a8bd9cc513b4eb6a30c675253f0f')
        self.assertEqual(
            file_equidistant_md5(file, n=2),
            '789eff904cc1fe9db32def64dcd4cbd0')
