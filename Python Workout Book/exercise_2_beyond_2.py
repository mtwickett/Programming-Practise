def average_numbers(*numbers):
    sum = 0
    for number in numbers:
        sum += number
    return sum / len(numbers)

print(average_numbers(25, 55, 3, 4, 8))
print(average_numbers(40, 60))
