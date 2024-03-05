#include <iostream>
#include <queue>

using namespace std;

int n, l, temp;
priority_queue<pair<int, int>> pq;

void input()
{
	cin >> n >> l;
}

void solution()
{
	for (int i = 1; i <= n; i++)
	{
		cin >> temp;
		pq.push({ -temp, i });

		while (pq.top().second <= i - l)
		{
			pq.pop();
		}
		cout << -pq.top().first << " ";
	}
}

void solve()
{
	input();
	solution();
}

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	//freopen("input.txt", "r", stdin);
	solve();
	return 0;
}