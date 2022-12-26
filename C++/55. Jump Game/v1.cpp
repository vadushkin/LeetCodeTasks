#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    bool canJump(vector<int> &nums) {
        int goal = nums.size() - 1;

        for (int i = nums.size() - 1; i >= 0; --i) {
            if ((nums[i] + i) >= goal) {
                goal = i;
            }
        }
        return !goal;
    }
};


int main() {

    Solution s;
    vector<int> array = {3, 2, 1, 0, 1};

    cout << s.canJump(array) << endl;

    return 0;
}

/* Tests:
1. Runtime 76 ms Beats 83.39%
   Memory 48.3 MB Beats 94.13%

2. Runtime 68 ms Beats 91.43%
   Memory 48.3 MB Beats 94.13%
*/
