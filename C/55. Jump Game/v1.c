#include <stdio.h>
#include <stdbool.h>


bool canJump(int *nums, int n) {
    int goal = n - 1, i;

    for (i = n; i--;)
        if (i + nums[i] >= goal)
            goal = i;

    return !goal;
}

int main() {

    int array[5] = {4, 2, 1, 0, 4};
    printf("%d", canJump(array, 5));

    return 0;
}

/* Tests:
1. Runtime 65 ms Beats 99.3%
   Memory 8.5 MB Beats 26.6%

2. Runtime 73 ms Beats 88.61%
   Memory 8.3 MB Beats 76.83%
*/
