# SPDX-FileCopyrightText: (c) 2021-2022 Artёm IG <github.com/rtmigo>
# SPDX-License-Identifier: MIT

from ._common import HashAlgo
from ._equidistant import file_equidistant_crc32, file_equidistant_md5, \
    file_to_hash_equidistant
from ._fibonacci import file_fibonacci_crc32, file_fibonacci_md5, \
    file_to_hash_fibonacci
