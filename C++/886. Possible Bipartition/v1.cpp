#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    bool bipartite(int src, vector<vector<int>> &adj, vector<int> &color) {
        if (color[src] == -1) {
            color[src] = 0;
        }

        for (auto it: adj[src]) {
            if (color[it] == -1) {
                color[it] = 1 - color[src];

                if (not bipartite(it, adj, color)) {
                    return false;
                }

            } else if (color[it] == color[src]) {
                return false;
            }
        }
        return true;
    }

    bool possibleBipartition(int n, vector<vector<int>> &dislikes) {
        vector<vector<int>> adj(n + 1);

        for (auto &dislike: dislikes) {
            adj[dislike[0]].push_back(dislike[1]);
            adj[dislike[1]].push_back(dislike[0]);
        }

        vector<int> color(n + 1, -1);

        for (int i = 0; i < n; i++) {
            if (color[i] == -1) {
                if (not bipartite(i, adj, color)) {
                    return false;
                }
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
1. Runtime 423 ms Beats 59.15%
   Memory 64.9 MB Beats 64.27%

2. Runtime 415 ms Beats 60.43%
   Memory 64.7 MB Beats 70.32%
*/
