""" 
    Stack Implementation using python lists
"""


class ArrayStack:

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        print(len(self._data))
        return len(self._data) == 0

    def push(self, data):
        self._data.append(data)

    def top(self):
        assert not self.is_empty(), "Empty Stack"
        return self._data[-1]

    def pop(self):
        assert not self.is_empty(), "Empty Stack"
        return self._data.pop()
