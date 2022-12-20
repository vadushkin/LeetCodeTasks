#include <iostream>


using namespace std;

class Solution {
public:
    bool isPalindrome(int x) {
        if (x < 0) {
            return false;
        }

        int num = x;
        long int rev = 0;

        while (x != 0) {
            rev = (rev * 10) + (x % 10);
            x = x / 10;
        }

        return num == rev;
    }
};

int main() {

    Solution s;
    cout << s.isPalindrome(121) << endl;

    return 0;
}

/* Tests:
1. Runtime 3 ms Beats 99.73%
   Memory 6 MB Beats 12.94%

2. Runtime 29 ms Beats 48.20%
   Memory 5.9 MB Beats 38.14%
*/
