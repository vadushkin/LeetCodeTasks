#include <iostream>
#include <vector>

using namespace std;


class Solution {
public:
    bool canJump(vector<int> &nums) {
        int n = nums.size();
        vector<bool> jump(n, false);
        jump[n - 1] = true;

        for (int i = n - 2; i >= 0; i--) {
            for (int j = 0; j <= nums[i] && i + j < n; j++) {
                if (jump[i + j]) {
                    jump[i] = true;
                    break;
                }
            }
        }

        return jump[0];
    }
};

int main() {

    Solution s;
    vector<int> array = {3, 2, 1, 0, 3};

    cout << s.canJump(array) << endl;

    return 0;
}

/* Tests:
1. Runtime 756 ms Beats 19.80%
   Memory 48.7 MB Beats 24.23%

2. Runtime 746 ms Beats 19.92%
   Memory 48.7 MB Beats 27.13%
*/
