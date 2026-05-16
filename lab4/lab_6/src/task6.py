import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

file_path1 = os.path.abspath(os.path.join(os.path.dirname(__file__), "../txtf/input.txt"))
file_path2 = os.path.abspath(os.path.join(os.path.dirname(__file__), "../txtf/output.txt"))

from lab4.utils import read_input_file2, write_output_file

def z_function(s):
    n = len(s)
    
    if n == 0:
        return []
    
    z = [0] * n
    z[0] = n  
    
    l, r = 0, 0
    for i in range(1, n):
        if i <= r:
            k = i - l
            if s[k] == s[i]:
                z[i] = z[k]
            else:
                l, r = i, i
                while r < n and s[r] == s[r - l]:
                    r += 1
                z[i] = r - l
                r -= 1
        else:
            l, r = i, i
            while r < n and s[r] == s[r - l]:
                r += 1
            z[i] = r - l
            r -= 1

    return z



def process_input_and_output():
    s = read_input_file2(file_path1)
    result = " ".join(map(str, z_function(s)))
    write_output_file(file_path2, result)

process_input_and_output()




