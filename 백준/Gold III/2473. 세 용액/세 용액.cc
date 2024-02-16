#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

#define NMAX 5001

int n;
long long minSumVal = 30000000001;
long long answer[3];
long long arr[NMAX];

void input()
{
    cin >> n;
    for(int i=0; i<n; i++)  cin >> arr[i];
    sort(arr, arr+n);
}

int binarySearch(int idx)
{
    int left = idx+1, right = n-1;

    while(left < right)
    {
        long long sumVal = arr[left] + arr[right] + arr[idx];

        if(abs(sumVal) < minSumVal)
        {
            minSumVal = abs(sumVal);
            answer[0] = arr[left], answer[1] = arr[right], answer[2] = arr[idx];
            sort(answer, answer+3);
            if(sumVal == 0)
                return 1;
        }

        if(sumVal < 0)
            left = left + 1;
        else
            right = right - 1;
    }

    return 0;
}

void solution()
{
    for(int i=0; i<n-2; i++)
    {
        if(binarySearch(i) == 1)
            break;
    }
    cout << answer[0] << " " << answer[1] << " " << answer[2];
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