// The function is declared with a void return type, so there is no value to return. 
// Modify the values in memory so that a contains their sum and b contains their absoluted difference.
// a' = a + b
// b' = |a - b|

#include <stdio.h>
#include <stdlib.h>

void update(int *a,int *b) {
    // Start code here
    *a += *b;
    *b = abs(*a - (*b * 2));  
}

int main() {
    int a, b;
    int *pa = &a, *pb = &b;
    
    scanf("%d %d", &a, &b);
    update(pa, pb);
    printf("%d\n%d", a, b);

    return 0;
}