from collections import deque


class Node:
    def __init__(self, value):
        self._value = value
        self._parent = None
        self._children = []

    @property
    def value(self):
        return self._value

    @property
    def children(self):
        return self._children

    def add_child(self, node):
        # if node is None:
        #     return
        if node not in self._children:
            self._children.append(node)
            if node._parent is not self:
                node.parent = self

    def remove_child(self, node):
        # if node is None:
        #     return
        if node in self._children:
            self._children = [n for n in self._children if n != node]
            node.parent = None

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, node):
        if node is None:
            self._parent = None
            return
        if self._parent:
            self._parent.remove_child(self)
        currentNode = self
        newParent = node

        # if self == node:
        #     return  # nothing to do

        currentNode._parent = newParent
        node.add_child(self)

    def depth_search(self, value):
        # Check the current node's value
        if self.value == value:
            return self

        # Recursively search through all children
        for child in self.children:
            found_node = child.depth_search(value)
            if found_node:
                return found_node

        # Return None if the value isn't found in the tree
        return None

    def breadth_search(self, target):
        queue = deque([self])  # Use a deque for efficient popping from the front
        while queue:
            current_node = queue.popleft()
            if current_node.value == target:
                return current_node
            queue.extend(current_node.children)  # Add children to the queue
        return None


# node1 = Node("root1")
# node2 = Node("root2")
# node3 = Node("root3")

# node3.parent = node1

# node3.parent = node2

# print(node1.children) # root 1
# print(node2.children) # root 2
