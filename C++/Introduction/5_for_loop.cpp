/*
Input Format

You will be given two positive integers, a and b (a <= b), separated by a newline.

Output Format

For each integer  in the inclusive interval [a, b]:

If 1 <= n <= 9, then print the English representation of it in lowercase. That is "one" for 1, "two" for 2, and so on.
Else if n and it is an even number, then print "even".
Else if n and it is an odd number, then print "odd".
*/

#include <iostream>
#include <cstdio>
using namespace std;

int main() {
    int a, b, n;
    cin >> a;
    cin >> b;
    n = b - a;
    for (int i = a; i <= b; i++) {
        if (i >= 1 && i <= 9) {
            if (i == 1) {
                printf("one\n");
            }
            else if (i == 2) {
                printf("two\n");
            }
            else if (i == 3) {
                printf("three\n");
            }
            else if (i == 4) {
                printf("four\n");
            }
            else if (i == 5) {
                printf("five\n");
            }
            else if (i == 6) {
                printf("six\n");
            }
            else if (i == 7) {
                printf("seven\n");
            }
            else if (i == 8) {
                printf("eight\n");
            }
            else if (i == 9) {
                printf("nine\n");
        }
    }
    else if (i % 2 == 0) {
        printf("even\n");
    }
    else {
        printf("odd\n");
    }
}
}