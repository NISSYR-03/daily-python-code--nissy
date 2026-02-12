from functools import reduce

numbers = [1, 2, 3, 4, 5, 6]

evens = list(filter(lambda x: x % 2 == 0, numbers))
total = reduce(lambda a, b: a + b, numbers)

print("Numbers:", numbers)
print("Even numbers:", evens)
print("Sum of numbers:", total)
