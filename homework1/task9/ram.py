class RAM():

    size_gb: int

    def __init__(self, size_gb: int):
        self._size_gb = size_gb

    @property
    def size_gb(self):
        return self._size_gb
