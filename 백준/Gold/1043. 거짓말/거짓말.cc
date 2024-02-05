#include <iostream>
#include <vector>

#define MAX 51

using namespace std;

int n, m, answer;
int parent[MAX];
vector<int> knowTruth;
vector<int> party[MAX];

void input()
{
    cin >> n >> m;
    int numOfPeople; cin >> numOfPeople;
    for(int i=0; i<numOfPeople; i++)
    {
        int temp; cin >> temp;
        knowTruth.push_back(temp);
    }
    for(int i=0; i<m; i++)
    {
        int peopleNum; cin >> peopleNum;
        for(int j=0; j<peopleNum; j++)
        {
            int temp; cin >> temp;
            party[i].push_back(temp);
        }
    }
    answer = m;
}

int findParent(int a)
{
    if(parent[a] == a) return a;
    return parent[a] = findParent(parent[a]);
}

void unionParent(int a, int b)
{
    a = findParent(a);
    b = findParent(b);
    parent[b] = a;
}

bool isSameParent(int a, int b)
{
    a = findParent(a);
    b = findParent(b);
    if(a == b) return true;
    return false;
}

void solution()
{
    for(int i=1; i<=n; i++) parent[i] = i;
    for(int i=0; i<m; i++)
    {
        int n1 = party[i][0];
        for(int j=1; j<party[i].size(); j++)
        {
            int n2 = party[i][j];
            unionParent(n1, n2);
        }
    }
    for(int i=0; i<m; i++)
    {
        bool canLie = true;
        for(int j=0; j<party[i].size(); j++)
        {
            if(canLie == false) break;
            int n1 = party[i][j];
            for(int k=0; k<knowTruth.size(); k++)
            {
                int n2 = knowTruth[k];
                if(isSameParent(n1, n2) == true)
                {
                    canLie = false;
                    break;
                }
            }
        }
        if(canLie == false) answer--;
    }
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