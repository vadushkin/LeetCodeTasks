#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

class Solution {
public:
    int maxIceCream(vector<int> &costs, int coins) {
        sort(costs.begin(), costs.end());

        int n = costs.size();
        int icecream = 0;

        while (icecream < n && costs[icecream] <= coins) {
            coins -= costs[icecream];
            icecream += 1;
        }

        return icecream;
    }
};


int main() {

    Solution s;
    vector<int> array = {1, 3, 2, 4, 1};

    cout << s.maxIceCream(array, 7) << endl;

    return 0;
}

/* Tests:
1. Runtime 421 ms Beats 32.47%
   Memory 76.5 MB Beats 76.68%

2. Runtime 276 ms Beats 45.94%
   Memory 76.5 MB Beats 76.68%
*/
