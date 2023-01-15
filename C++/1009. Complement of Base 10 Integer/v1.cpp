#include <iostream>
#include <math.h>

using namespace std;

class Solution {
public:
    int bitwiseComplement(int n) {
        return n > 0 ? (int) ((1ll << ((int) log2(n) + 1)) - 1) ^ n : 1;
    }
};

int main() {

    Solution s;
    cout << s.bitwiseComplement(5) << endl;

    return 0;
}

/* Tests:
1. Runtime 0 ms Beats 100%
   Memory 5.9 MB Beats 87.98%

2. Runtime 3 ms Beats 36.42%
   Memory 6.1 MB Beats 11.2%
*/
