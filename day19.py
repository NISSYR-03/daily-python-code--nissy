try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    result = a / b
    print("Result:", result)

except ZeroDivisionError:
    print("Cannot divide by zero ")

except ValueError:
    print("Please enter only numbers ")

else:
    print("Calculation successful ")

finally:
    print("Program ended.")
