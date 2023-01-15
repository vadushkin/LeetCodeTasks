#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int repeatedNTimes(vector<int> &nums) {
        int i = 0, j = 0, n = nums.size();

        while (i == j || nums[i] != nums[j])
            i = rand() % n, j = rand() % n;

        return nums[i];
    }
};


int main() {

    Solution s;
    vector<int> array = {1, 2, 3, 3};
    cout << s.repeatedNTimes(array) << endl;

    return 0;
}

/* Tests:
1. Runtime 33 ms Beats 91.75%
   Memory 24.6 MB Beats 99.39%

2. Runtime 34 ms Beats 90.89%
   Memory 24.8 MB Beats 68.75%
*/
