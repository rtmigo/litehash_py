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

Calculate the checksum based on ten equidistant bytes, and the file size. 
The very first and the very last byte of the file will be among the ten read.

``` python3
from coarse_hash import file_equidistant_crc32 

print(file_equidistant_crc32('/path/to/file.dat', n=10))
```

Calculate the checksum based on the bytes located at an increasing distance from
each other, and the file size. In this case, we will read more bytes from the
file header than from the body.

``` python3
from coarse_hash import file_fibonacci_crc32, file_fibonacci_md5

print(file_fibonacci_crc32('/path/to/file.dat'))
print(file_fibonacci_md5('/path/to/file.dat'))
```
