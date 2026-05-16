import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

file_path1 = os.path.abspath(os.path.join(os.path.dirname(__file__), "../txtf/input.txt"))
file_path2 = os.path.abspath(os.path.join(os.path.dirname(__file__), "../txtf/output.txt"))

from lab2.utils import read_input_file2, write_output_file

class BST:
    def __init__(self, nodes):
        self.tree = {}
        self.node_count = len(nodes)
        
        for key, left, right in nodes:
            self.tree[key] = (left, right)

    def count_subtree(self, node):
        if node == 0:
            return 0
        left, right = self.tree.get(node, (0, 0))
        return 1 + self.count_subtree(left) + self.count_subtree(right)

    def delete_subtree(self, key):
        if key not in self.tree:
            return self.node_count

        nodes_to_remove = self.count_subtree(key)
        self.node_count -= nodes_to_remove
        del self.tree[key]

        for parent in self.tree:
            left, right = self.tree[parent]
            if left == key:
                self.tree[parent] = (0, right)
            elif right == key:
                self.tree[parent] = (left, 0)

        return self.node_count

tree_data = read_input_file2(file_path1)
n = int(tree_data[0])
nodes = [list(map(int, tree_data[i + 1].split())) for i in range(n)]
m = int(tree_data[n + 1])
removals = list(map(int, tree_data[n + 2].split()))

bst = BST(nodes)
results = [str(bst.delete_subtree(key)) for key in removals]

write_output_file(file_path2, "\n".join(results))
