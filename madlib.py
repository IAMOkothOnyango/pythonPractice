'''
sample madlib game
'''
print("Welcome to the Madlib!")

# get user input

adjectiveOne = input("Enter an adjective: ") # string variable for adjective
adjectiveTwo = input("Enter another adjective: ") # string variable for adjective
adjectiveThree = input("Enter one more adjective: ") # string variable for adjective
adjectiveFour = input("Enter a fourth adjective: ") # string variable for adjective
adjectiveFive = input("Enter a fifth adjective: ") # string variable for adjective

# print out the madlib with the user input using the f-string method

madlib = f"Computer programming is so {adjectiveOne}! It makes me so {adjectiveTwo} all the time because I love to {adjectiveThree}. Stay hydrated and {adjectiveFour} like you are {adjectiveFive}!"

print(madlib) # print out the madlib

# print out the madlib with the user input using the .format method

madlib = "Computer programming is so {}! It makes me so {} all the time because I love to {}. Stay hydrated and {} like you are {}!".format(adjectiveOne, adjectiveTwo, adjectiveThree, adjectiveFour, adjectiveFive)

print(madlib) # print out the madlib

# print out the madlib with the user input using the + operator

madlib = "Computer programming is so " + adjectiveOne + "! It makes me so " + adjectiveTwo + " all the time because I love to " + adjectiveThree + ". Stay hydrated and " + adjectiveFour + " like you are " + adjectiveFive + "!"

print(madlib) # print out the madlib

# print out the madlib with the user input using the % operator

madlib = "Computer programming is so %s! It makes me so %s all the time because I love to %s. Stay hydrated and %s like you are %s!" % (adjectiveOne, adjectiveTwo, adjectiveThree, adjectiveFour, adjectiveFive)

print(madlib) # print out the madlib

# print out the madlib with the user input using the join method

madlib = " ".join(["Computer programming is so", adjectiveOne + "!", "It makes me so", adjectiveTwo + " all the time because I love to", adjectiveThree + ".", "Stay hydrated and", adjectiveFour + " like you are", adjectiveFive + "!"])

print(madlib) # print out the madlib