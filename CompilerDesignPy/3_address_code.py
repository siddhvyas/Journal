import re
import ast

def generate_TAC(expression):
    temp_count = 1
    tac_code = []

    def _generate_TAC_recursive(node):
        nonlocal temp_count, tac_code

        if isinstance(node, ast.BinOp):
            left_temp = _generate_TAC_recursive(node.left)
            right_temp = _generate_TAC_recursive(node.right)
            temp_var = f't{temp_count}'
            op_str = {
                ast.Add: '+',
                ast.Sub: '-',
                ast.Mult: '*',
                ast.Div: '/',
            }.get(type(node.op), str(node.op))
            tac_code.append(f'{temp_var} = {left_temp} {op_str} {right_temp}')
            temp_count += 1
            return temp_var
        elif isinstance(node, ast.UnaryOp):
            operand_temp = _generate_TAC_recursive(node.operand)
            temp_var = f't{temp_count}'
            tac_code.append(f'{temp_var} = {node.op} {operand_temp}')
            temp_count += 1
            return temp_var
        elif isinstance(node, ast.Name):
            return node.id
        elif isinstance(node, ast.Constant):
            return node.value

    expression = expression.strip()
    if expression.startswith('(') and expression.endswith(')'):
        expression = expression[1:-1]

    parsed_expression = ast.parse(expression).body[0]

    if isinstance(parsed_expression, ast.Assign):
        target_var = parsed_expression.targets[0].id
        result_temp = _generate_TAC_recursive(parsed_expression.value)
        tac_code.append(f'{target_var} = {result_temp}')
    else:
        result_temp = _generate_TAC_recursive(parsed_expression)
        tac_code.append(f'Result = {result_temp}')
    #print(d)
    return tac_code


expression = input("Enter a universal expression (d=a+b-c+d*100-500*2)(d=1+2-5+6*100-500*2): ")
tac_code = generate_TAC(expression)
for line in tac_code:
    print(line)

######
# Enter a universal expression (d=a+b-c+d*100-500*2)(d=1+2-5+6*100-500*2): d=a+b-c+d*100-500*2
# t1 = a + b
# t2 = t1 - c
# t3 = d * 100
# t4 = t2 + t3
# t5 = 500 * 2
# t6 = t4 - t5
# d = t6
######


# prompt: print the temp varables from the above code in tabular format will be (1-termp 2-operand 3-varable 4-varable) give full code only temp varable

import re
import ast

def generate_TAC(expression):
    temp_count = 1
    tac_code = []
    temp_variables = []

    def _generate_TAC_recursive(node):
        nonlocal temp_count, tac_code, temp_variables

        if isinstance(node, ast.BinOp):
            left_temp = _generate_TAC_recursive(node.left)
            right_temp = _generate_TAC_recursive(node.right)
            temp_var = f't{temp_count}'
            op_str = {
                ast.Add: '+',
                ast.Sub: '-',
                ast.Mult: '*',
                ast.Div: '/',
            }.get(type(node.op), str(node.op))
            tac_code.append(f'{temp_var} = {left_temp} {op_str} {right_temp}')
            temp_variables.append((temp_var, left_temp, right_temp, op_str))
            temp_count += 1
            return temp_var
        elif isinstance(node, ast.UnaryOp):
            operand_temp = _generate_TAC_recursive(node.operand)
            temp_var = f't{temp_count}'
            tac_code.append(f'{temp_var} = {node.op} {operand_temp}')
            temp_variables.append((temp_var, operand_temp, None, str(node.op)))
            temp_count += 1
            return temp_var
        elif isinstance(node, ast.Name):
            return node.id
        elif isinstance(node, ast.Constant):
            return node.value

    expression = expression.strip()
    if expression.startswith('(') and expression.endswith(')'):
        expression = expression[1:-1]

    parsed_expression = ast.parse(expression).body[0]

    if isinstance(parsed_expression, ast.Assign):
        target_var = parsed_expression.targets[0].id
        result_temp = _generate_TAC_recursive(parsed_expression.value)
        tac_code.append(f'{target_var} = {result_temp}')
    else:
        result_temp = _generate_TAC_recursive(parsed_expression)
        tac_code.append(f'Result = {result_temp}')

    return tac_code, temp_variables


