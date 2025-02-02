input_digits = input("Enter a string with digits: ")
sum_of_digits = 0

for char in input_digits:
    if char.isdigit():
        sum_of_digits += int(char)

print(f"Sum of digits: {sum_of_digits}")