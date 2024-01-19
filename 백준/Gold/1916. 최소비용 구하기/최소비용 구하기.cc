#include <iostream>
#include <queue>
#include <climits>

using namespace std;

#define N_MAX 1001
#define M_MAX 100001

int n, m;
int start, dest;
int minCost = INT_MAX;
int dist[N_MAX];
std::vector<std::pair<int, int>> bus[N_MAX];

void input()
{
    std::cin >> n >> m;
    for(int i=0; i<m; i++)
    {
        int s, d, c;
        std::cin >> s >> d >> c;
        bus[s].push_back({d, c});
    }
    std::cin >> start >> dest;

    for(int i=1; i<=n; i++)
    {
        dist[i] = INT_MAX;
    }
}

void Dijkstra()
{
    std::priority_queue<std::pair<int, int>> pq;
    pq.push({0, start});
    dist[start] = 0;

    while(!pq.empty())
    {
        int cost = -pq.top().first;
        int cur = pq.top().second;
        pq.pop();

        if(dist[cur] < cost)
            continue;
        for(int i=0; i<bus[cur].size(); i++)
        {
            int next = bus[cur][i].first;
            int ncost = cost + bus[cur][i].second;

            if(dist[next] > ncost)
            {
                dist[next] = ncost;
                pq.push({-ncost, next});
            }
        }
    }
    std::cout << dist[dest];
}

void solution()
{
    Dijkstra();
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