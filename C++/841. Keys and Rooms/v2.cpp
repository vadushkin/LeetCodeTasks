#include <iostream>
#include <queue>


using namespace std;

class Solution {
public:
    void dfs(int u, vector<vector<int>> &g, vector<bool> &vis) {
        vis[u] = true;

        for (int v: g[u]) {
            if (!vis[v]) {
                dfs(v, g, vis);
            }
        }
    }

    bool canVisitAllRooms(vector<vector<int>> &rooms) {
        int n = rooms.size();
        vector<bool> vis(n + 1);

        dfs(0, rooms, vis);

        for (int i = 1; i < n; i++)
            if (!vis[i])
                return false;

        return true;
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

/*  Tests:
1. Runtime 20 ms Beats 47.53%
   Memory 10.5 MB Beats 58.80%

2. Runtime 19 ms Beats 52.82%
   Memory 10.5 MB Beats 35.11%
*/
