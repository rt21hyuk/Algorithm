#include <iostream>
#include <vector>

using namespace std;

int n;
int step[301];
int dp[301];

void input()
{
	cin >> n;
	for(int i=1; i<=n; i++)	cin >> step[i];
}

void solution()
{
	dp[1] = step[1];
	dp[2] = step[1] + step[2];
	dp[3] = max(step[1] + step[3], step[2] + step[3]);
	for(int i=4; i<=n; i++)
	{
		dp[i] = max(dp[i-3] + step[i-1] + step[i], dp[i-2] + step[i]);
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
