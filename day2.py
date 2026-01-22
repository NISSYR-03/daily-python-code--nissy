num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

sum = num1 + num2
diff = num1 - num2
print("Sum =", sum)
print("Difference =", diff)
prod = num1 * num2
if num2 != 0:
    quot = num1 / num2
    print("Quotient =", quot)
else:
    print("Cannot divide by zero")
print("Product =", prod)
