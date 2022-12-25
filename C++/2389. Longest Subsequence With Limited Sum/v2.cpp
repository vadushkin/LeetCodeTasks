#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;

class Solution {
public:
    vector<int> answerQueries(vector<int> &nums, vector<int> &queries) {
        sort(begin(nums), end(nums));
        partial_sum(begin(nums), end(nums), begin(nums));
        transform(begin(queries), end(queries), begin(queries), [&](int q) {
            return upper_bound(begin(nums), end(nums), q) - begin(nums);
        });
        return queries;
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
   Memory 13.7 MB Beats 65.60%

2. Runtime 27 ms Beats 81.20%
   Memory 13.7 MB Beats 83.30%
*/
