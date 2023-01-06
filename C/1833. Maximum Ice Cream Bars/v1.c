#include <stdio.h>
#include <stdlib.h>

int comparator(const void *p, const void *q) {
    return (*(int *) p - *(int *) q);
}

int maxIceCream(int *costs, int size, int coins) {
    qsort((void *) costs, size, sizeof(costs[0]), comparator);

    for (int i = 0; i < size; ++i)
        if ((coins -= costs[i]) < 0) return i;

    return size;
}

int main() {

    int array[] = {1, 2, 3, 4, 1};

    printf("%d", maxIceCream(array, 5, 7));

    return 0;
}

/* Tests:
1. Runtime 226 ms Beats 100%
   Memory 16.3 MB Beats 25%

2. Runtime 217 ms Beats 100%
   Memory 16.4 MB Beats 25%
*/
