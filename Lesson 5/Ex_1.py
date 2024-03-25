"""
Using the vscode Debugger Demo

- Create a breakpoint by clicking on the left side of the line numbers. A red dot will show up
- Breakpoints can be created anytime, also while debugging
- Once you have a breakpoint, run the code with the green Play button or press F5
- Watch the Variables on the left part
- Continue (F5): continue with the program until the next breakpoint or until the program finishes
- Step over (F10): continue with the next line even if it has no breakpoint
- Restart: restart the debugging from the beginning
- Stop: stop the debugging

Debug this code to understand what it does and find out what the mysterious variables are!
Hint: what is the purpose of line 21?
"""

last_names = ["Schwarz", "Braun", "Lehmann", "Weiß", "Schneider", "Hell"]
last_names_length = {}

for name in last_names:
    name_capital_letters = name.upper()
    name_length = len(name_capital_letters)
    last_names_length[name] = name_length

mysterious_variable = 0
mysterious_variable_2 = ""
last_names.sort()
for name in last_names:
    name_length = last_names_length[name]
    print(f"{name}: {name_length}")
    if name_length > mysterious_variable:
        mysterious_variable = name_length
        mysterious_variable_2 = name

print("Final mystery: Winner is...")
print(f"{mysterious_variable_2}: {mysterious_variable}")
Collapse