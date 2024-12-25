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
                child_node = Node(child)
                self._considered_positions.add(child)
                current_node.add_child(child_node)
                queue.append(child_node)

    def print_move_tree(self):
        # Perform breadth-first traversal of the tree
        queue = deque([self._root])  # Start from the root node
        while queue:
            current_node = queue.popleft()
            # Print the current node's value
            print(f"Node: {current_node.value}")

            # If the node has children, print them as well
            if current_node.children:
                print(
                    f"  Children: {', '.join(str(child.value) for child in current_node.children)}"
                )

            # Add all children to the queue for further exploration
            queue.extend(current_node.children)

    # Add this method to your KnightPathFinder clase

    def find_path(self, end_position):
        # self.build_move_tree()
        node_to_find = self._root.breadth_search(end_position)
        return self.trace_to_root(node_to_find)

    def trace_to_root(self, end_node):
        current = end_node
        queue = deque()
        while current:
            queue.appendleft(current.value)
            current = current.parent
        return list(queue)


# finder = KnightPathFinder((0, 0))
# print(finder.new_move_positions((0, 0)))

# finder = KnightPathFinder((0, 0))
# finder.build_move_tree()
# print(finder._root.children)

finder = KnightPathFinder((0, 0))
finder.build_move_tree()
print(finder.find_path((5, 1)))  # => [(0, 0), (2, 1)]
print(finder.find_path((3, 3)))  # => [(0, 0), (2, 1), (3, 3)]
print(finder.find_path((6, 2)))  # => [(0, 0), (1, 2), (2, 4), (4, 3), (6, 2)]
print(finder.find_path((7, 6)))  # => [(0, 0), (1, 2), (2, 4), (4, 3), (5, 5), (7, 6)]
