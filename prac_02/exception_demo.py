"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
When entering that isn't an integer, like a letter, space, or float.
2. When will a ZeroDivisionError occur?
When a zero is entered for the denominator.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Man, I'm just an English student.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")