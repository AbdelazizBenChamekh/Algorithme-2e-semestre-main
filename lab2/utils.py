import os

def read_input_file(file_path):

    with open(file_path, 'r') as file:
        lines = file.readlines()

    n = int(lines[0].strip())
    tree = []

    for i in range(1, n + 1):
        parts = list(map(int, lines[i].strip().split()))
        tree.append(parts)

    return tree

def read_input_file2(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    with open(file_path, 'r') as file:
        lines = file.read().strip().split("\n")

    return lines

def write_output_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)
