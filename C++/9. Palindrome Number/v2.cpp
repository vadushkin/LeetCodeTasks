#include <iostream>


using namespace std;

class Solution {
public:
    bool isPalindrome(int x) {
        string str_x = to_string(x);
        int len = str_x.size();

        for (int i = 0; i <= len / 2; i++) {
            if (str_x[i] != str_x[len - i - 1]) {
                return false;
            }
        }
        return true;
    }
};

int main() {

    Solution s;
    cout << s.isPalindrome(121) << endl;

    return 0;
}

/* Tests:
1. Runtime 32 ms Beats 40.86%
   Memory 5.9 MB Beats 76.91%

2. Runtime 16 ms Beats 83.18%
   Memory 6 MB Beats 38.14%
*/
