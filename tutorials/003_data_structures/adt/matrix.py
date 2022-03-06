from arrays import Array2D

class Matrix:

    def __init__(self,numRows,numCols):
        self._grid= Array2D(numRows,numCols)
        self._grid.clear(0)

    def numRows(self):
        return self._grid.numRows()

    def numCols(self):
        return self._grid.numCols()

    def __getitem__(self, ndxTuple):
        return self._grid[ndxTuple[0], ndxTuple[1]]

    def __setitem__(self,ndxTuple,value):
        print(value)
        self._grid[ndxTuple[0],ndxTuple[1]] = value

    def scaleBy(self, value):
        
        for i in range(self.numRows()):
            for j in range(self.numCols()):
                self._grid[i, j] *= value

    def transpose(self):
        transposedGrid = Array2D(self.numCols(), self.numRows())
        for row in range(self.numCols()):
            for col in range(self.numRows()):
                transposedGrid[row,col] = self._grid[col, row]
        return transposedGrid

    def __add__(self, rhsMatrix):

        assert rhsMatrix.numRows() == self.numRows() and rhsMatrix.numCols() == self.numCols(), 'Matrix Sizes not compatable for addition'

        resultantMatrix = Array2D(self.numRows(), self.numCols())

        for r in range(self.numRows()):
            for c in range(self.numCols()):
                resultantMatrix[r,c] = self._grid[ r, c ] + rhsMatrix[ r, c ]
        return resultantMatrix

    def __sub__(self, rhsMatrix):
        assert rhsMatrix.numRows() == self.numRows() and rhsMatrix.numCols() == self.numCols(), 'Matrix Sizes not compatable for substraction'

        resultantMatrix = Array2D(self.numRows(), self.numCols())

        for r in range(self.numRows()):
            for c in range(self.numCols()):
                resultantMatrix[r,c] = self._grid[ r, c ] - rhsMatrix[ r, c ]
        return resultantMatrix

    def __mul__(self, rhsMatrix):
        assert rhsMatrix.numRows() == self.numCols(), 'Matrix Sizes are not compatable for multiplication'

        result = Array2D(self.numCols(), self.numRows())

        for r in range(self.numRows()):
            for p in range(rhsMatrix.numCols):
                for c in range(rhsMatrix.numRows()):
                    result[r][c] += self._grid[r][c] * rhsMatrix[p][c]
        


matrix = Matrix(2,2)
matrix[1,1] =9
matrix[0,1] =9
matrix.scaleBy(9)
print(matrix[1,1])
print(matrix.transpose()[1,0])
