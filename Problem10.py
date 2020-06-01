# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.

sum = 0

def check_for_prime(num):
    for n in range(2, num):
        if num%n == 0:
            return False
    return True

for n in range(2, 2000001):
    if check_for_prime(n):
        sum += n
        print(n)

print(sum)

# [Finished in 18374.383s]
