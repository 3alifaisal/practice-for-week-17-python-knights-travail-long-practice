from tree import Node
from collections import deque


class KnightPathFinder:
    def __init__(self, pos):

        if not isinstance(pos, tuple) or len(pos) != 2:
            raise TypeError(
                "You must provide a tuple with two integers (x, y) as the starting position."
            )
        x, y = pos

        if not (isinstance(x, int) and isinstance(y, int)):
            raise TypeError("Coordinates must be integers.")
        if not (0 <= x < 8 and 0 <= y < 8):
            raise ValueError(
                "Starting coordinates must be within the 8x8 board boundaries."
            )
        self._pos = pos
        self._root = Node(pos)
        self._considered_positions = {pos}

    def get_valid_moves(self, pos):
        x, y = pos
        possible_moves = [
            (x + 1, y + 2),
            (x + 1, y - 2),
            (x - 1, y + 2),
            (x - 1, y - 2),
            (x + 2, y + 1),
            (x + 2, y - 1),
            (x - 2, y + 1),
            (x - 2, y - 1),
        ]
        # Filter moves within board boundaries (if simulating an 8x8 chessboard)
        return [(mx, my) for mx, my in possible_moves if 0 <= mx < 8 and 0 <= my < 8]

    def new_move_positions(self, pos):
        valid_moves = self.get_valid_moves(pos)
        new_moves = [i for i in valid_moves if i not in self._considered_positions]
        return new_moves

    def build_move_tree(self):
        queue = deque([self._root])
        while queue:
            current_node = queue.popleft()
            children = self.new_move_positions(current_node.value)
            for child in children:
                self._considered_positions.add(child)
                current_node.add_child(Node(child))
                queue.append(Node(child))


# finder = KnightPathFinder((0, 0))
# print(finder.new_move_positions((0, 0)))

finder = KnightPathFinder((0, 0))
finder.build_move_tree()
print(finder._root.children)
