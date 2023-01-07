#include <iostream>
#include <vector>
#include <numeric>

using namespace std;

class Solution {
public:
    int canCompleteCircuit(vector<int> &gas, vector<int> &cost) {
        int sum_gas = accumulate(begin(gas), end(gas), 0, plus<int>());
        int sum_cost = accumulate(begin(cost), end(cost), 0, plus<int>());

        if (sum_gas < sum_cost) return -1;

        int tank = 0, index = 0;

        for (int i = 0; i < gas.size(); i++) {
            tank += gas[i] - cost[i];

            if (tank < 0) {
                tank = 0;
                index = i + 1;
            }
        }
        return index;
    }
};


int main() {

    Solution s;

    vector<int> gas = {1, 2, 3, 4, 5};
    vector<int> cost = {3, 4, 5, 1, 2};

    cout << s.canCompleteCircuit(gas, cost) << endl;

    return 0;
}

/* Tests:
1. Runtime 69 ms Beats 99.52%
   Memory 69.5 MB Beats 55.78%

2. Runtime 88 ms Beats 84.98%
   Memory 69.5 MB Beats 12.90%
*/
