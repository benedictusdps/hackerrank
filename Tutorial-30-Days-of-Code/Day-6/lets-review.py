# Given a string, S, of length N that is indexed from 0 to N - 1, print its even-indexed and odd-indexed 
# characters as 2 space-separated strings on a single line

def loopstring(string):
    # Declare the result variable
    result_even = ""
    result_odd = ""

    # Loop through the string
    for i in range(len(string)):
        # If it's an even index then add to the even result variable
        if i % 2 == 0:
            result_even += string[i]
        # Else, it's an odd index so add to the odd result variable
        else:
            result_odd += string[i]
    # Print both result variables separated by a comma
    print(result_even + " " + result_odd)

if __name__ == '__main__':
    for i in range(int(input())):
        loopstring(input())