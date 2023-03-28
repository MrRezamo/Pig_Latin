# First we have user input
user = input("Please Enter your word : ")
# Creat a list of vowel letter
first_list = ["a", "e", "i", "o", "u"]
# if the Users input starts by vowel letter
if user[0] in first_list:
    # Add on the end "way"
    user += "way"
    print(user)
# if the Users input doesnt start by vowel letter
elif user[0] not in first_list:
    # take first index and put it on the end of user index
    user = user[1:]+user[0]
    # Add on the end "ay"
    user += "ay"
    print(user)
