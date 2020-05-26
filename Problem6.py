# The sum of the squares of the first ten natural numbers is, (1^2)+(2^2)+...+(10^2) = 385
#
# The square of the sum of the first ten natural numbers is, (1+2+...+10)^2 = 55^2 = 3025
#
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025−385=2640
#
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def sum_of_squares(num):
    sum_of_squares = 0
    for n in range(num + 1):
        sum_of_squares += n*n
    return sum_of_squares

def square_of_sum(num):
    sum = 0
    for n in range(num + 1):
        sum += n
    return (sum*sum)

print(square_of_sum(100) - sum_of_squares(100))
