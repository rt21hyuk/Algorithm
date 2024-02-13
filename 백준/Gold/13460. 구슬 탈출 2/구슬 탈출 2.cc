#include <iostream>
#include <vector>
#include <queue>
using namespace std;

#define wall '#'
#define blank '.'
#define hole 'O'
#define redBead 'R'
#define blueBead 'B'

struct info {
	int rx, ry, bx, by, count;
};

int n, m, ans = -1;
info start;
string map[11];
int dx[] = {-1, 0, 1, 0}, dy[] = {0, -1, 0, 1};
int visited[11][11][11][11] = {0,};

void input()
{
	cin >> n >> m;
	for(int i=0; i<n; i++)
		cin >> map[i];
	for(int i=0; i<n; i++)
	{
		for(int j=0; j<m; j++)
		{
			if(map[i][j] == redBead)	start.ry = i, start.rx = j;
			if(map[i][j] == blueBead)	start.by = i, start.bx = j;
		}
	}
	start.count = 0;
}

void bfs()
{
	queue<info> q;
	q.push(start);
	visited[start.ry][start.rx][start.by][start.bx] = 1;

	while(!q.empty())
	{
		info cur = q.front(); q.pop();

		if(cur.count > 10) break;

		if(map[cur.ry][cur.rx] == hole and map[cur.by][cur.bx] != hole)
		{
			ans = cur.count;
			break;
		}

		for(int i=0; i<4; i++)
		{
			int nextRy = cur.ry, nextRx = cur.rx;
			int nextBy = cur.by, nextBx = cur.bx;

			while(1)
			{
				if(map[nextRy][nextRx] != wall and map[nextRy][nextRx] != hole)
				{
					nextRy = nextRy + dy[i];
					nextRx = nextRx + dx[i];
				}
				else
				{
					if(map[nextRy][nextRx] == wall)
					{
						nextRy = nextRy - dy[i];
						nextRx = nextRx - dx[i];
					}
					break;
				}
			}

			while(1)
			{
				if(map[nextBy][nextBx] != wall and map[nextBy][nextBx] != hole)
				{
					nextBy = nextBy + dy[i];
					nextBx = nextBx + dx[i];
				}
				else
				{
					if(map[nextBy][nextBx] == wall)
					{
						nextBy = nextBy - dy[i];
						nextBx = nextBx - dx[i];
					}
					break;
				}
			}

			if(nextRy == nextBy and nextRx == nextBx)
			{
				if(map[nextRy][nextRx] != hole)
				{
					int redDist = abs(nextRy - cur.ry) + abs(nextRx - cur.rx);
					int blueDist = abs(nextBy - cur.by) + abs(nextBx - cur.bx);

					if(blueDist > redDist)
					{
						nextBy = nextBy - dy[i];
						nextBx = nextBx - dx[i];
					}
					else
					{
						nextRy = nextRy - dy[i];
						nextRx = nextRx - dx[i];
					}
				}
			}

			if(visited[nextRy][nextRx][nextBy][nextBx] == 0)
			{
				visited[nextRy][nextRx][nextBy][nextBx] = 1;
				info next;
				next.ry = nextRy; next.rx = nextRx;
				next.by = nextBy; next.bx = nextBx;
				next.count = cur.count + 1;
				q.push(next);
			}
		}
	}
}

void solution()
{
	bfs();
	cout << ans << "\n";
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
//	freopen("input.txt", "r", stdin);
    solve();
    return 0;
}
