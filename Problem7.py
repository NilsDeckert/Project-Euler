# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
# What is the 10001st prime number?

counter1 = 2
counter2 = 0

def check_for_prime(num):
    factor = 0
    for q in range(2, num):
        if num%q == 0:
            factor += q
    if factor == 0:
        return True
    else:
        return False

while True:
    if check_for_prime(counter1):
        counter2 += 1
        print("{}: {}".format(counter2, counter1))
    if counter2 == 10001:
        print("Stop")
        break
    counter1 += 1
