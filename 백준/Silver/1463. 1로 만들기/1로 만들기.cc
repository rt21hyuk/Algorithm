#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main(int argc, char* argv[])
{
	ios::sync_with_stdio(false);
	cin.tie(0);

	int n;
	cin >> n;
	vector<int> dp(n + 1);

	dp[0] = 0;
	for (int i = 2; i <= n; i++)
	{
		dp[i] = dp[i - 1] + 1;
		if (i % 3 == 0) dp[i] = min(dp[i], dp[i / 3] + 1);
		if (i % 2 == 0) dp[i] = min(dp[i], dp[i / 2] + 1);
	}

	cout << dp[n] << "\n";
	return 0;
}