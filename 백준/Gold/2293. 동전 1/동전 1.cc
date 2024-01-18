#include <iostream>
#include <vector>

using namespace std;

int n, k;
std::vector<int> coin;
std::vector<int> dp;

void input()
{
    std::cin >> n >> k;

    coin.assign(n, 0);
    dp.assign(k+1, 0);

    for(int i=0; i<n; i++)
    	std::cin >> coin[i];
}

void solution()
{
	dp[0] = 1;

	for(int i=0; i<n; i++)
	{
		for(int j=coin[i]; j<=k; j++)
		{
			dp[j] = dp[j] + dp[j - coin[i]];
		}
	}

	std::cout << dp[k];
}

void solve()
{
    input();
    solution();
}

int main()
{
//	freopen("input.txt", "r", stdin);
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    solve();
    return 0;
}
