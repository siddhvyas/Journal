import re

symbol_table = []
symbol_count = 0

def add_symbol(name, data_type, defined, used, mem_loc, value):
    global symbol_count
    symbol_count += 1
    symbol_table.append({
        "ID": symbol_count,
        "Name": name,
        "DataType": data_type,
        "Used": used,
        "Defined": defined,
        "MemLoc": mem_loc,
        "Value": value
    })

def display_symbol_table():
    print(f"\n{'ID':<5} {'Name':<10} {'DataType':<10} {'Used':<5} {'Defined':<8} {'MemLoc':<8} {'Value':<10}")
    for entry in symbol_table:
        print(f"{entry['ID']:<5} {entry['Name']:<10} {entry['DataType']:<10} {entry['Used']:<5} "
              f"{entry['Defined']:<8} {entry['MemLoc']:<8} {entry['Value']:<10}")

def process_code(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    data_type_patterns = ['int', 'float', 'char', 'double']
    variable_pattern = re.compile(r'\b([a-zA-Z_][a-zA-Z0-9_]*)\b')

    for line_num, line in enumerate(lines, start=1):
        tokens = line.split()
        for token in tokens:

            if token in data_type_patterns:

                next_token = tokens[tokens.index(token) + 1]
                if next_token.isidentifier():
                    add_symbol(next_token, token, defined=1, used=0, mem_loc=line_num, value='N/A')

            elif variable_pattern.match(token):
                for symbol in symbol_table:
                    if symbol["Name"] == token:
                        symbol["Used"] = 1
                        break
                else:
                    add_symbol(token, "Unknown", defined=0, used=1, mem_loc=line_num, value='N/A')

file_path = 'test.txt'
process_code(file_path)
display_symbol_table()


#####
# ID    Name       DataType   Used  Defined  MemLoc   Value     
# 1     a          int        1     1        1        N/A       
# 2     pi         float      1     1        2        N/A       
# 3     ch         char       1     1        3        N/A       
# 4     b          Unknown    1     0        6        N/A       
# 5     c          Unknown    1     0        7        N/A       
#####