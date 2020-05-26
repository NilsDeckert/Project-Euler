# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?

number = 600851475143

def check_for_prime(num):
    factor = 0
    for q in range(2, num):
        if num%q == 0:
            factor += q
    if factor == 0:
        return True
    else:
        return False

for i in range(1, number+1):
    if number%i == 0 and check_for_prime(i):
        print(i)
