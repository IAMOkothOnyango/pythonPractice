youtuber = " Okoth Onyango"  # string variable

# Different methods of string concatenation
print("Subscribe to " + youtuber)  # using the + operator
print("Subscribe to {}".format(youtuber))  # using the format method
print(f"Subscribe to {youtuber}")  # using f-string

'''
Concatenation using the + operator is the most common way of concatenating strings
'''

a = "Python "  # string variable
b = "is "  # string variable
c = "cool"  # string variable

print(a + b + c)  # using the + operator

'''
Concatenation using the * operator
Used to repeat a string a given number of times for a single output
'''
a = "Python "  # string variable

print(a * 3)  # using the * operator

'''
Concatenation using the join method
Most flexible method of concatenating strings
'''

a = "Python"  # string variable
b = "is"  # string variable
c = "cool"  # string variable

print(" ".join([a, b, c]))  # using the join method

'''
Concatenation using the % operator
'''

a = "Python"  # string variable
b = "is"  # string variable
c = "cool"  # string variable

print("%s %s %s" % (a, b, c))  # using the % operator