#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int repeatedNTimes(vector<int> &A) {
        for (int i = 2; i < A.size(); ++i)
            if (A[i] == A[i - 1] || A[i] == A[i - 2])
                return A[i];

        return A[0];
    }
};


int main() {

    Solution s;
    vector<int> array = {1, 2, 3, 3};
    cout << s.repeatedNTimes(array) << endl;

    return 0;
}

/* Tests:
1. Runtime 43 ms Beats 78.99%
   Memory 24.7 MB Beats 68.75%

2. Runtime 34 ms Beats 90.89%
   Memory 24.6 MB Beats 90.89%
*/
