#include <iostream>
#include <string>
#include <vector>
#include <queue>

using namespace std;

vector<int> solution(int n, vector<vector<int>> roads, vector<int> sources, int destination) {
    vector<int> answer;
    vector<int> costs(n+1, -1);
    vector<vector<int>> edges(n+1);
    for(int i=0; i<roads.size(); i++) {
        int v1 = roads[i][0], v2 = roads[i][1];
        edges[v1].push_back(v2);
        edges[v2].push_back(v1);
    }
    
    queue<pair<int, int>> q;
    q.push({destination, 0});
    costs[destination] = 0;
    
    while(!q.empty()) {
        int cur = q.front().first, curCost = q.front().second;
        q.pop();
        for(int i=0; i<edges[cur].size(); i++) {
            int next = edges[cur][i];
            if(costs[next] != -1) continue; // 방문하지 않았으면
            
            q.push({next, curCost + 1});
            costs[next] = curCost + 1;
        }
    }
    
    for(int source:sources) {
        answer.push_back(costs[source]);    
    }
    return answer;
}