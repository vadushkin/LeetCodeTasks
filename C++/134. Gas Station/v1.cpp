#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int canCompleteCircuit(vector<int> &gas, vector<int> &cost) {
        int total_gas = 0, total_cost = 0;
        int curr_gas = 0, starting_point = 0;

        for (int i = 0; i < gas.size(); i++) {

            total_gas += gas[i];
            total_cost += cost[i];
            curr_gas += gas[i] - cost[i];

            if (curr_gas < 0) {
                starting_point = i + 1;
                curr_gas = 0;
            }
        }
        return (total_gas < total_cost) ? -1 : starting_point;
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
1. Runtime 91 ms Beats 80.36%
   Memory 69.4 MB Beats 55.78%

2. Runtime 98 ms Beats 68.85%
   Memory 69.5 MB Beats 12.90%
*/
