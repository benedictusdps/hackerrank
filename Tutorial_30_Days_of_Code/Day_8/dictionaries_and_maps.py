# Given n names and phone numbers, assemble a phone book that maps friends' names to their respective phone numbers. 
# You will then be given an unknown number of names to query your phone book for. 
# For each  queried, print the associated entry from your phone book on a new line in the form name=phoneNumber; 
# if an entry for  is not found, print Not found instead.

# Number of key-value pairs
n = int(input())

# Loop through the number of pairs, appending the input into the names list
names = [input().split() for i in range(n)]

# Loop through the list, inserting the key and val into the phone book dictionary
phone_book = {key: val for key, val in names}

# While there is still name input, check in the phonebook if the name existed
# If it exist, print out the name and number
while True:
    try:
        name = input()
        if name in phone_book:
            print("%s=%s" % (name, phone_book[name]))
        else:
            print("Not found")
    except:
        break