#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>

using namespace std;

#define NMAX 32001
#define MMAX 100001

int n, m;
int entry[NMAX];
vector<int> info[NMAX];

void input()
{
    cin >> n >> m;
    for(int i=0; i<m; i++)
    {
        int n1, n2; cin >> n1 >> n2;
        info[n1].push_back(n2);
        entry[n2]++;
    }
}

void solution()
{
    priority_queue<int> pq;

    for(int i=1; i<=n; i++)
        if(entry[i] == 0) pq.push(-i);
        
    while(pq.empty() == 0)
    {
        int cur = -pq.top();
        pq.pop();

        cout << cur << " ";

        for(int i=0; i<info[cur].size(); i++)
        {
            int next = info[cur][i];
            entry[next]--;

            if(entry[next] == 0) pq.push(-next);
        }
    }
    cout << "\n";
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