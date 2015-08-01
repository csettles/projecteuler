# Find the difference between the sum of the squares of the
# first one hundred natural numbers and the square of the sum.

ls = list(range(1, 101))


def sum_of_squares(n):
    sum1 = 0
    for i in n:
        i **= 2
        sum1 += i
    return sum1


def square_of_sum(n):
    sum2 = 0
    for i in n:
        sum2 += i
    return sum2**2

print(square_of_sum(ls)-sum_of_squares(ls))
