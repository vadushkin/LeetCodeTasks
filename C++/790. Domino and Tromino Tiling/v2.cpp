#include <iostream>

using namespace std;


class Solution {
public:
    int numTilings(int n) {
        if (n <= 2)
            return n;
        if (n == 3)
            return 5;

        long res, a = 1, b = 2, c = 5;

        while (n-- > 3) {
            res = (2 * c + a) % int(1e9 + 7);

            a = b;
            b = c;
            c = res;
        }
        return res;
    }
};

int main() {

    Solution s;

    cout << s.numTilings(30) << endl;

    return 0;
}

/* Tests:
1. Runtime 3 ms Beats 55.84%
   Memory 6 MB Beats 71.49%

2. Runtime 3 ms Beats 55.84%
   Memory 6 MB Beats 80.59%
*/
