# [coarse_hash](https://github.com/rtmigo/coarse_hash_py)

Calculates fast but very coarse hashes from files. The hash is made up of the
file size and rare bytes of the file.

This allows you to get hashes of large files very quickly. However, such a hash
may not display minor differences within the files.

# Install

``` bash
$ pip3 install git+https://github.com/rtmigo/coarse_hash_py#egg=coarse_hash
```

# Use

``` python3
from coarse_hash import coarse_file_crc32

print(coarse_file_crc32('/path/to/file.dat'))
```