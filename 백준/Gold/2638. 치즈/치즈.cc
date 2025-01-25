#include <iostream>
#include <queue>
#include <cstring>

using namespace std;

int n, m, ans = 0;
int area[101][101];
int visited[101][101];
int dr[] = {-1, 0, 1, 0}, dc[] = {0, -1, 0, 1};

void input() {
	cin >> n >> m;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			cin >> area[i][j];
		}
	}
}

bool bfs() {
	int cnt = 0;
	visited[0][0] = 1;
	queue<pair<int, int>> q;
	queue<pair<int, int>> nq;
	q.push({0, 0});
	ans++;

	while (!q.empty()) {
		int cr = q.front().first, cc = q.front().second;
		q.pop();

		for (int idx = 0; idx < 4; idx++) {
			int nr = cr + dr[idx], nc = cc + dc[idx];
			if (nr < 0 || nr >= n || nc < 0 || nc >= m) continue;
			if (visited[nr][nc]) continue;

			if (area[nr][nc] == 0) {
				q.push({nr, nc});
			}
			else {
				nq.push({nr, nc});
				cnt++;
			}
			visited[nr][nc] = 1;
		}
	}

	while (!nq.empty()) {
		int cr = nq.front().first, cc = nq.front().second;
		//cout << cr << " " << cc << " ";
		int side = 0;
		nq.pop();

		for (int idx = 0; idx < 4; idx++) {
			int nr = cr + dr[idx], nc = cc + dc[idx];
			if (nr < 0 || nr >= n || nc < 0 || nc >= m) continue;
			if (visited[nr][nc] and area[nr][nc] == 0) {
				side++;
			}
		}
		//cout << side << "\n";
		if (side >= 2) {
			q.push({ cr, cc });
			//area[cr][cc] = 0;
		}
	}

	while (!q.empty()) {
		int cr = q.front().first, cc = q.front().second;
		q.pop();
		area[cr][cc] = 0;
	}

	if (cnt == 0) {
		cout << ans-1;
		return true;
	}
	return false;
}

void solution() {
	while (true) {
		/*for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				cout << area[i][j] << " ";
			}
			cout << "\n";
		}
		cout << "\n";
		cout << "\n";*/
		if (bfs()) break;
		memset(visited, 0, sizeof(visited));
	}
}

void solve() {
	input();
	solution();
}

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	//freopen("input.txt", "r", stdin);
	solve();
	return 0;
}