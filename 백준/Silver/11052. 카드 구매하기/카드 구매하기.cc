#include <iostream>
#include <vector>
using namespace std;

int n;
int card[1001];
int dp[1001];

void Input()
{
	cin >> n;
    for(int i=1; i<=n; i++)
        cin >> card[i];
}

void Solution()
{
    dp[1] = card[1];

    for(int i=2; i<=n; i++)
    {
        dp[i] = card[i];
        for(int j=1; j<i; j++)
        {
            dp[i] = max(dp[i], dp[i-j] + dp[j]);
        }
    }

	cout << dp[n] << "\n";
}

void Solve()
{
	Input();
	Solution();
}

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	Solve();
}