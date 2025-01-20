#include <iostream>
#include <algorithm>
#include <queue>
#include <cstring>

using namespace std;

int n, m, result = 0, hour = 0;
int area[101][101];
bool visited[101][101];
int dr[4] = { -1, 0, 1, 0 }, dc[4] = {0, -1, 0, 1};

void input() {
	cin >> n >> m;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			cin >> area[i][j];
		}
	}
}

bool bfs() {
	visited[0][0] = true;
	int cnt = 0;
	queue<pair<int, int>> q;
	q.push({ 0, 0 });
	hour++;

	while (!q.empty()) {
		int r = q.front().first, c = q.front().second;
		q.pop();

		for (int idx = 0; idx < 4; idx++) {
			int nr = r + dr[idx], nc = c + dc[idx];
			if (nr < 0 || nr >= n || nc < 0 || nc >= m) continue;
			if (visited[nr][nc]) continue;

			if (area[nr][nc] == 0) {
				q.push({ nr, nc });
			}
			else {
				area[nr][nc] = 0;
				cnt++;
			}
			visited[nr][nc] = true;
		}
	}

	if (cnt == 0) {
		cout << hour - 1 << "\n" << result;
		return true;
	}

	result = cnt;
	return false;
}

void solve() {
	while (true) {
		if (bfs()) {
			break;
		}
		memset(visited, false, sizeof(visited));
	}
}

void solution() {
	input();
	solve();
}

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	//freopen("input.txt", "r", stdin);
	solution();
	return 0;
}