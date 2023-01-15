#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    bool validMountainArray(vector<int> &A) {
        int n = A.size(), i = 0, j = n - 1;

        while (i + 1 < n && A[i] < A[i + 1]) i++;
        while (j > 0 && A[j - 1] > A[j]) j--;

        return i > 0 && i == j && j < n - 1;
    }
};


int main() {

    Solution s;
    vector<int> array = {0, 1, 2, 3, 5, 4, 2, 1};

    cout << s.validMountainArray(array) << endl;

    return 0;
}

/* Tests:
1. Runtime 40 ms Beats 49.10%
   Memory 22.5 MB Beats 6.76%

2. Runtime 34 ms Beats 67.39%
   Memory 22.5 MB Beats 53.52%
*/
