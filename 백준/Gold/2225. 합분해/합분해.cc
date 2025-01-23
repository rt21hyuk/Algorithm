#include <iostream>

using namespace std;

int N, K;
long long dp[201][201];

void input() {
	cin >> N >> K;
}

void solution() {
	/*
	dp[a][b] = c -> a개 더해서 그 합이 b가 되는 경우의 수는 c

	dp[k][n] -> 숫자를 K개를 뽑아서 그 합이 N이 되는 경우의 수

	마지막 k번째 숫자를 뽑을 때, K - 1번째 숫자까지 뽑았을 때의 경우의 수가 영향을 미침

	예로 k-1번째 숫자까지 뽑았을 때, 그 합이 N이라면 0을 뽑고, N-1이면 1, ... 0이면 N을 뽑음 -> 1가지 경우만 존재하므로

	점화식 dp[k][n] = dp[k-1][0] + dp[k-1][1] + ... + dp[k-1][n]
	*/

	for (int i = 0; i <= N; i++) { // 어떤 수를 한개만 더해서 n이 나오는 경우의 수는 n 자신 하나
		dp[1][i] = 1;
	}
	for (int k = 2; k <= K; k++) {
		for (int n = 0; n <= N; n++) {
			for (int i = 0; i <= n; i++) {
				dp[k][n] = dp[k][n] + dp[k - 1][i];
			}
			dp[k][n] = dp[k][n] % 1000000000;
		}
	}
	cout << dp[K][N];
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