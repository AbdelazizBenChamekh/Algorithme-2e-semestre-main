import sys
import os
import heapq


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

file_path1 = os.path.abspath(os.path.join(os.path.dirname(__file__), "../txtf/input.txt"))
file_path2 = os.path.abspath(os.path.join(os.path.dirname(__file__), "../txtf/output.txt"))

from lab2.utils import read_input_file2, write_output_file

class KthMax:
    def __init__(self):
        self.data = []  
        self.lookup = set()  

    def add(self, x):
        heapq.heappush(self.data, -x)
        self.lookup.add(x)

    def remove(self, x):
        if x in self.lookup:
            self.lookup.remove(x)  

    def kth_max(self, k):
        temp = []
        result = None

        while len(temp) < k and self.data:
            top = -heapq.heappop(self.data)
            if top in self.lookup:
                temp.append(top)
        
        if len(temp) == k:
            result = temp[-1]

        for val in temp:
            heapq.heappush(self.data, -val)

        return result

kth_max_ds = KthMax()
queries = read_input_file2(file_path1)

n = int(queries[0])
results = []

for i in range(1, n + 1):
    command = queries[i].split()
    op = int(command[0])
    value = int(command[1])

    if op == 1:
        kth_max_ds.add(value)
    elif op == -1:
        kth_max_ds.remove(value)
    elif op == 0:
        results.append(str(kth_max_ds.kth_max(value)))

write_output_file(file_path2, "\n".join(results))



