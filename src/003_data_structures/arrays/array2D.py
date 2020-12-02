from array import Array

class Array2D:

    def __init__(self,numRows,numCols):
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
        assert row >= 0 and row < self.numRows() and col >=0 and col < self.numCols(), "Array subscript out of range"
        
        rowArray = self._Rows[row]
        return rowArray[col]
    
    def __setitem__(self,ndxTuple,value):
        assert len(ndxTuple) == 2, "Invalid Number of array subscripts"
        row = ndxTuple[0]
        col = ndxTuple[1]
        assert row >= 0 and row < self.numRows() and col >= 0 and col < self.numCols(), "Array subscript out of range"
        rowArray = self._Rows[row]
        rowArray[col] = value
    