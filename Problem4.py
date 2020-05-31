# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.

largest_palindrome = 0

def is_palindrome(num):
    num_list = [int(i) for i in str(num)]
    for q in range(len(num_list)):
        if not num_list[q] == num_list[len(num_list)-(q+1)]:
            return False
    return True

for i in range(101, 1000):
    for n in range(101, 1000):
        if is_palindrome(i*n) and (i*n) > largest_palindrome:
            largest_palindrome = i*n

print(largest_palindrome)
