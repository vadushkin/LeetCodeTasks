#include <stdbool.h>
#include <stdio.h>

#define MAX(a, b) (a > b ? a : b)

bool canJump(int *nums, int numsSize) {
    int i;
    int reach = 0;

    for (i = 0; i < (numsSize - 1); i++) {
        reach = MAX(reach, (i + nums[i]));
        if (i >= reach || reach >= (numsSize - 1)) {
            break;
        }
    }
    return (reach >= (numsSize - 1)) ? true : false;
}

int main() {

    int array[5] = {3, 2, 1, 0, 4};
    printf("%d", canJump(array, 5));

    return 0;
}

/* Tests:
1. Runtime 72 ms Beats 90.35%
   Memory 8.3 MB Beats 57.92%

2. Runtime 64 ms Beats 99.3%
   Memory 8.6 MB Beats 26.6%
*/
