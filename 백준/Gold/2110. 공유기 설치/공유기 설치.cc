#include <iostream>
#include <algorithm>

# define N_MAX 200001

using namespace std;

int houseNum, routerNum;
int pos[N_MAX] = {0,};

void input()
{
    cin >> houseNum >> routerNum;
    for(int i=0; i<houseNum; i++)
    {
        cin >> pos[i];
    }
    sort(pos, pos + houseNum);
}

void binarySearch()
{
    int start = 1, end = pos[houseNum - 1] - pos[0]; // 최소 거리, 최대 거리
    int ans = -1;

    while(start <= end)
    {
        int curRouterNum = 1;
        int mid = (start + end) / 2;
        int checkPoint = pos[0];

        for(int i=1; i<houseNum; i++)
        {
            if(pos[i] - checkPoint >= mid)
            {
                curRouterNum++;
                checkPoint = pos[i];
            }
        }

        if(curRouterNum >= routerNum)
        {
            ans = max(ans, mid);
            start = mid + 1;
        }
        else
        {
            end = mid - 1;
        }
    }
    cout << ans;
}

void solution()
{
    binarySearch();
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