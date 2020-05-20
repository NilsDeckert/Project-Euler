# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.

Palindromes = []

def IsPalindrome(num):
    counter = 0
    num_list = [int(i) for i in str(num)]
    for q in range(len(num_list)):
        if not num_list[q] == num_list[len(num_list)-(q+1)]:
            counter += 1
    if counter != 0:
        return False
    else:
        return True

def BubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

for i in range(101, 1000):
    for n in range(101, 1000):
        product = i*n
        #print("{} * {} = {}".format(i, n, product))
        if IsPalindrome(product):
            #print("Found Palindrome: {}".format(product))
            Palindromes.append(product)

BubbleSort(Palindromes)
#print(Palindromes)
print("Largest Palindrome: " + str(Palindromes[len(Palindromes)-1]))
