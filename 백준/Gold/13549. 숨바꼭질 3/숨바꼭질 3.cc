#include <iostream>
#include <vector>
#include <queue>

#define MaxValue 100001

using namespace std;

int startPoint, targetPoint;
bool visited[MaxValue] = {false,};

void input()
{
    cin >> startPoint >> targetPoint;
}

void BFS(int cur, int cnt)
{
    queue<pair<int, int>> q;
    q.push({cur, cnt});
    visited[cur] = true;

    while(!q.empty())
    {
        int curPoint = q.front().first, curCnt = q.front().second;
        q.pop();

        if(curPoint == targetPoint)
        {
            cout << curCnt;
            return;
        }
        if(curPoint * 2 < MaxValue && visited[curPoint * 2] == false)
        {
            q.push({curPoint*2, curCnt});
            visited[curPoint*2] = true;
        }
        if(curPoint - 1 >= 0&& visited[curPoint - 1] == false)
        {
            q.push({curPoint-1, curCnt+1});
            visited[curPoint-1] = true;
        }
        if(curPoint + 1 < MaxValue&& visited[curPoint + 1] == false)
        {
            q.push({curPoint+1, curCnt+1});
            visited[curPoint+1] = true;
        }
    }
}

void solution()
{
    BFS(startPoint, 0);    
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