#include <iostream>
#include <vector>
#include <algorithm>

#define MAX 1000001

using namespace std;

int n;
int numArr[MAX] = {0,};
vector<int> v;

void input()
{
    cin >> n;
    for(int i=1; i<=n; i++) cin >> numArr[i];
}

void solution()
{
    for(int i=1; i<=n; i++)
    {
        if(v.size() == 0 || v[v.size()-1] < numArr[i]) v.push_back(numArr[i]);
        else
        {
            int pos = lower_bound(v.begin(), v.end(), numArr[i]) - v.begin();
            v[pos] = numArr[i];
        }
    }
    cout << v.size() << "\n";
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