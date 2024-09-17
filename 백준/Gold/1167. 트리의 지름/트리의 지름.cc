#include <iostream>
#include <vector>
#include <cstring>

using namespace std;

int v;
const int MAX = 100001;

vector<pair<int, int>> graph[MAX];
int visited[MAX] = { 0, };
int maxDist = 0;
int maxNode;

void input() {
	cin >> v;
	for (int i = 0; i < v; i++) {
		int from;
		cin >> from;
		while (1) {
			int to, cost;
			cin >> to;
			if (to != -1) {
				cin >> cost;
				graph[from].push_back({ to, cost });
			}
			else break;
		}
	}
}

void dfs(int node, int dist) {
	if (visited[node]) return;

	if (maxDist < dist)
	{
		maxDist = dist;
		maxNode = node;
	}
	visited[node] = 1;

	for (int i = 0; i < graph[node].size(); i++) {
		int nextNode = graph[node][i].first;
		int nextDist = graph[node][i].second;
		dfs(nextNode, dist + nextDist);
	}
}

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	//freopen("input.txt", "r", stdin);
	input();
	dfs(1, 0);
	maxDist = 0;
	memset(visited, 0, sizeof(visited));
	dfs(maxNode, 0);
	cout << maxDist;
	return 0;
}