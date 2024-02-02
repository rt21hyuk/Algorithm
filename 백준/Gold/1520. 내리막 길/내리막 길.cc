#include <iostream>
#include <vector>

using namespace std;

int M, N, answer=0;
int map[500][500] = {0, };
int dp[500][500] = {0, };
int dx[] = {-1, 0, 1, 0}, dy[] = {0, -1, 0, 1};

void input()
{
    cin >> M >> N;
    for(int i=0; i<M; i++)
        for(int j=0; j<N; j++)
        {
            cin >> map[i][j];
            dp[i][j] = -1;
        }
}

int dfs(int x, int y)
{
    if(x == N-1 && y == M-1)    return 1;
    if(dp[y][x] != -1)  return dp[y][x];

    dp[y][x] = 0;

    for(int i=0; i<4; i++)
    {
        int nx = x + dx[i], ny = y + dy[i];

        if(nx>=0 && ny>=0 && nx<N && ny<M)
        {
            if(map[ny][nx] < map[y][x])
            {
                dp[y][x] = dp[y][x] + dfs(nx, ny);
            }
        }
    }
    
    return dp[y][x];
}

void solution()
{
    answer = dfs(0, 0);
    cout << answer;
}

void solve()
{
    input();
    solution();
}

int main()
{
    std::cin.tie(NULL);
	std::ios::sync_with_stdio(false);
	// freopen("input.txt", "r", stdin);
    solve();
    return 0;
}