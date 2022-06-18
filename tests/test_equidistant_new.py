# SPDX-FileCopyrightText: (c) 2022 Artёm IG <github.com/rtmigo>
# SPDX-License-Identifier: MIT

import unittest
from pathlib import Path

from lighthash import file_fibonacci_md5, HashAlgo
from lighthash._equidistant import file_to_hash_equidistant
from lighthash._fibonacci import file_to_hash_fibonacci

file = Path(__file__).parent / "data" / "public-domain-image.jpg"


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
