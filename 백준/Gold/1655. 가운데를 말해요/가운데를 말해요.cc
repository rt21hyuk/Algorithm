#include <iostream>
#include <queue>
#include <vector>

#define MAX 100001

using namespace std;

int n;
int numArr[MAX];
priority_queue<int, vector<int>, less<int>> maxPq;      // desc
priority_queue<int, vector<int>, greater<int>> minPq;   // asc   

void input()
{
    cin >> n;
    for(int i=0; i<n; i++)
        cin >> numArr[i];;
}

void solution()
{
    for(int i=0; i<n; i++)
    {
        if(maxPq.size() == minPq.size())    maxPq.push(numArr[i]);
        else    minPq.push(numArr[i]);

        if(!maxPq.empty() && !minPq.empty())
        {
            if(maxPq.top() > minPq.top())
            {
                int a = maxPq.top(); maxPq.pop();
                int b = minPq.top(); minPq.pop();

                maxPq.push(b);
                minPq.push(a);
            }
        }
        cout << maxPq.top() << "\n";
    }
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