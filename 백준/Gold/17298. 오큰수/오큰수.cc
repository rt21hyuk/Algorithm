#include <iostream>
#include <stack>

#define MAX_N 1000000

using namespace std;

int N;
int arr[MAX_N] = {0,};
int NGE[MAX_N] = {0,};
std::stack<int> stk;

void input()
{
    std::cin >> N;
    for(int i=0; i<N; i++)
    {
        std::cin >> arr[i];
    }
}

void printNGE()
{
    for(int i=0; i<N-1; i++)
        std::cout << NGE[i] << " ";
    std::cout << NGE[N-1];
}

void solution()
{
    for(int i=N-1; i>=0; i--)
    {
        while(1)
        {
            if(stk.empty())
            {
                NGE[i] = -1;
                break;
            }
            else if(stk.top() > arr[i])
            {
                NGE[i] = stk.top();
                break;
            }
            else if(stk.top() <= arr[i])
            {
                stk.pop();
            }
        }
        stk.push(arr[i]);
    }
    printNGE();
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