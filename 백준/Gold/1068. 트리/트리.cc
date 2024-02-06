#include <iostream>
#include <vector>

#define MAX 51

using namespace std;

int n, deleteNode, cnt=0, root;
vector<int> child[MAX];

void input()
{
    cin >> n;
    for(int i=0; i<n; i++)
    {
        int temp;
        cin >> temp;
        if(temp == -1)	root = i;
        else	child[temp].push_back(i);
    }
    cin >> deleteNode;
}

int dfs(int node)
{
	if(node == deleteNode) return -1;
	if(child[node].size() == 0)
	{
		cnt++;
		return 0;
	}
	for(int i=0; i<child[node].size(); i++)
	{
		int check = dfs(child[node][i]);
		if(check == -1 && child[node].size() == 1) cnt++;
	}
	return 0;
}

void solution()
{
	dfs(root);
	cout << cnt;
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
