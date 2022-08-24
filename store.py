from abstract import Storage


class Store(Storage):

    def __init__(self, items: dict, capacity=100):
        self._items = items
        self._capacity = capacity

    @property
    def items(self):
        return self._items

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, count):
        self._capacity = count

    def add(self, name, count):
        """Add items to the store, taking into capacity limits"""
        if name in self._items.keys():
            if self.get_free_space() >= count:
                self._items[name] += count
                print("Item added")
                return True
            else:
                print("Not enough storage space!")
                return False

        else:
            if self.get_free_space() >= count:
                print("Item added")
                self._items[name] = count
                return True
            else:
                print("Not enough storage space!")
                return False

    def remove(self, name, count):
        """ reduce the number of items but not below zero"""
        if self._items[name] >= count:
            self._items[name] -= count
            print("This quantity is in store")
            return True
        else:
            print(f"We can remove just {self._items[name]}")
            return False

    def get_free_space(self):
        """return free space"""
        current_space = 0
        for value in self._items.values():
            current_space += value
        return self._capacity - current_space

    # def get_items(self):
    #     return self._items

    def get_unique_items_count(self):
        """ return unique items count"""
        return len(self._items.keys())

    def __repr__(self):
        return f"{self._items.items()}"




