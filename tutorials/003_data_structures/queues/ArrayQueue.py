"""  """

class ArrayQueue:
    _def_capacity = 0

    def __init__(self) -> None:
        self._size= 0
        self._data = [None] * self._def_capacity
        self._front = 0
    
    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0 
    
    def first(self):
        return self._data[self._front]

    def dequeue(self):
        assert not self.is_empty(), 'Empty Queue'
        item = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size = self._size -1
        return item

        
    def enqueue(self,data):
        # Check if the queue has the capacity to add a new item
        if self._size == len(self._data):
            self._resize(self._def_capacity*2)
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = data
        self._size += 1
    
    def _resize(self,capacity):

        old = self._data
        self._data = [None] * capacity
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (walk +1)% len(old)
        self._front = 0
