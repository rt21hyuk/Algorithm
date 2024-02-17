#include <iostream>
#include <algorithm>
#include <cstring>

using namespace std;

int n;
int dp[31];

void input()
{
    cin >> n;
}

void solution()
{
    dp[0] = 1;
    dp[1] = 0;
    dp[2] = 3;
    for(int i=4; i<=n; i=i+2)
    {
        dp[i] = dp[i-2] * dp[2];

        for(int j=i-4; j>=0; j=j-2)
            dp[i] = dp[i] + 2*dp[j];
    }
    cout << dp[n];
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
	// freopen("input.txt", "r", stdin);
    solve();
    return 0;
}