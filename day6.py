numbers = []

n = int(input("How many numbers do you want to enter? "))

for i in range(n):
    num = int(input("Enter number: "))
    numbers.append(num)

print("Numbers:", numbers)
print("Largest number:", max(numbers))
print("Smallest number:", min(numbers))
