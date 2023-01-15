#include <iostream>

using namespace std;

class Solution {
public:
    int bitwiseComplement(int n) {
        int a = 1;

        while (n > a) a = a * 2 + 1;

        return a - n;
    }
};

int main() {

    Solution s;
    cout << s.bitwiseComplement(5) << endl;

    return 0;
}

/* Tests:
1. Runtime 0 ms Beats 100%
   Memory 5.9 MB Beats 56.46%

2. Runtime 0 ms Beats 100%
   Memory 5.9 MB Beats 87.98%
*/
