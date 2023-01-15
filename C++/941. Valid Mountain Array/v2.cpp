#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    bool validMountainArray(vector<int> &arr) {
        int length = arr.size();
        int i = 0;

        while (i < length - 1 && arr[i] < arr[i + 1]) i++;

        if (i == length - 1 || i == 0) return false;

        while (i < length - 1 && arr[i] > arr[i + 1]) i++;

        if (i == length - 1) return true;
        else return false;
    }
};

int main() {

    Solution s;
    vector<int> array = {0, 1, 2, 3, 5, 4, 2, 1};

    cout << s.validMountainArray(array) << endl;

    return 0;
}

/* Tests:
1. Runtime 26 ms Beats 93.42%
   Memory 22.5 MB Beats 53.52%

2. Runtime 25 ms Beats 94.35%
   Memory 22.4 MB Beats 53.52%
*/
