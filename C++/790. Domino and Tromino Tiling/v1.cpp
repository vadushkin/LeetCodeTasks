#include <iostream>

using namespace std;


class Solution {
public:
    unsigned int numTilings(int n) {
        unsigned int dp[n + 3];

        dp[0] = 1;
        dp[1] = 2;
        dp[2] = 5;

        for (int i = 3; i < n; i++) {
            dp[i] = (2 * dp[i - 1] + dp[i - 3]) % 1000000007;
        }
        return dp[n - 1];
    }
};

int main() {

    Solution s;

    cout << s.numTilings(6) << endl;

    return 0;
}

/* Tests:
1. Runtime 0 ms Beats 100%
   Memory 6.1 MB Beats 71.49%

2. Runtime 3 ms Beats 55.84%
   Memory 5.9 MB Beats 93.27%
*/