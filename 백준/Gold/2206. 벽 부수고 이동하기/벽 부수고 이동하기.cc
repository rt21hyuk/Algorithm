#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <tuple>

#define MAX 1001
#define Blank 0
#define Wall 1

int R, C, Min_Dist = INT32_MAX;
int Map[MAX][MAX];
int Visited[MAX][MAX][2];

int dr[] = {-1, 0, 1, 0};
int dc[] = {0, -1, 0, 1};

int BFS()
{
	std::queue<std::tuple<int, int, int>> q;
	q.push({0, 0, 1});
	Visited[0][0][1] = 1;

	while(!q.empty())
	{
		int current_r = std::get<0>(q.front()), current_c = std::get<1>(q.front()), block = std::get<2>(q.front());
		q.pop();

		if(current_r == R-1 && current_c == C-1){
			return Visited[current_r][current_c][block];
		}

		for(int i=0; i<4; i++)
		{
			int nr = current_r + dr[i], nc = current_c + dc[i];

			if(nr >= 0 && nc >= 0 && nr < R && nc < C)
			{
				if(Map[nr][nc] == Wall && block)
				{
					q.push({nr, nc, 0});
					Visited[nr][nc][block - 1] = Visited[current_r][current_c][block] + 1;
				}
				else if(Map[nr][nc] == Blank && Visited[nr][nc][block] == 0)
				{
					q.push({nr, nc, block});
					Visited[nr][nc][block] = Visited[current_r][current_c][block] + 1;
				}
			}
		}
	}

	return -1;
}

void INPUT()
{
	std::cin >> R >> C;

	for(int i=0; i<R; i++)
	{
		std::string Inp;
		std::cin >> Inp;

		for(int j=0; j<C; j++)
		{
			int Tmp = Inp[j] - '0';
			Map[i][j] = Tmp;
		}
	}
}

void Solution()
{
	Min_Dist = BFS();
	std::cout << Min_Dist;
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

//	freopen("Input.txt", "r", stdin);
	Solve();

	return 0;
}


