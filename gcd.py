# Given an array of n positive integers,
# find the GCD of all the array elements.

'''
Docstring for gcd
Example :

Input: n = 3, arr = [1, 2, 3]
Output: 1
Explanation: GCD of 1,2,3 is 1.
'''

def gcd(n):
    for i in range(1,n):
        if(n%i==0):
            gcd=i
        return gcd

print("Hello, Shrujan!")
print("\n")