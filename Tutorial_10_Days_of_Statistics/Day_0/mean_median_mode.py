# Given an array, X, of N integers, calculate and print the respective mean, median, and mode on separate lines. 
# If your array contains more than one modal value, choose the numerically smallest one.

# Sample input
# 10
# 64630 11735 14216 99233 14470 4978 73429 38120 51135 67060

# Enter your code here. Read input from STDIN. Print output to STDOUT

N = int(input())
X = input().split()

# Convert the list from str into int
for i in range(len(X)):
    X[i] = int(X[i])

# Sort the list
X.sort()

# Calculate mean
total_X = 0
for i in range(N):
    total_X += int(X[i])
mean = total_X / N
print(mean)

# Calculate median
half_N = int(N/2)
if N % 2 == 0:
    median = (int(X[half_N - 1]) + int(X[half_N]))/2
else:
    median = int(X[half_N])
print(median)

# Calculate mode
mode = max(X, key=X.count)
print(mode)