# ============================================================
#  💼 RESUME PROJECT — Student Management System
#  Author   : Vidya
#  Language : Python
#  Topics   : Lists, Dictionaries, Loops, f-strings
#
#  About    : B.Tech IT Graduate | Ex-Tech Mahindra
#             Restarting career as Data Analyst
#             Learning Python for Data Analytics
# ============================================================

print("=" * 35)
print("   STUDENT MANAGEMENT SYSTEM")
print("=" * 35)

# Step 1 — Take number of students
n = int(input("Enter number of students: "))

# Step 2 — Take name and marks, store in list of dicts
students = []
for i in range(1, n + 1):
    name  = input(f"Enter name of student {i}: ")
    marks = int(input(f"Enter marks of {name}: "))
    student = {"name": name, "marks": marks}
    students.append(student)

# Step 3 — Print formatted table
print("\n" + "=" * 35)
print(f"{'No':<5} {'Name':<15} {'Marks':<10}")
print("-" * 35)
for i, details in enumerate(students, 1):
    print(f"{i:<5} {details['name']:<15} {details['marks']:<10}")
print("=" * 35)

# Step 4 — Calculate highest, lowest, average, passed count
highest_score = float('-inf')
highest_name  = None
lowest_score  = float('inf')
lowest_name   = None
total         = 0
count         = 0

for details in students:
    m = details['marks']
    total += m

    if m > highest_score:
        highest_score = m
        highest_name  = details['name']

    if m < lowest_score:
        lowest_score = m
        lowest_name  = details['name']

    if m >= 40:
        count += 1

avg = total / len(students)

# Step 5 — Print results
print(f"\n📊 CLASS REPORT")
print(f"Highest Scorer : {highest_name} → {highest_score}")
print(f"Lowest Scorer  : {lowest_name} → {lowest_score}")
print(f"Class Average  : {avg:.2f}")
print(f"Students Passed: {count}/{len(students)}")
print("=" * 35)
