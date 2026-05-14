# ============================================================
#  💼 RESUME PROJECT — Smart Calculator
#  Author   : Vidya
#  Language : Python
#  Topics   : Loops, Conditionals, Error Handling, Lists
#
#  About    : B.Tech IT Graduate | Ex-Tech Mahindra
#             Restarting career as Data Analyst
#             Learning Python for Data Analytics
# ============================================================
 
print("=" * 40)
print("         SMART CALCULATOR")
print("=" * 40)
 
history = []
is_end = False
 
while not is_end:
    operation = ""
    c = None
 
    print("\nOperators: +  -  *  /  %  ** (power)  // (floor div)")
    op_value = input("Enter operator: ")
    n1 = int(input("Enter Number1: "))
    n2 = int(input("Enter Number2: "))
 
    if op_value == "+":
        c = n1 + n2
        operation = "addition"
    elif op_value == "-":
        c = n1 - n2
        operation = "subtraction"
    elif op_value == "*":
        c = n1 * n2
        operation = "multiplication"
    elif op_value == "/":
        if n2 == 0:
            print("⚠️  Error!! Cannot divide by zero!!")
        else:
            c = n1 / n2
            operation = "division"
    elif op_value == "%":
        c = n1 % n2
        operation = "modulo"
    elif op_value == "**":
        c = n1 ** n2
        operation = "power"
    elif op_value == "//":
        c = n1 // n2
        operation = "floor division"
    else:
        print("⚠️  Invalid Operation!!")
        is_end = True
 
    if operation != "":
        print(f"✅ Result: {n1} {op_value} {n2} = {c}")
        history.append(f"{n1} {op_value} {n2} = {c}  ({operation})")
 
    if not is_end:
        another = input("\nDo you want another calculation? (yes/no): ").lower()
        if another == "yes":
            is_end = False
        else:
            is_end = True
 
print("\n" + "=" * 40)
print("         📋 CALCULATION HISTORY")
print("=" * 40)
for i, h in enumerate(history, 1):
    print(f"{i}. {h}")
print("=" * 40)
print(f"Total Calculations: {len(history)}")
