# SPDX-FileCopyrightText: (c) 2022 Artёm IG <github.com/rtmigo>
# SPDX-License-Identifier: MIT
import random
import unittest
from pathlib import Path

from lighthash import file_fibonacci_md5, HashAlgo
from lighthash import file_to_hash_fibonacci
from tests._tests_common import TempSizedFile

file = Path(__file__).parent / "data" / "public-domain-image.jpg"
zerofile = Path(__file__).parent / "data" / "zerofile.txt"


class TestFibonacci(unittest.TestCase):
    def test_outdated_md5(self):
        self.assertEqual(file_fibonacci_md5(file),
                         '2733248e623e759bb1e7737ab4b97e4a')
        self.assertEqual(file_fibonacci_md5(file, 2),
                         '4a8994806624aeabf601b3094f7e28e2')

    def test_file_to_hash_md5(self):
        self.assertEqual(file_to_hash_fibonacci(file),
                         '2733248e623e759bb1e7737ab4b97e4a')
        self.assertEqual(file_to_hash_fibonacci(file, HashAlgo.md5),
                         '2733248e623e759bb1e7737ab4b97e4a')
        self.assertEqual(file_to_hash_fibonacci(file, HashAlgo.md5, 1),
                         '2733248e623e759bb1e7737ab4b97e4a')
        self.assertEqual(file_to_hash_fibonacci(file, HashAlgo.md5, 2),
                         '4a8994806624aeabf601b3094f7e28e2')

    def test_file_to_hash_sha256(self):
        self.assertEqual(
            file_to_hash_fibonacci(file, HashAlgo.sha256),
            'c117a5eee3503e9ef6672ece41dc9dd361b45371a60c61f02c5b3d6c247cba08')
        self.assertEqual(
            file_to_hash_fibonacci(file, HashAlgo.sha256, 1),
            'c117a5eee3503e9ef6672ece41dc9dd361b45371a60c61f02c5b3d6c247cba08')
        self.assertEqual(
            file_to_hash_fibonacci(file, HashAlgo.sha256, 2),
            '5c3e4c2677ba055f10d315c33d1d40ca473a9a38207c782d589ad2de185d8963')

    def test_file_to_hash_crc32(self):
        self.assertEqual(
            file_to_hash_fibonacci(file, HashAlgo.crc32),
            'b02e9bce')
        self.assertEqual(
            file_to_hash_fibonacci(file, HashAlgo.crc32, 1),
            'b02e9bce')
        self.assertEqual(
            file_to_hash_fibonacci(file, HashAlgo.crc32, 2),
            'c54b2182')

    def test_zerofile(self):
        with TempSizedFile(0) as f:
            assert f.path.stat().st_size == 0
            self.assertEqual(file_to_hash_fibonacci(f.path),
                             '7dea362b3fac8e00956a4952a3d4f474')
            self.assertEqual(
                file_to_hash_fibonacci(f.path, algo=HashAlgo.crc32),
                '6522df69')

    def test_randoms(self):
        for _ in range(100):
            with TempSizedFile(random.randint(0, 10)) as f:
                file_to_hash_fibonacci(f.path, speedup=random.randint(1, 100))
