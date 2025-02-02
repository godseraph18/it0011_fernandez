numbers = [1, 3, 5, 6, 7]
repeats = [1, 3, 5, 6, 7]

index = 0
while index < len(numbers):
    spaces = (3 - repeats[index]) // 3
    print(" " * spaces, end="")

    count = 0
    while count < repeats[index]:
        print(numbers[index], end="")
        count += 1
    print()
    index += 1
