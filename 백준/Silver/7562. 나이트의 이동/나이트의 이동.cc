#include <iostream>
#include <algorithm>
#include <queue>
#include <tuple>

using namespace std;

int T, L=0, Cnt=0, prevL=0;
int dx[] = {-2, -1, 1, 2, 2, 1, -1, -2};
int dy[] = {1, 2, 2, 1, -1, -2, -2, -1};
std::pair<int, int> startPoint, targetPoint;
bool visited[300][300] = {false, };

void init()
{
    prevL = L;
    for(int i=0; i<prevL; i++)
    {
        for(int j=0; j<prevL; j++)
        {
            visited[i][j] = false;
        }
    }
    Cnt = 0;
}

void input()
{
    int s_x, s_y, t_x, t_y;
    std::cin >> L;
    std::cin >> s_x >> s_y;
    std::cin >> t_x >> t_y;
    startPoint = {s_x, s_y};
    targetPoint = {t_x, t_y};
}

int BFS(int cx, int cy)
{
    std::queue<std::tuple<int, int, int>> q;
    q.push(std::make_tuple(cx, cy, 0));
    visited[cy][cx] = true;

    while(!q.empty())
    {
        int x = get<0>(q.front()), y = get<1>(q.front()), cnt = get<2>(q.front());
        q.pop();

        if(x == targetPoint.first && y == targetPoint.second)
            return cnt;

        for(int i=0; i<8; i++)
        {
            int nx = x + dx[i], ny = y + dy[i], ncnt = cnt + 1;
            if(nx >= 0 && nx < L && ny >= 0 && ny < L)
            {
                if(visited[ny][nx] == false)
                {
                    q.push(std::make_tuple(nx, ny, ncnt));
                    visited[ny][nx] = true;
                }
            }
        }
    }
}

void solution()
{
    std::cout << BFS(startPoint.first, startPoint.second) << "\n";
}

void solve()
{
    std::cin >> T;
    for(int k=0; k<T; k++)
    {
        init();
        input();
        solution();
    }
}

int main()
{
    std::cin.tie(NULL);
	std::ios::sync_with_stdio(false);
	// freopen("input.txt", "r", stdin);
    solve();
    return 0;
}