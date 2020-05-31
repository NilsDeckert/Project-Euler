# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?

number = 600851475143

def check_for_prime(num):
    for n in range(2, num):
        if num%n == 0:
            return False
    return True

for n in range(1, number+1):
    if number%n == 0 and check_for_prime(n):
        print(n)
