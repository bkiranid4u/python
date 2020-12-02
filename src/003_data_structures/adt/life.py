from arrays import Array2D
from typing import DefaultDict


class LifeGrid:
    # Define the live and dead cells
    LIVE_CELL = 1
    DEAD_CELL = 0

    def __init__(self, numRows, numCols):
        self._grid = Array2D(numRows, numCols)
        self.configure(list())

    def numRows(self):
        return self._grid.numRows()

    def numCols(self):
        return self._grid.numCols()

    def configure(self, coordList):

        for i in range(self.numRows()):
            for j in range(self.numCols()):
                self.clearCell(i, j)

        for coord in coordList:
            self.setCell(coord[0], coord[1])

    def clearCell(self, i, j):
        print(i)
        print(j)
        self._grid[i, j] = LifeGrid.DEAD_CELL

    def isLiveCell(self, row, col):
        return self._grid[row, col] == LifeGrid.LIVE_CELL

    def setCell(self, row, col):
        self._grid[row, col] = LifeGrid.LIVE_CELL

    def numLiveNeighbors(self, row, col):
        # Return the number of living cells sorounding the given cell
        # Row value is zero
        # Row value is len(self.numRows-1)
        # Col value is zero
        # Col value is len(self.numCols-1)
        rowStart = 0
        rowEnd = 0
        colStart = 0
        if row == 0:
            rowStart = 0
            rowEnd = 2
        elif row == (self.numRows() - 1):
            rowStart = row - 1
            rowEnd = row + 1
        else:
            rowStart = row - 1
            rowEnd = row + 2

        if col == 0:
            colStart = 0
            colEnd = 2
        elif col == (self.numCols() - 1):
            colStart = col - 1
            colEnd = col + 1
        else:
            colStart = col - 1
            colEnd = col + 2
        total = 0
        for i in range(rowStart, rowEnd):
            for j in range(colStart, colEnd):
                total += self._grid[i, j]
        return total
