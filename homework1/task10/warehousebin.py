
class WarehouseBin:

    def __init__(self):
        self._items = set()

    def add(self, item):
        self._items.add(item)

    def __len__(self):
        return len(self._items)

    def __contains__(self, item):
        return item in self._items

    def __iter__(self):
        return iter(self._items)
