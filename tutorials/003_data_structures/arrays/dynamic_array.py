import ctypes

class DynamicArray:

    def __init__(self):
        self._size = 0
        self._capacity = 1
        self._array = self._make_an_array(self._capacity)
    
    def __len__(self):
        return self._size

    def __getitem__(self,index):
        # assert index >= 0 and index < self._size, 'Array Subscript out of index'
        if not 0 <= index < self._size:
            raise IndexError('Invalid Index')
        return self._array[index]
    
    def append(self,item):
        # Append an item to the array
        # Check if the array has the capacity to add the new item
        if self._size == self._capacity:
            self._resize_array(2 * self._capacity)
        self._array[self._size] = item
        self._size = self._size + 1

    def _resize_array(self,capacity):
        resizedArray = self._make_an_array(capacity)
        for i in range(self._size):
            resizedArray[i] = self._array[i]
        self._array = resizedArray
        self._capacity = capacity

    def _make_an_array(self,capacity):
        return (capacity * ctypes.py_object )()

array = DynamicArray()