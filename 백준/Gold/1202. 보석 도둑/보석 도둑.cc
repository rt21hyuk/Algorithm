#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

#define MAX 300001

using namespace std;

int n, k;
long long total = 0;
int bagArr[MAX];
pair<int, int> gemArr[MAX];
priority_queue<int, vector<int>, less<int>> pq;

void input()
{
    cin >> n >> k;
    for(int i=0; i<n; i++)  cin >> gemArr[i].first >> gemArr[i].second;
    for(int i=0; i<k; i++)  cin >> bagArr[i];
    sort(gemArr, gemArr+n);
    sort(bagArr, bagArr+k);
}

void solution()
{
    int idx = 0;

    for(int i=0; i<k; i++)
    {
        while(idx < n && bagArr[i] >= gemArr[idx].first)
        {
            pq.push(gemArr[idx].second);
            idx++;
        }
        if(!pq.empty())
        {
            total = total + pq.top();
            pq.pop();
        }
    }
    cout << total << "\n";
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