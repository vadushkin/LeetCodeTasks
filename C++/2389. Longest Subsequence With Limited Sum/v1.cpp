#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<int> answerQueries(vector<int> A, vector<int> &queries) {
        sort(A.begin(), A.end());

        vector<int> answer;

        for (int i = 1; i < A.size(); ++i)
            A[i] += A[i - 1];

        for (int &q: queries)
            answer.push_back(upper_bound(A.begin(), A.end(), q) - A.begin());

        return answer;
    }
};

int main() {

    Solution s;

    vector<int> nums = {4, 5, 2, 1};
    vector<int> queries = {3, 10, 21};

    vector<int> answer = s.answerQueries(nums, queries);

    for (int i: answer) {
        cout << i << endl;
    }

    return 0;
}

/* Tests:
1. Runtime 17 ms Beats 94.40%
   Memory 13.8 MB Beats 65.60%

2. Runtime 18 ms Beats 93.30%
   Memory 14.1 MB Beats 12.20%
*/
