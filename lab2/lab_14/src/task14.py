import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

file_path1 = os.path.abspath(os.path.join(os.path.dirname(__file__), "../txtf/input.txt"))
file_path2 = os.path.abspath(os.path.join(os.path.dirname(__file__), "../txtf/output.txt"))

from lab2.utils import read_input_file2, write_output_file

class AVLTree:
    def __init__(self, nodes):
        self.tree = {}
        self.root = None
        for key, left, right in nodes:
            self.tree[key] = (left, right)
            if self.root is None:
                self.root = key

    def insert(self, key):
        if not self.tree:
            self.tree[key] = (0, 0)
            self.root = key
            return

        current = self.root
        parent = None

        while current in self.tree:
            parent = current
            left, right = self.tree.get(current, (0, 0))

            if key < current:
                if left == 0:
                    self.tree[current] = (key, right)
                    break
                current = left
            else:
                if right == 0:
                    self.tree[current] = (left, key)
                    break
                current = right

        self.tree[key] = (0, 0)
        self.balance_tree()

    def get_height(self, node):
        if node == 0 or node not in self.tree:
            return 0
        left, right = self.tree.get(node, (0, 0))
        return 1 + max(self.get_height(left), self.get_height(right))

    def get_balance(self, node):
        if node == 0 or node not in self.tree:
            return 0
        left, right = self.tree.get(node, (0, 0))
        return self.get_height(left) - self.get_height(right)

    def left_rotate(self, root):
        if root not in self.tree:
            return root

        right_child = self.tree[root][1]
        if right_child == 0:
            return root

        right_left, right_right = self.tree.get(right_child, (0, 0))
        self.tree[right_child] = (root, right_right)
        self.tree[root] = (self.tree[root][0], right_left)

        return right_child

    def right_rotate(self, root):
        if root not in self.tree:
            return root

        left_child = self.tree[root][0]
        if left_child == 0:
            return root

        left_left, left_right = self.tree.get(left_child, (0, 0))
        self.tree[left_child] = (left_left, root)
        self.tree[root] = (left_right, self.tree[root][1])

        return left_child

    def balance_tree(self):
        if self.root not in self.tree:
            return

        balance = self.get_balance(self.root)

        if balance > 1:
            if self.get_balance(self.tree[self.root][0]) < 0:
                self.tree[self.root] = (self.left_rotate(self.tree[self.root][0]), self.tree[self.root][1])
            self.root = self.right_rotate(self.root)

        if balance < -1:
            if self.get_balance(self.tree[self.root][1]) > 0:
                self.tree[self.root] = (self.tree[self.root][0], self.right_rotate(self.tree[self.root][1]))
            self.root = self.left_rotate(self.root)

tree_data = read_input_file2(file_path1)
n = int(tree_data[0])
nodes = [list(map(int, tree_data[i + 1].split())) for i in range(n)]
new_key = int(tree_data[n + 1])

avl = AVLTree(nodes)
avl.insert(new_key)

output_data = f"{len(avl.tree)}\n" + "\n".join(f"{key} {left} {right}" for key, (left, right) in sorted(avl.tree.items()))
write_output_file(file_path2, output_data)


