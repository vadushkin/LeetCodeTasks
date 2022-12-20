#include <stdio.h>
#include <stdbool.h>

bool isPalindrome(int x) {
    if (x < 0) return false;

    char str[16];
    int len = sprintf(str, "%d", x);

    for (int i = 0; i <= (len / 2); ++i) {
        if (str[i] != str[len - i - 1])
            return false;
    }
    return true;
}

int main() {

    printf("%d", isPalindrome(1234321));

    return 0;
}

/* Tests:
1. Runtime 26 ms Beats 37.85%
   Memory 5.9 MB Beats 49.82%

2. Runtime 20 ms Beats 60.39%
   Memory 6 MB Beats 24.63%
*/