expression = input("Enter a universal expression (d=a+b-c+d*100-500*2)(d=1+2-5+6*100-500*2): ")
tac_code, temp_variables = generate_TAC(expression)

# for line in tac_code:
#     print(line)

print("\nTemporary Variables Table:")
if temp_variables:
    print("Temp\tOperand1\tOperand2\tOperator")
    for var, op1, op2, op in temp_variables:
        print(f"{var}\t{op1}\t\t{op2}\t\t{op}")

######
# Enter a universal expression (d=a+b-c+d*100-500*2)(d=1+2-5+6*100-500*2): d=a+b-c+d*100-500*2

# Temporary Variables Table:
# Temp	Operand1	Operand2	Operator
# t1	a		b		+
# t2	t1		c		-
# t3	d		100		*
# t4	t2		t3		+
# t5	500		2		*
# t6	t4		t5		-
######


# prompt: print the temp varables from the above code in tabular format will be (1-termp 2-operand 3-varable 4-varable) give full code only temp varable

import re
import ast

def generate_TAC(expression):
    temp_count = 1
    tac_code = []
    temp_variables = []

    def _generate_TAC_recursive(node):
        nonlocal temp_count, tac_code, temp_variables

        if isinstance(node, ast.BinOp):
            left_temp = _generate_TAC_recursive(node.left)
            right_temp = _generate_TAC_recursive(node.right)
            temp_var = f't{temp_count}'
            op_str = {
                ast.Add: '+',
                ast.Sub: '-',
                ast.Mult: '*',
                ast.Div: '/',
            }.get(type(node.op), str(node.op))
            tac_code.append(f'{temp_var} = {left_temp} {op_str} {right_temp}')
            temp_variables.append((temp_var, left_temp, right_temp, op_str))
            temp_count += 1
            return temp_var
        elif isinstance(node, ast.UnaryOp):
            operand_temp = _generate_TAC_recursive(node.operand)
            temp_var = f't{temp_count}'
            tac_code.append(f'{temp_var} = {node.op} {operand_temp}')
            temp_variables.append((temp_var, operand_temp, None, str(node.op)))
            temp_count += 1
            return temp_var
        elif isinstance(node, ast.Name):
            return node.id
        elif isinstance(node, ast.Constant):
            return node.value

    expression = expression.strip()
    if expression.startswith('(') and expression.endswith(')'):
        expression = expression[1:-1]

    parsed_expression = ast.parse(expression).body[0]

    if isinstance(parsed_expression, ast.Assign):
        target_var = parsed_expression.targets[0].id
        result_temp = _generate_TAC_recursive(parsed_expression.value)
        tac_code.append(f'{target_var} = {result_temp}')
    else:
        result_temp = _generate_TAC_recursive(parsed_expression)
        tac_code.append(f'Result = {result_temp}')

    return tac_code, temp_variables


expression = input("Enter a universal expression (d=a+b-c+d*100-500*2)(d=1+2-5+6*100-500*2): ")
tac_code, temp_variables = generate_TAC(expression)

# for line in tac_code:
#     print(line)

print("\nTemporary Variables Table:")
if temp_variables:
    print("Temp\tOperand1\tOperand2\tOperator")
    for var, op1, op2, op in temp_variables:
        print(f"\t{op1}\t\t{op2}\t\t{op}")

######
# Enter a universal expression (d=a+b-c+d*100-500*2)(d=1+2-5+6*100-500*2): d=a+b-c+d*100-500*2

# Temporary Variables Table:
# Temp	Operand1	Operand2	Operator
# 	a		b		+
# 	t1		c		-
# 	d		100		*
# 	t2		t3		+
# 	500		2		*
# 	t4		t5		-
######