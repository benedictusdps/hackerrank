// Some C++ data types, their format specifiers, and their most common bit widths are as follows:

/* 
Int ("%d"): 32 Bit integer
Long ("%ld"): 64 bit integer
Char ("%c"): Character type
Float ("%f"): 32 bit real value
Double ("%lf"): 64 bit real value 
*/

#include <iostream>
#include <cstdio>
using namespace std;

int main() {
    // Complete the code.
    int d;
    long ld;
    char c;
    float f;
    double lf;
    scanf("%d %ld %c %f %lf", &d, &ld, &c, &f, &lf);
    printf("%d\n%ld\n%c\n%f\n%lf\n", d, ld, c, f, lf);
    return 0;
}