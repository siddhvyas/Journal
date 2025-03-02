import re


def check_if_else_statement(filepath):
    try:
        with open(filepath, 'r') as file:
            text = file.read()
            #pattern = r"if\s*\(dhawal\)\s*{[\s\S]*?siddh;[\s\S]*?faiyaz;[\s\S]*?}\s*else\s*{[\s\S]*?suraj;[\s\S]*?mitesh;[\s\S]*?}"
            #pattern = r"switch\s*\(.*?\)\s*{[\s\S]*?case\s+.*?:[\s\S]*?break;[\s\S]*?case\s+.*?:[\s\S]*?break;[\s\S]*?default:[\s\S]*?}"
            pattern = r"if\s*\(.*?\)\s*{(.*?)}\s*else\s*{(.*?)}"
            #pattern = r"if\s*\(\)\s*{[\s\S]*?}\s*else\s*{[\s\S]*?}"
            #pattern = r"if\s*\(([a-zA-Z0-9!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>\/?]*)\)\s*{(.*?)}\s*else\s*{(.*?)}"
            match = re.search(pattern, text, re.DOTALL)
            if match:
                return True
            else:
                return False
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
        return False
filepath = "/content/test.txt"
if check_if_else_statement(filepath):
    print(f"The file {filepath} contains 'if {{}} else {{}}' statements.")
else:
    print(f"The file {filepath} does not contain 'if {{}} else {{}}' statements.")

#####
# Error: File not found at /content/test.txt
# The file /content/test.txt does not contain 'if {} else {}' statements.
#####



def check_if_else_statement(filepath):
    try:
        with open(filepath, 'r') as file:
            text = file.read()
            pattern = r"if\s*\([\s\S]*?\)\s*{[\s\S]*?}\s*else\s*{[\s\S]*?}"
            match = re.search(pattern, text)
            if match:
                return True
            else:
                return False
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
        return False
filepath = "/content/test.txt"
if check_if_else_statement(filepath):
    print(f"The file {filepath} contains 'if {{}} else {{}}' statements.")
else:
    print(f"The file {filepath} does not contain 'if {{}} else {{}}' statements.")

#####
# Error: File not found at /content/test.txt
# The file /content/test.txt does not contain 'if {} else {}' statements.
#####


def check_loops(filepath):
    try:
        with open(filepath, 'r') as file:
            text = file.read()
            # Patterns for loop types
            for_pattern = r"for\s+\w+\s+in\s+.+:"
            while_pattern = r"while\s+.+:"
            do_while_pattern = r"do\s*\{\s*(.*\s*)+?\}\s*while\s*\(\s*\w+\s*<\s*\d+\s*\)\s*;"


            # Check for each loop type
            has_for = re.search(for_pattern, text) is not None
            has_while = re.search(while_pattern, text) is not None
            has_do_while = re.search(do_while_pattern, text, re.MULTILINE) is not None

            return has_for, has_while, has_do_while

    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
        return False, False, False
# Example usage

filepath = r"test.txt"
has_for, has_while, has_do_while = check_loops(filepath)

if has_for:
    print("The file contains 'for' loops.")
if has_while:
    print("The file contains 'while' loops.")
if has_do_while:
    print("The file contains 'do-while' loops.")
if not (has_for or has_while or has_do_while):
    print("The file does not contain any of the specified loop types.")

#####
# The file contains 'for' loops.
# The file contains 'while' loops.
# The file contains 'do-while' loops.
#####