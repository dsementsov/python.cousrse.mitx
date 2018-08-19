
# s = "itkedulgrouawlnejkmxml"

# longest_substring = ""
# for start in range(len(s)):
#     end = 0
#     current_substring = ""
#     while True:
#         if not current_substring or s[start+end] >= current_substring[-1]:
#             current_substring += s[start+end]
#         else:
#             break
#         end += 1
#         if (start + end) >= len(s):
#             break
#     if len(current_substring) > len(longest_substring):
#         longest_substring = current_substring
# print ("Longest substring in alphabetical order is:", longest_substring)



# longest_substring = ""
# #'abcdefghijklmnopqrstuvwxyz'
# for i in range(len(s)):
#     current_substring = ""
#     for char in s[i:]:
#         if not current_substring or current_substring[-1] <= char:
#             current_substring += char
#         if len(current_substring) >= len(longest_substring):
#             longest_substring = current_substring
# print ("Longest substring in alphabetical order is:", longest_substring)


# def satisfiesF(L):
#     """
#     Assumes L is a list of strings
#     Assume function f is already defined for you and it maps a string to a Boolean
#     Mutates L such that it contains all of the strings, s, originally in L such
#             that f(s) returns True, and no other elements. Remaining elements in L
#             should be in the same order.
#     Returns the length of L after mutation
#     """
#     # Your function implementation here
#     for element in L.copy():
#         if not f(element):
#             L.remove(element)
#     return len(L)
# #run_satisfiesF(L, satisfiesF)


# def f(s):
#     return 'a' in s or  'b' in s or 'c' in s
      
# L = ['a', 'b', 'a', 's', 'f', 'n', 'b', 'cat']
# print (satisfiesF(L))
# print (L)


# Prime generator

def genPrimes():
    generated_primes = []
    next_prime = 2
    def isPrime(x):
        for prime in generated_primes:
            if x % prime == 0:
                return False
        return True
    while True:
        if isPrime(next_prime):
            generated_primes.append(next_prime)
            yield next_prime
            next_prime += 1
        else:
            next_prime += 1

primegenerator = genPrimes()
for i in range(100):
    print(primegenerator.__next__())