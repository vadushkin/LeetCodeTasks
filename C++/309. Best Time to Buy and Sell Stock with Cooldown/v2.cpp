#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int maxProfit(vector<int> &prices) {
        int buy(INT_MIN), sell(0), prev_sell(0), prev_buy;

        for (int price: prices) {
            prev_buy = buy;
            buy = max(prev_sell - price, buy);
            prev_sell = sell;
            sell = max(prev_buy + price, sell);
        }

        return sell;
    }
};


int main() {

    Solution s;
    vector<int> array = {1, 2, 3, 0, 2};

    cout << s.maxProfit(array) << endl;

    return 0;
}

/* Tests:
1. Runtime 0 ms Beats 100%
   Memory 11.2 MB Beats 91.1%

2. Runtime 3 ms Beats 91.63%
   Memory 11.2 MB Beats 91.1%
*/
