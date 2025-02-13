def is_palindrome(n):
    return str(n) == str(n)[::-1]

try:
    with open("Technical_Midterm_Exam\\numbers.txt", "r") as file:
        line_number = 1
        for line in file:
            line = line.strip()
            if line:
                try:
                    numbers = list(map(int, line.split(",")))  
                    total_sum = sum(numbers)
                    status = "Palindrome" if is_palindrome(total_sum) else "Not a Palindrome"
                    print(f"Line {line_number}: {line} (sum {total_sum}) - {status}")
                    line_number += 1
                except ValueError:
                    print(f"Line {line_number}: Error - Invalid number format.")
except FileNotFoundError:
    print("Failed to open numbers.txt")
