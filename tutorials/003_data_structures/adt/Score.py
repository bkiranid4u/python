"""
Custom Data structure to record the Score of the player
"""


class Entry:
    # Stores the Player name and the score
    def __init__(self, score, name) -> None:
        self._name = name
        self._score = score

    def get_name(self):
        return self._name

    def get_score(self):
        return self._score

    def __str__(self):
        return '({0}, {1})'.format(self._name, self._score)


class ScoreBoard:
    # Captures the score of the players

    def __init__(self, capacity=10) -> None:
        self._board = [None] * capacity
        self._size = 0

    def add(self, entry: Entry):
        score = entry.get_score()
        # Does the entry qualify to be part of the top 10 score
        # Checking if the score is greater than the last entry of all ready sorted score
        assert self._size < len(
            self._board) or score > self._board[-1], "It's not a top score"

        if self._size < len(self._board):
            # Means there is still place for the score to be added without popping other scores
            self._size += 1

        j = self._size - 1

        while j > 0 and self._board[j-1].get_score() < score:
            self._board[j] = self._board[j-1]
            j = j-1

        self._board[j] = entry

    def __str__(self) -> str:
        return '\n'.join(str(self._board[j]) for j in range(self._size))


scoreBoard = ScoreBoard()

scoreBoard.add(Entry('Kiran', 19))

print(str(scoreBoard))
