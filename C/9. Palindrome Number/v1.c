#include <stdio.h>
#include <stdbool.h>

bool isPalindrome(int x) {
    if (x < 0) {
        return false;
    }

    int num = x;
    long int rev = 0;

    while(x != 0) {
        rev = (rev * 10) + (x % 10);
        x = x / 10;
    }

    return rev == num;
}


int main() {

    printf("%d", isPalindrome(121));

    return 0;
}

/* Tests:
1. Runtime 15 ms Beats 81.15%
   Memory 5.9 MB Beats 49.82%

2. Runtime 3 ms Beats 99.73%
   Memory 5.7 MB Beats 99.90%
*/
