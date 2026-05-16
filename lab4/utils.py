def read_input_file(file_path):
    with open(file_path, "r") as file:
        p = file.readline().strip()  
        t = file.readline().strip()  
    return p, t

def read_input_file2(file_path):
    with open(file_path, "r") as file:
        s = file.readline().strip()  
    return s

def write_output_file(file_path, result):
    with open(file_path, "w") as file:
        file.write(result)
