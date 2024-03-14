#include <iostream>
#include <algorithm>
#include <cstring>

#define Max_N 100000

int main(int argc, char argv[])
{
	std::ios_base::sync_with_stdio(false);
	std::cin.tie(NULL);

	int n;
	std::cin >> n;

	int dp[Max_N + 1] = { 0, };
	memset(dp, -1, sizeof(dp));

	dp[0] = -1;
	dp[1] = -1;
	dp[2] = 1;
	dp[3] = -1;
	dp[4] = 2;
	dp[5] = 1;
	dp[6] = 3;
	dp[7] = 2;
	dp[8] = 4;

	for (int i = 9; i <= n; i++)
	{
		dp[i] = dp[i-5] + 1;
	}

	std::cout << dp[n];

	return 0;
}
