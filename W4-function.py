# function 1 (union)
def unify_lists(a, b):
    return list(set(a).union(set(b)))


# example 1
a1 = [1, 3, 5]
b1 = [1, 2, 3]

print(unify_lists(a1, b1)) # prints union of a1 and b1

# example 2
a2 = [2, 4, 6]
b2 = [2, 4, 6]

print(unify_lists(a2, b2)) # prints union of a2 and b2

# example 3
a3 = [1, 2, 3, 4]
b3 = [4, 5, 6, 7]

print(unify_lists(a3, b3)) # prints union of a3 and b3



# function 2 (modify)
def modify_strings(tuple, string):
    return ''.join(char * n for char, n in zip(tuple, string))

# example 1
tup1 = (1, 2, 3, 4)
str1 = 'alx'

print(modify_strings(tup1, str1)) # prints alex as alleeexxxx

# example 2
tup2 = (1, 2, 1)
str2 = 'pan'

print(modify_strings(tup2, str2)) # prints pan as paan

# example 3
tup3 = (5,)
str3 = 'z'

print(modify_strings(tup3, str3)) # prints z as zzzzz