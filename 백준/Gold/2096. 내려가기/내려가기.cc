#include <iostream>

using namespace std;

int n;
int curDp[3], maxDp[3], minDp[3];

void input()
{
    cin >> n;
    for(int i=0; i<3; i++)
    {
        cin >> curDp[i];
        maxDp[i] = curDp[i];
        minDp[i] = curDp[i];
    }   
}

void solution()
{
    int n1, n2, n3;

    for(int i=1; i<n; i++)
    {
        cin >> n1 >> n2 >> n3;
        curDp[0] = max(maxDp[0], maxDp[1]) + n1;
        curDp[1] = max(maxDp[0], max(maxDp[1], maxDp[2])) + n2;
        curDp[2] = max(maxDp[1], maxDp[2]) + n3;
        maxDp[0] = curDp[0]; maxDp[1] = curDp[1]; maxDp[2] = curDp[2];

        curDp[0] = min(minDp[0], minDp[1]) + n1;
        curDp[1] = min(minDp[0], min(minDp[1], minDp[2])) + n2;
        curDp[2] = min(minDp[1], minDp[2]) + n3;
        minDp[0] = curDp[0]; minDp[1] = curDp[1]; minDp[2] = curDp[2];
    }

    cout << max(maxDp[0], max(maxDp[1], maxDp[2])) << " " << min(minDp[0], min(minDp[1], minDp[2]));
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