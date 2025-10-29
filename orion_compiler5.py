import os

def orion_to_python(line):
    line = line.strip()
    if line.startswith("print:"):
        content = line[6:].strip()
        # FIX: Add quotes if they're missing
        if not (content.startswith('"') and content.endswith('"')):
            content = f'"{content}"'
        return f"print({content})"
    elif line.startswith("let "):
        return line[4:]
    else:
        return line

print("ORION COMPILER - FIXED VERSION!")
print("=" * 50)

filename = "my_program.orion"

if not os.path.exists(filename):
    print(f"{filename} not found!")
else:
    print(f"COMPILING: {filename}")
    print("=" * 30)
    
    with open(filename, 'r') as file:
        orion_lines = file.readlines()
    
    python_lines = []
    for orion_line in orion_lines:
        python_line = orion_to_python(orion_line)
        python_lines.append(python_line)
        print(f"Orion: {orion_line.strip()} -> Python: {python_line}")
    
    print("=" * 30)
    python_code = '\n'.join(python_lines)
    exec(python_code)
    
    print("=" * 30)
    print("SUCCESS! Compiler found and ran your file!")