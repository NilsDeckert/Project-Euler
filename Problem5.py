# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

n = 232000000

def evenly_divisible(num, top):
    check = 0
    for i in range(2, top+1):
        if not num%i == 0:
            return False
    return True


while True:
    if evenly_divisible(n, 20):
        print("Found something!")
        print(n)
        break
    else:
        print(n)
        n += 1
