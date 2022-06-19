# SPDX-FileCopyrightText: (c) 2022 Artёm IG <github.com/rtmigo>
# SPDX-License-Identifier: MIT

import random
import unittest
from pathlib import Path

from lighthash import HashAlgo
from lighthash._equidistant import file_to_hash_equidistant
from tests._tests_common import TempSizedFile

file = Path(__file__).parent / "data" / "public-domain-image.jpg"
zerofile = Path(__file__).parent / "data" / "zerofile.txt"


class TestEquidistant(unittest.TestCase):

    def test_file_to_hash_md5(self):
        self.assertEqual(file_to_hash_equidistant(file),
                         '16d3a8bd9cc513b4eb6a30c675253f0f')
        self.assertEqual(file_to_hash_equidistant(file, HashAlgo.md5),
                         '16d3a8bd9cc513b4eb6a30c675253f0f')
        self.assertEqual(file_to_hash_equidistant(file, HashAlgo.md5, 8),
                         '16d3a8bd9cc513b4eb6a30c675253f0f')
        self.assertEqual(file_to_hash_equidistant(file, HashAlgo.md5, 17),
                         '84b0f635354c52e130a6b2439aac02de')

    def test_file_to_hash_sha256(self):
        self.assertEqual(
            file_to_hash_equidistant(file, HashAlgo.sha256),
            'bf9a4bd0eadeda7b178ff2d3340b08f14f808601a299fb0b343d5738449b39d9')
        self.assertEqual(
            file_to_hash_equidistant(file, HashAlgo.sha256, 8),
            'bf9a4bd0eadeda7b178ff2d3340b08f14f808601a299fb0b343d5738449b39d9')
        self.assertEqual(
            file_to_hash_equidistant(file, HashAlgo.sha256, 17),
            'a78c0303f7aa43a3865410f3e5ac0ddd2fb5e4ebb8c716d764b262352daf2588')

    def test_file_to_hash_crc32(self):
        self.assertEqual(
            file_to_hash_equidistant(file, HashAlgo.crc32),
            '74d26036')
        self.assertEqual(
            file_to_hash_equidistant(file, HashAlgo.crc32, 8),
            '74d26036')
        self.assertEqual(
            file_to_hash_equidistant(file, HashAlgo.crc32, 17),
            '2964686a')

    def test_zerofile(self):
        self.assertEqual(zerofile.stat().st_size, 0)
        self.assertEqual(file_to_hash_equidistant(zerofile),
                         '7dea362b3fac8e00956a4952a3d4f474')
        self.assertEqual(
            file_to_hash_equidistant(zerofile, algo=HashAlgo.crc32),
            '6522df69')

    def test_args(self):
        file_to_hash_equidistant(file)
        with self.assertRaises(ValueError):
            file_to_hash_equidistant(file, n=-1)
        file_to_hash_equidistant(file, n=1)
        file_to_hash_equidistant(file, n=2)
        file_to_hash_equidistant(file, n=9999999999999999)

    def test_randoms(self):
        for _ in range(100):
            with TempSizedFile(random.randint(0, 10)) as f:
                file_to_hash_equidistant(f.path, n=random.randint(1, 100))
