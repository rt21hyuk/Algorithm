#include <iostream>
#include <vector>
#include <queue>

using namespace std;

#define M_MAX 100001

int n, m;
int state[M_MAX];
queue<int> q;
vector<int> vec[M_MAX];

void input() 
{
	cin >> n >> m;
	for (int i = 1; i <= m; i++)
	{
		int n1, n2;
		cin >> n1 >> n2;
		vec[n1].push_back(n2);
		state[n2]++;
	}
}

void solution() 
{
	for (int i = 1; i <= n; i++)
	{
		if (state[i] == 0)
		{
			state[i] = -1;
			q.push(i);
		}
	}

	while (!q.empty())
	{
		int idx = q.front();
		cout << idx << " ";
		q.pop();

		for (int i = 0; i < vec[idx].size(); i++)
		{
			state[vec[idx][i]]--;

			if (state[vec[idx][i]] == 0)
			{
				state[vec[idx][i]] = -1;
				q.push(vec[idx][i]);
			}
		}
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