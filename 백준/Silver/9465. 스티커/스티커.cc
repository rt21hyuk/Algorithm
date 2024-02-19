#include <iostream>
#include <vector>
using namespace std;

int n, tc;
int area[2][100001];
int dp[2][100001];

void Input()
{
	cin >> n;
    for(int i=0; i<2; i++)
        for(int j=1; j<=n; j++)
            cin >> area[i][j];
}

void Solution()
{
    dp[0][1] = area[0][1];
    dp[1][1] = area[1][1];

    for(int i=2; i<=n; i++)
    {
        dp[0][i] = max(dp[1][i-1], dp[1][i-2]) + area[0][i];
        dp[1][i] = max(dp[0][i-1], dp[0][i-2]) + area[1][i];
    }

    cout << max(dp[0][n], dp[1][n]) << "\n";
}

void Solve()
{
    cin >> tc;
	for(int i=0; i<tc; i++)
    {
        Input();
        Solution();
    }
}

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	Solve();
}