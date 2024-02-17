#include <iostream>
#include <algorithm>
#include <queue>
#include <cstring>

#define blank 0
#define shark 9

using namespace std;

int n, sharkSize=2, totalMove=0, ate=0;
int sharkX, sharkY;
int map[20][20];
int visited[20][20];
int dx[] = {0, -1, 0, 1};
int dy[] = {-1, 0, 1, 0};

void input()
{
    cin >> n;
    for(int i=0; i<n; i++)
    {
        for(int j=0; j<n; j++)
        {
            cin >> map[i][j];
            if(map[i][j] == shark)  {
                sharkY = i, sharkX = j;
                map[i][j] = blank;
            }
        }
    }
}

int bfs(int y, int x)
{
    int dist = 0;
    visited[y][x] = 1;
    queue<pair<int, int>> q;
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    q.push({y, x});

    while(!q.empty())
    {
        int cy = q.front().first, cx = q.front().second; 
        q.pop();

        if(visited[cy][cx] == dist) break;

        for(int i=0; i<4; i++)
        {
            int ny = cy + dy[i], nx = cx + dx[i];
            if(ny < 0 || nx < 0 || ny >= n || nx >= n)  continue;
            if(visited[ny][nx]) continue;

            if(map[ny][nx] == blank || map[ny][nx] == sharkSize)
            {
                visited[ny][nx] = visited[cy][cx] + 1;
                q.push({ny, nx});
            }
            else if(map[ny][nx] < sharkSize)
            {
                if(dist == 0)   ate++;
                visited[ny][nx] = visited[cy][cx] + 1;
                dist = visited[ny][nx];
                pq.push({ny, nx});
            }
        }
    }
    if(pq.empty())
        return 0;

    sharkY = pq.top().first;
    sharkX = pq.top().second;
    map[sharkY][sharkX] = blank;

    if(ate == sharkSize)
    {
        sharkSize++;
        ate = 0;
    }
    return visited[sharkY][sharkX] - 1;
}

void solution()
{
    while(1)
    {
        for(int i=0; i<n; i++)
            memset(visited[i], 0, sizeof(int)*n);
        
        int sec = bfs(sharkY, sharkX);
        if(sec == 0) break;
        totalMove = totalMove + sec;
    }
    cout << totalMove << "\n";
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