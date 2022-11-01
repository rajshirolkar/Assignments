from typing import List

board = [
    "......................",
    "......##########......",
    "......#........#......",
    "......#........#......",
    "......#........#####..",
    "....###............#..",
    "....#............###..",
    "....##############....",
]


def flood_fill(input_board: List[str], old: str, new: str, x: int, y: int) -> List[str]:
    """Returns board with old values replaced with new values
    through flood filling starting from the coordinates x, y
    Args:
        input_board (List[str])
        old (str): Value to be replaced
        new (str): Value that replaces the old
        x (int): X-coordinate of the flood start point
        y (int): Y-coordinate of the flood start point
    Returns:
        List[str]: Modified board
    """

    # Implement your code here.
    if input_board[x][y] == old:

        # get column in list
        column = list(input_board[x])
        column[y] = new
        #convert back to string
        input_board[x] = ''.join(column)
        flood_fill(input_board, old, new, x-1, y)
        flood_fill(input_board, old, new, x+1, y)
        flood_fill(input_board, old, new, x, y-1)
        flood_fill(input_board, old, new, x, y+1)
        return input_board
    else:
        return

modified_board = flood_fill(input_board=board, old=".", new="~", x=5, y=12)
# printing the board after implementing flood fill
for a in modified_board:
    print(a)
