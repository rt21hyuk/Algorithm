#include <iostream>
#include <queue>
#include <algorithm>

using namespace std;

int N, num;
int Map[65][65];

void Input()
{
	std::cin >> N;
	for(int i=0; i<N; i++)
	{
		string str;
		std::cin >> str;
		for(int j=0; j<N; j++)
		{
			Map[i][j] = str[j]-'0';
		}
	}
}

void DFS(int x, int y, int Size)
{
	if(Size == 1)
	{
		std::cout << Map[y][x];
		return;
	}

	bool OnlyZero = true, OnlyOne = true;
	for(int i=y; i<y+Size; i++)
	{
		for(int j=x; j<x+Size; j++)
		{
			if(Map[i][j] == 0) OnlyOne = false;
			if(Map[i][j] == 1) OnlyZero = false;
		}
	}

	if(OnlyZero == true)
	{
		std::cout << 0;
		return;
	}
	if(OnlyOne == true)
	{
		std::cout << 1;
		return;
	}
	std::cout << "(";
	DFS(x, y, Size/2);
	DFS(x + Size/2, y, Size/2);
	DFS(x, y + Size/2, Size/2);
	DFS(x + Size/2, y + Size/2, Size/2);
	std::cout << ")";
}

void Solution()
{
	DFS(0,0,N);
}

void Solve()
{
	Input();
	Solution();
}

int main(int argc, char argv[])
{
	std::cin.tie(NULL);
	std::ios::sync_with_stdio(false);
//	freopen("input.txt", "r", stdin);

	Solve();

	return 0;
}

