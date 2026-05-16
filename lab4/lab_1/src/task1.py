import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

file_path1 = os.path.abspath(os.path.join(os.path.dirname(__file__), "../txtf/input.txt"))
file_path2 = os.path.abspath(os.path.join(os.path.dirname(__file__), "../txtf/output.txt"))

from lab4.utils import read_input_file, write_output_file

def naive_substring_search(p, t):
    n = len(t)
    m = len(p)
    matches = []
    
   
    for i in range(n - m + 1):
        if t[i:i + m] == p:
            matches.append(i + 1)  
    
    return len(matches), matches

def process_input_and_output():
    p, t = read_input_file(file_path1)
    
    count, matches = naive_substring_search(p, t)
    
    result = f"{count}\n"
    if matches:
        result += " ".join(map(str, matches))
    
    write_output_file(file_path2, result)

process_input_and_output()

