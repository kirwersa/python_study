class Playlist:
    def __init__(self, tracks: dict):
        self._tracks = tracks

    def __getitem__(self, key):
        return self._tracks[key]

    def __setitem__(self, key, value):
        self._tracks[key] = value

    def __repr__(self):
        return f"{self._tracks}"
