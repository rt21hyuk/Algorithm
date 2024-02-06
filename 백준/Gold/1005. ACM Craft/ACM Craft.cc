#include <iostream>
#include <vector>
#include <queue>
#include <cstring>

#define MAX 1001

using namespace std;

int t, n, k, w;
int constructionTime[MAX];
int resultTime[MAX];
int entry[MAX];
vector<int> orderOfConstruction[MAX];

void input()
{
    cin >> n >> k;
    for(int i=1; i<=n; i++)
        cin >> constructionTime[i];
    for(int i=1; i<=k; i++)
    {
        int temp1, temp2; cin >> temp1 >> temp2;
        orderOfConstruction[temp1].push_back(temp2);
        entry[temp2]++;
    }
    cin >> w;
}

void solution()
{
    queue<int> q;
    for(int i=1; i<=n; i++)
    {
        if(entry[i] == 0)
        {
            q.push(i);
            resultTime[i] = constructionTime[i];
        }
    }
    while(!q.empty())
    {
        int cur = q.front();
        q.pop();

        for(int i=0; i<orderOfConstruction[cur].size(); i++)
        {
            int next = orderOfConstruction[cur][i];
            resultTime[next] = max(resultTime[next], resultTime[cur] + constructionTime[next]);
            entry[next]--;

            if(entry[next] == 0) q.push(next);
        }
    }
    cout << resultTime[w] << "\n";
}

void init()
{
    memset(constructionTime, 0, sizeof(constructionTime));
    memset(resultTime, 0, sizeof(resultTime));
    memset(entry, 0, sizeof(entry));
    for(int i=0; i<n+1; i++) orderOfConstruction[i].clear();
}

void solve()
{
    cin >> t;
    for(int i=0; i<t; i++)
    {
        input();
        solution();
        init();
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