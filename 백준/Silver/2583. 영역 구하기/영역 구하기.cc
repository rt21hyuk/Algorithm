#include <iostream>
#include <cstring>
#include <queue>
#include <vector>
#include <algorithm>

using namespace std;

const int N_MAX = 101, M_MAX = 101;

int n, m, k, answer = 0;
int maps[N_MAX][M_MAX];
int visited[N_MAX][M_MAX];
int dx[] = { -1, 0, 1, 0 }, dy[] = {0, -1, 0, 1};
vector<int> areas;

void bfs(int y, int x) {
	queue<pair<int, int>> q;
	visited[y][x] = 1;
	q.push({ y, x });
	int area = 1;

	while (!q.empty()) {
		int cy = q.front().first, cx = q.front().second;
		q.pop();
		for (int i = 0; i < 4; i++) {
			int ny = cy + dy[i], nx = cx + dx[i];

			if (nx < 0 || ny < 0 || nx >= m || ny >= n) continue;
			if (visited[ny][nx] == 1 || maps[ny][nx] == 1) continue;

			q.push({ ny, nx });
			visited[ny][nx] = 1;
			area++;
		}
	}
	areas.push_back(area);
}

void input() {
	cin >> n >> m >> k;
	memset(maps, 0, sizeof(maps));
	memset(visited, 0, sizeof(visited));

	for (int i = 0; i < k; i++) {
		int x1, y1, x2, y2;
		cin >> x1 >> y1 >> x2 >> y2;

		for (int x = x1; x < x2; x++) {
			for (int y = y1; y < y2; y++) {
				if (maps[y][x] == 0) maps[y][x] = 1;
			}
		}
	}
}

void solve() {
	for (int j = 0; j < n; j++) {
		for (int i = 0; i < m; i++) {
			if (maps[j][i] == 0 && !visited[j][i]) {
				bfs(j, i);
				answer++;
			}
		}
	}
	cout << answer << "\n";
	sort(areas.begin(), areas.end());

	for (auto iter : areas) {
		cout << iter << " ";
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