# -*- coding: utf-8 -*-

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 17:31:36 2020

@author: Kiran 
"""


# Implements the Array ADT using array capabilities of the ctypes module.
import ctypes


class Array:
    # Creates an array with size elements.
    def __init__(self, size):
        assert size > 0, "Array size must be > 0"
        self._size = size
        # Create the array structure using the ctypes module.
        PyArrayType = ctypes.py_object * size
        self._elements = PyArrayType()
        # Initialize each element.
        self.clear(None)
       # Returns the size of the array.

    def __len__(self):
        return self._size

    # Gets the contents of the index element.
    def __getitem__(self, index):
        assert index >= 0 and index < len(self), "Array subscript out of range"
        return self._elements[index]
    # Puts the value in the array element at index position.

    def __setitem__(self, index, value):
        assert index >= 0 and index < len(self), "Array subscript out of range"
        self._elements[index] = value
    # Clears the array by setting each element to the given value.

    def clear(self, value):
        for i in range(len(self)):
            self._elements[i] = value
         # Returns the array's iterator for traversing the elements.

    def __iter__(self):
        return _ArrayIterator(self._elements)
# An iterator for the Array ADT.


class _ArrayIterator:
    def __init__(self, theArray):
        self._arrayRef = theArray
        self._curNdx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._curNdx < len(self._arrayRef):
            entry = self._arrayRef[self._curNdx]
            self._curNdx += 1
            return entry
        else:
            raise StopIteration


class Array2D:

    def __init__(self, numRows, numCols):
        self._Rows = Array(numRows)

        for i in range(len(self._Rows)):
            self._Rows[i] = Array(numCols)

    def numRows(self):
        return len(self._Rows)

    def numCols(self):
        return len(self._Rows[0])

    def clear(self, value):
        for i in range(self.numRows()):
            self._Rows[i].clear(value)

    def __getitem__(self, ndxTuple):
        assert len(ndxTuple) == 2, "Invalid Number of array subscripts"
        row = ndxTuple[0]
        col = ndxTuple[1]
        assert row >= 0 and row < self.numRows(
        ) and col >= 0 and col < self.numCols(), "Array subscript out of range"

        rowArray = self._Rows[row]
        return rowArray[col]

    def __setitem__(self, ndxTuple, value):
        assert len(ndxTuple) == 2, "Invalid Number of array subscripts"
        row = ndxTuple[0]
        col = ndxTuple[1]
        assert row >= 0 and row < self.numRows(
        ) and col >= 0 and col < self.numCols(), "Array subscript out of range"
        rowArray = self._Rows[row]
        rowArray[col] = value
