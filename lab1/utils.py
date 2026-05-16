def read_input_file(file_path):
    with open(file_path, 'r') as file:
        n, W = map(int, file.readline().split())
        items = []
        for _ in range(n):
            value, weight = map(int, file.readline().split())
            items.append((value, weight))
    return n, W, items

def read_input_filetask13(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    n = int(lines[0].strip())  
    values = list(map(int, lines[1].strip().split()))  
    return n, values

def read_input_filetask15(file_path):
    with open(file_path, 'r') as f:
        return f.read().strip() 
    
def read_input_file3(file_path):
    with open(file_path, 'r') as file:
        return file.read().splitlines()

def write_output_file(file_path, max_value):
    with open(file_path, 'w') as file:
        file.write(f"{max_value:.4f}") 

def write_output_file2(file_path, data):
    with open(file_path, 'w') as file:
        if isinstance(data, (int, float)):  
            file.write(f"{data:.4f}")  
        elif isinstance(data, list):  
            file.writelines(data)  
        else:
            file.write(str(data))

def write_output_file3(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)