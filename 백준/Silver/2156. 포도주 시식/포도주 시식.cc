#include <iostream>
#include <vector>

using namespace std;

int n;
int wine[10001];
int dp[10001];

void input()
{
	cin >> n;
	for(int i=1; i<=n; i++)	cin >> wine[i];
}

void solution()
{
	dp[1] = wine[1];
	dp[2] = wine[1] + wine[2];
	dp[3] = max(wine[1] + wine[3], max(wine[1] + wine[2], wine[2] + wine[3]));
	for(int i=4; i<=n; i++)
	{
		dp[i] = max(dp[i-3] + wine[i-1] + wine[i], max(dp[i-1], dp[i-2] + wine[i]));
	}
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
