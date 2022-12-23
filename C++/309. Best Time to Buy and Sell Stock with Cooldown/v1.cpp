#include <iostream>
#include <vector>
#include <mem.h>

using namespace std;

class Solution {
public:
    int dp[5001][2];

    int helper(vector<int> &prices, int curr, int n, bool hadBought) {
        if (curr >= n) {
            return 0;
        }
        if (dp[curr][hadBought] != -1) {
            return dp[curr][hadBought];
        }

        int profit;

        if (!hadBought) {
            int BUY = (-prices[curr]) +
                      helper(prices, curr + 1, n, true);
            int NOT_BUY = helper(prices, curr + 1, n, hadBought);
            profit = max(BUY, NOT_BUY);
        } else {
            int SELL = prices[curr] + helper(prices, curr + 2, n, false);
            int NOT_SELL = helper(prices, curr + 1, n, hadBought);
            profit = max(SELL, NOT_SELL);
        }
        return dp[curr][hadBought] = profit;
    }

    int maxProfit(vector<int> &prices) {
        memset(dp, -1, sizeof(dp));

        int n = prices.size();

        return helper(prices, 0, n, false);
    }
};


int main() {

    Solution s;
    vector<int> array = {1, 2, 3, 0, 2};

    cout << s.maxProfit(array) << endl;

    return 0;
}

/* Tests:
1. Runtime 3 ms Beats 91.63%
   Memory 11.5 MB Beats 56.69%

2. Runtime 3 ms Beats 91.63%
   Memory 11.4 MB Beats 59.53%
*/
