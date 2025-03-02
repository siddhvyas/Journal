def execute_assembly(code):
    memory = [0] * 100
    accumulator = 0
    pc = 0

    while code[pc][0] != 'HLT':
        instruction = code[pc][0]

        if instruction == 'INP':
            operand = code[pc][1]
            # Access the 'location' from the symbol table dictionary
            memory[symbol_table[operand]['location']] = int(input(f"Enter value for {operand}: "))
        elif instruction == 'OUT':
            operand = code[pc][1]
            # Access the 'location' from the symbol table dictionary
            print(f"Output: {memory[symbol_table[operand]['location']]}")
        elif instruction == 'STO':
            operand = code[pc][1]
            # Access the 'location' from the symbol table dictionary
            memory[symbol_table[operand]['location']] = accumulator
            print(accumulator)
        elif instruction == 'ADD':
            operand = code[pc][1]
            # Access the 'location' from the symbol table dictionary
            accumulator += memory[symbol_table[operand]['location']]
        # Handle other instructions (SUB, MUL, DIV, BRZ, BRN, BRP, BRA) similarly
        pc += 1  # Move to the next instruction

#####

mnemonic_table = {
    "INP": 1,
    "OUT": 2,
    "STO": 3,
    "ADD": 4,
    "HLT": 5,
    "DS": 0
}

symbol_table = {}

assembly_code = [
    ("DS", "D", 1),
    ("DS", "B", 1),
    ("INP", "D"),
    ("ADD", "D"),
    ("STO", "D"),
    ("INP", "B"),
    ("ADD", "B"),
    ("STO", "C"),    # Store the result back into A
    ("OUT", "C"),    # Output the updated value of A
    ("HLT",)
]

# First Pass: Build Symbol Table
location_counter = 0
for instruction in assembly_code:
    if instruction[0] == "DS":
        symbol_table[instruction[1]] = {'defined': 1, 'used': 0, 'location': location_counter}
        location_counter += instruction[2]
    else:
        # Update symbol table for used variables
        if len(instruction) > 1:
            operand = instruction[1]
            if operand not in symbol_table:
                symbol_table[operand] = {'defined': 0, 'used': 1, 'location': 0}  # Initialize with used = 1
            else:
                symbol_table[operand]['used'] = 1  # Mark as used if already in the table

# Second Pass: Execute Code
execute_assembly(assembly_code)
# Print Symbol Table (for demonstration)
print("Symbol Table:")
for symbol, entry in symbol_table.items():
    print(f"{symbol}: {entry}")


#####
# Enter value for D: 1
# 1
# Enter value for B: 5
# 6
# Output: 6
# Symbol Table:
# D: {'defined': 1, 'used': 1, 'location': 0}
# B: {'defined': 1, 'used': 1, 'location': 1}
# C: {'defined': 0, 'used': 1, 'location': 0}
#####