#include <iostream>
#include <vector>

using namespace std;

#define blank 0
#define cctv1 1
#define cctv2 2
#define cctv3 3
#define cctv4 4
#define cctv5 5
#define wall 6

int N, M, answer = 100;
int dx[] = {-1, 0, 1, 0}, dy[] = {0, -1, 0, 1};
int map[8][8] = {0, };
vector<pair<int, int>> posOfCctv;

void check(int x, int y, int dir)
{
    dir = dir % 4;
    while(1)
    {
        int nx = x + dx[dir];
        int ny = y + dy[dir];
        x = nx;
        y = ny;

        if(nx < 0 || ny < 0 || nx >= M || ny >= N) return;
        if(map[ny][nx] == wall) return;
        if(map[ny][nx] != blank) continue;
        map[ny][nx] = -1;
    }
}

void dfs(int depth)
{
    if(depth == posOfCctv.size())
    {
        int cnt = 0;
        for(int i=0; i<N; i++)
            for(int j=0; j<M; j++)
                if(map[i][j] == 0) cnt++;

        answer = min(answer, cnt);
        return;
    }

    int x = posOfCctv[depth].first;
    int y = posOfCctv[depth].second;
    int tempMap[8][8];

    for(int dir=0; dir<4; dir++)
    {
        for(int i=0; i<N; i++)
            for(int j=0; j<M; j++)
                tempMap[i][j] = map[i][j];

        if(map[y][x] == cctv1)
        {
            check(x, y, dir);
        }
        else if(map[y][x] == cctv2)
        {
            check(x, y, dir);
            check(x, y, dir+2);
        }
        else if(map[y][x] == cctv3)
        {
            check(x, y, dir);
            check(x, y, dir+1);
        }
        else if(map[y][x] == cctv4)
        {
            check(x, y, dir);
            check(x, y, dir+1);
            check(x, y, dir+2);
        }
        else if(map[y][x] == cctv5)
        {
            check(x, y, dir);
            check(x, y, dir+1);
            check(x, y, dir+2);
            check(x, y, dir+3);
        }

        dfs(depth+1);

        for(int i=0; i<N; i++)
            for(int j=0; j<M; j++)
                map[i][j] = tempMap[i][j];
    }
}

void input()
{
    cin >> N >> M;
    for(int i=0; i<N; i++)
    {
        for(int j=0; j<M; j++)
        {
            cin >> map[i][j];
            if(map[i][j] >= cctv1 && map[i][j] <= cctv5)
                posOfCctv.push_back({j, i});
        }
    }
}

void solution()
{
    dfs(0);
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