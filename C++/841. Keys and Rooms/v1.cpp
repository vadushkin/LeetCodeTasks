#include <iostream>
#include <queue>
#include <algorithm>

using namespace std;


class Solution {
public:
    bool canVisitAllRooms(vector<vector<int>> &rooms) {
        vector<bool> visited(rooms.size(), false);
        queue<int> q;

        q.push(0);

        while (!q.empty()) {
            int size = q.size();
            for (int i = 0; i < size; i++) {
                int room = q.front();
                q.pop();
                visited[room] = true;

                for (int ele: rooms[room])
                    if (!visited[ele]) {
                        q.push(ele);
                    }
            }
        }
        return count(visited.begin(), visited.end(), true) == rooms.size();
    }
};

int main() {

    Solution s;
    vector<vector<int>> array = {
            {1},
            {2},
            {3},
            {}
    };

    cout << s.canVisitAllRooms(array) << endl;

    return 0;
}

/*   Tests:
1. Runtime 16 ms Beats 65.74%
   Memory 10.5 MB Beats 58.80%

2. Runtime 18 ms Beats 56.98%
   Memory 10.4 MB Beats 58.80%
*/
