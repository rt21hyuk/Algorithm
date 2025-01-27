#include <iostream>

using namespace std;

int n, m;
int board[2001];
int question[1000001][2];
bool palindrome[2001][2001] = { false, };

void input() {
	cin >> n;
	for (int i = 1; i <= n; i++) cin >> board[i];
	cin >> m;
	for (int i = 1; i <= m; i++) {
		cin >> question[i][0] >> question[i][1];
	}
}

void solution() {
	for (int i = 1; i <= n; i++) {
		palindrome[i][i] = true; // 한자리 수는 팰린드롬
		if (i != 1 && board[i - 1] == board[i]) palindrome[i - 1][i] = true; // 두자리 수는 두 수가 같으면 팰린드롬
	}
	// 세자리 이상일 경우, arr[start][end] 이고, palindrome[start+1][end-1]이면 팰린드롬
	for (int i = 2; i <= n - 1; i++) {
		for (int j = 1; i + j <= n; j++) {
			if (board[j] == board[i + j] && palindrome[j + 1][i + j - 1] == true) palindrome[j][i + j] = true;
		}
	}
	for (int i = 1; i <= m; i++) {
		int start = question[i][0], end = question[i][1];
		cout << palindrome[start][end] << "\n";
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