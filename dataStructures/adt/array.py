import ctypes

class Array:
    # Creates an array with size elements
    def __init__( self, size):
        assert size > 0, "Array size must be greater than zero"
        self._size = size
        # Creates array structure using ctype module 
        PyArrayType = ctypes.py_object * size
        self._elements = PyArrayType()
        self.clear ( None )

    # Returns the length of the array 
    def __len__( self ):
        return self._size

    #  Returns the contents of the index item
    def __getitem__( self, index ):
        assert index >= 0 and index < len( self ), "Array subscript out of range"
        return self._elements[ index ]

    #  Puts an item at the given index
    def __setitem__( self, index, value ):
        assert index >= 0 and index < len( self ), "Array subscript out of range"
        self._elements[ index ] = value
    
    #  Clears the array with given value 
    def clear( self, value ):
        for i in range( len( self ) ):
            self._elements[ i ] = value
    
    #  Returns the array's iterator for traversing through array elements

    def __iter__( self ):
        return _ArrayIterator( self._elements )

class _ArrayIterator:
    def __init__( self, theArray ):
        self._arrayRef = theArray
        self._curIndex = 0
    
    def __iter__( self ):
        if self._curIndex < len(self._arrayRef):
            entry = self._arrayRef[ self._curIndex ]
            self._curIndex += 1
            return entry
        else:
            raise StopIteration
