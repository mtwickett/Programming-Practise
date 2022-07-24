def sum_numbers(*numbers, starting_sum=0):
    sum = starting_sum
    for number in numbers:
        sum += number
    return sum

print(sum_numbers(10, 24, 50.4))
print(sum_numbers(*[10, 20, 10]))
print(sum_numbers(5, 4, 2))
print(sum_numbers(*[10, 10], 5))
