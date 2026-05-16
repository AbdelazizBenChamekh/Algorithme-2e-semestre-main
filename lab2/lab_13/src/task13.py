import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

file_path1 = os.path.abspath(os.path.join(os.path.dirname(__file__), "../txtf/input.txt"))
file_path2 = os.path.abspath(os.path.join(os.path.dirname(__file__), "../txtf/output.txt"))

from lab2.utils import read_input_file2, write_output_file

class AVLTree:
    def __init__(self, nodes):
        self.tree = {}
        self.keys = []
        for i, (key, left, right) in enumerate(nodes):
            self.tree[key] = (left, right)
            self.keys.append(key)

    def left_rotate(self):
        root = self.keys[0]

        if root not in self.tree:
            return self.tree

        right_child = self.tree[root][1]

        if right_child == 0:
            return self.tree 

        right_left, right_right = self.tree.get(right_child, (0, 0))

        new_root = right_child
        self.tree[new_root] = (root, right_right)
        self.tree[root] = (self.tree[root][0], right_left)

        del self.tree[right_child]

        return self.tree

tree_data = read_input_file2(file_path1)
n = int(tree_data[0])
nodes = [list(map(int, tree_data[i + 1].split())) for i in range(n)]

avl = AVLTree(nodes)
rotated_tree = avl.left_rotate()

output_data = f"{n}\n" + "\n".join(f"{key} {left} {right}" for key, (left, right) in rotated_tree.items())
write_output_file(file_path2, output_data)



