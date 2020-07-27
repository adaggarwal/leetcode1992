'''
348. Design Tic-Tac-Toe
Medium
271
21


Design a Tic-tac-toe game that is played between two players on a n x n grid.

You may assume the following rules:

A move is guaranteed to be valid and is placed on an empty block.
Once a winning condition is reached, no more moves is allowed.
A player who succeeds in placing n of their marks in a horizontal, vertical, or diagonal row wins the game.
Example:
Given n = 3, assume that player 1 is "X" and player 2 is "O" in the board.

TicTacToe toe = new TicTacToe(3);

toe.move(0, 0, 1); -> Returns 0 (no one wins)
|X| | |
| | | |    // Player 1 makes a move at (0, 0).
| | | |

toe.move(0, 2, 2); -> Returns 0 (no one wins)
|X| |O|
| | | |    // Player 2 makes a move at (0, 2).
| | | |

toe.move(2, 2, 1); -> Returns 0 (no one wins)
|X| |O|
| | | |    // Player 1 makes a move at (2, 2).
| | |X|

toe.move(1, 1, 2); -> Returns 0 (no one wins)
|X| |O|
| |O| |    // Player 2 makes a move at (1, 1).
| | |X|

toe.move(2, 0, 1); -> Returns 0 (no one wins)
|X| |O|
| |O| |    // Player 1 makes a move at (2, 0).
|X| |X|

toe.move(1, 0, 2); -> Returns 0 (no one wins)
|X| |O|
|O|O| |    // Player 2 makes a move at (1, 0).
|X| |X|

toe.move(2, 1, 1); -> Returns 1 (player 1 wins)
|X| |O|
|O|O| |    // Player 1 makes a move at (2, 1).
|X|X|X|

'''

'''
Personally, I didn't get the intuition correct before I saw -> https://leetcode.com/problems/design-tic-tac-toe/discuss/81898/Java-O(1)-solution-easy-to-understand
But then, just to reiterate the meat of that solution:
***
1. We don't store the whole tic-tac-toe board and it's state.
2. Just store the state of pertinent row/col/diagonal/anti-diagonal.
3. By state, what we mean is -> how many times any of the two players have picked that row and column. (Hence the O(1) solution)
4. At any point, as the state becomes the total size 'n'; we have a winner! Congratulations current player :)

***

For solutions to other problems, feel free to visit -> https://github.com/adityaaggarwal1992/leetcode1992

'''

class TicTacToe:

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.row = [0 for x in range(n)]
        self.col = [0 for x in range(n)]
        self.diag = 0
        self.undiag = 0
        self.n = n
        

    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        order = 1 if player == 1 else -1
        self.row[row] += order
        self.col[col] += order
        if row == col:
            self.diag += order
        if col == self.n-1 -row:
            self.undiag += order
        if abs(self.row[row]) == self.n or \
            abs(self.col[col]) == self.n or \
            abs(self.diag) == self.n or \
            abs(self.undiag) == self.n:
            return player
        else:
            return 0
            