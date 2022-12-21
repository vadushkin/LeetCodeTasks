#include <iostream>
#include <queue>
#include <map>

using namespace std;

class Solution {
public:
    bool is_bipartite(int node, map<int, vector<int>> &adj, vector<int> &color) {
        queue<int> q;
        q.push(node);

        color[node] = 1;

        while (!q.empty()) {
            int cur = q.front();
            int curColor = color[cur];

            q.pop();

            for (int j: adj[cur]) {
                if (color[j] == -1) {
                    q.push(j);
                    color[j] = 1 - curColor;
                } else if (color[j] == curColor) {
                    return false;
                }
            }
        }

        return true;
    }

    bool possibleBipartition(int n, vector<vector<int>> &dislikes) {
        map<int, vector<int>> adj;
        vector<int> color(n + 1, -1);

        for (int i = 0; i < dislikes.size(); i++) {
            int p1 = dislikes[i][0];
            int p2 = dislikes[i][1];

            adj[p1].push_back(p2);
            adj[p2].push_back(p1);
        }

        for (int i = 1; i <= n; i++) {
            if (color[i] == -1 && !is_bipartite(i, adj, color)) {
                return false;
            }
        }
        return true;
    }
};

int main() {

    Solution s;
    int n = 4;
    vector<vector<int>> array = {
            {1, 2},
            {1, 3},
            {2, 4}
    };
    cout << s.possibleBipartition(n, array) << endl;

    return 0;
}

/* Tests:
1. Runtime 394 ms Beats 64.84%
   Memory 67.5 MB Beats 48.47%

2. Runtime 579 ms Beats 11.46%
   Memory 67.8 MB Beats 48.11%
*/
