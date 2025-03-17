#include <iostream>
#include <vector>
#include <queue>
using namespace std;

vector<int> edge[100001];
bool visited[100001];

int bfs(int start, int n) {
    queue<int> q;
    q.push(start);
    visited[start] = true;
    int cnt = 1;
    
    while (!q.empty()) {
        int cur = q.front();
        q.pop();
        
        for (int next : edge[cur]) {
            if (!visited[next]) {
                visited[next] = true;
                q.push(next);
                cnt++;
            }
        }
    }
    
    return cnt;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    
    int n, m;
    cin >> n >> m;
    
    for (int i = 0; i < m; i++) {
        int node1, node2;
        cin >> node1 >> node2;
        edge[node2].push_back(node1);
    }
    
    int maxTotal = 0;
    vector<int> comList;
    
    for (int i = 1; i <= n; i++) {
        fill(begin(visited), end(visited), false);
        int curTotal = bfs(i, n);
        
        if (maxTotal < curTotal) {
            maxTotal = curTotal;
            comList = {i};
        } else if (maxTotal == curTotal) {
            comList.push_back(i);
        }
    }
    
    for (int i : comList) {
        cout << i << " ";
    }
    cout << "\n";
    
    return 0;
}
