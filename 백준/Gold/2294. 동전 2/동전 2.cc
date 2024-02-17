#include <iostream>
#include <algorithm>
#include <cstring>

using namespace std;

int n, k;
int coin[101] = {0,};
int dp[10001] = {0,};

void input()
{
    cin >> n >> k;
    for(int i=0; i<n; i++)
        cin >> coin[i];
    memset(dp, 0, sizeof(dp));
}

void solution()
{
    for(int i=1; i<=k; i++) dp[i] = 10001;

    for(int i=0; i<n; i++)
    {
        for(int j=coin[i]; j<=k; j++)
        {
            dp[j] = min(dp[j], dp[j - coin[i]] + 1);
        }
    }
    if(dp[k] == 10001) cout << -1;
    else cout << dp[k];
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