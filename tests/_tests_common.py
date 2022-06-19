import os
import tempfile
from pathlib import Path
from typing import Optional, Any


class TempSizedFile:
    def __init__(self, size: int):
        self._ntf: Optional[Any] = None
        self._size = size

    @property
    def path(self):
        return Path(self._ntf.name)

    def __enter__(self):
        self._ntf = tempfile.NamedTemporaryFile(delete=False)
        self.path.write_bytes(os.urandom(self._size))
        assert self.path.stat().st_size == self._size
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            os.remove(self._ntf.name)
        except PermissionError:
            if os.name == "nt":
                pass  # we knew it ;)
            else:
                raise

