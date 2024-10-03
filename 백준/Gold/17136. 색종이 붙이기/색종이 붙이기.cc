#include <iostream>

using namespace std;

const int N_SIZE = 10;
const int PAPER_MAX_SIZE = 5;
const int PAPER_MAX_CNT = 5;

int answer = 987654321;
int arr[N_SIZE][N_SIZE] = { 0, };
int paper[PAPER_MAX_SIZE+1] = { 0,};

bool isPossible(int r, int c, int size) {
	for (int i = r; i < r + size; i++) {
		for (int j = c; j < c + size; j++) {
			if (arr[i][j] == 0) return false;
		}
	}
	return true;
}

void changeValue(int r, int c, int size, int value) {
	for (int i = r; i < r + size; i++) {
		for (int j = c; j < c + size; j++) {
			arr[i][j] = value;
		}
	}
}

void printArr() {
	for (int i = 0; i < N_SIZE; i++) {
		for (int j = 0; j < N_SIZE; j++) {
			cout << arr[i][j] << " ";
		}
		cout << "\n";
	}
	cout << "\n";
}

void dfs(int r, int c, int cnt) {
	if (cnt >= answer) return;
	while (arr[r][c] == 0) {
		c++;
		if (c >= N_SIZE) {
			r++;
			c = 0;
			if (r >= N_SIZE) {
				answer = min(answer, cnt);
				return;
			}
		}
	}

	for (int size = PAPER_MAX_SIZE; size >= 1; size--) {
		if (r + size > N_SIZE || c + size > N_SIZE) continue;
		if (paper[size] >= PAPER_MAX_CNT) continue;
		if (isPossible(r, c, size)) {
			paper[size]++;
			changeValue(r, c, size, 0);
			dfs(r, c, cnt+1);
			paper[size]--;
			changeValue(r, c, size, 1);
		}
	}
}

void input() {
	for (int i = 0; i < N_SIZE; i++)
		for (int j = 0; j < N_SIZE; j++)
			cin >> arr[i][j];
}

void solution() {
	dfs(0, 0, 0);
	if (answer == 987654321) answer = -1;
	cout << answer;
}

void solve() {
	input();
	solution();
}

int main(int argc, char* argv[]) {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	//freopen("input.txt", "r", stdin);
	solve();
	return 0;
}