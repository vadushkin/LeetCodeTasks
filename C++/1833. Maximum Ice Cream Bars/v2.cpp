#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

class Solution {
public:
    int maxIceCream(vector<int> &costs, int coins) {
        sort(costs.begin(), costs.end());

        for (int i = 0; i < costs.size(); ++i)
            if ((coins -= costs[i]) < 0)
                return i;

        return costs.size();
    }
};


int main() {

    Solution s;
    vector<int> array = {1, 3, 2, 4, 1};

    cout << s.maxIceCream(array, 7) << endl;

    return 0;
}

/* Tests:
1. Runtime 354 ms Beats 41.80%
   Memory 76.5 MB Beats 76.68%

2. Runtime 262 ms Beats 46.81%
   Memory 76.6 MB Beats 32.82%
*/
