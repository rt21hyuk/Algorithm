#include <iostream>
#include <algorithm>
#include <vector>

#define MAX 100001

int N, K, Answer=-1;
int dp[101][MAX];
int W[101];
int V[101];

int Max(int A, int B)
{
	if(A < B) return B;
	return A;
}

void INPUT()
{
	std::cin >> N >> K;

	for(int i=1; i<=N; i++)
	{
		std::cin >> W[i] >> V[i];
	}
}

void Solution()
{
    // https://cocoon1787.tistory.com/206
	for(int i=1; i<=N; i++)
	{
		for(int j=1; j<=K; j++)
		{
			if(j-W[i] >= 0) dp[i][j] = Max(dp[i-1][j], dp[i-1][j-W[i]]+V[i]);
			else dp[i][j] = dp[i-1][j];
		}
	}

	std::cout << dp[N][K];
}

void Solve()
{
	INPUT();
	Solution();
}

int main(int argc, char *argv[])
{
	std::cin.tie(NULL);
	std::ios::sync_with_stdio(false);

	//freopen("Input.txt", "r", stdin);
	Solve();

	return 0;
}
