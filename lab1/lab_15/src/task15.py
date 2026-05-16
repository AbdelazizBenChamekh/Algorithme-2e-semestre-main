import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

file_path1 = os.path.abspath(os.path.join(os.path.dirname(__file__), "../txtf/input.txt"))
file_path2 = os.path.abspath(os.path.join(os.path.dirname(__file__), "../txtf/output.txt"))

from lab1.utils import read_input_filetask15,  write_output_file2 


def remove_invalid_brackets(s):
    stack = []
    indices_to_remove = set()

    for i, char in enumerate(s):
        if char in "({[":
            stack.append((char, i))
        elif char in ")}]":
            if stack and ((stack[-1][0] == "(" and char == ")") or
                          (stack[-1][0] == "[" and char == "]") or
                          (stack[-1][0] == "{" and char == "}")):
                stack.pop()
            else:
                indices_to_remove.add(i)

    indices_to_remove.update({index for _, index in stack})

    return "".join([s[i] for i in range(len(s)) if i not in indices_to_remove])

text = read_input_filetask15(file_path1)
result = remove_invalid_brackets(text)
write_output_file2(file_path2, result)
