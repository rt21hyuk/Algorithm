#include <iostream>
#include <vector>

using namespace std;

int n;
long long dp[1000001];

void input()
{
	cin >> n;
}

void solution()
{
	dp[0] = 1;
	dp[1] = 1;
	dp[2] = 2;
	for(int i=3; i<=n; i++)
		dp[i] = (2 * dp[i-2] + dp[i-3]) % 15746;
	cout << dp[n] << "\n";
}

void solve()
{
    input();
	solution();
}

int main()
{
    cin.tie(NULL);
    ios::sync_with_stdio(false);
//	freopen("input.txt", "r", stdin);
    solve();
    return 0;
}
