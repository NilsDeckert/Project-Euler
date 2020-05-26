# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.

palindromes = []

def is_palindrome(num):
    counter = 0
    num_list = [int(i) for i in str(num)]
    for q in range(len(num_list)):
        if not num_list[q] == num_list[len(num_list)-(q+1)]:
            counter += 1
    if counter != 0:
        return False
    else:
        return True

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

for i in range(101, 1000):
    for n in range(101, 1000):
        product = i*n
        if is_palindrome(product):
            palindromes.append(product)

bubble_sort(palindromes)
print("Largest Palindrome: " + str(palindromes[len(palindromes)-1]))
