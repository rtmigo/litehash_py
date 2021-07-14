# [coarse_hash](https://github.com/rtmigo/coarse_hash_py)

Calculates fast but very coarse hashes from files.

This package is hastily made, barely documented, and is not intended to be used
by anyone.

# Install

``` bash
$ pip3 install git+https://github.com/rtmigo/fast_file_hash_py#egg=fast_file_hash
```

# Use

``` python3
from coarse_hash import coarse_file_crc32

print(coarse_file_crc32('/path/to/file.dat'))
```