students = {}

n = int(input("How many students? "))

for i in range(n):
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    students[name] = marks

print("\nStudent Records:")
for name, marks in students.items():
    print(name, ":", marks)

print("\nTopper:", max(students, key=students.get))
print("Lowest scorer:", min(students, key=students.get))
