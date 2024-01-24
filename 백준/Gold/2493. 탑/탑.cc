#include <iostream>
#include <vector>
#include <stack>

using namespace std;

int N;
vector<int> tower;
vector<int> answer;
stack<pair<int, int>> stk;

void input()
{
    cin >> N;
    tower.resize(N);
    answer.resize(N);
    for(int i=0; i<N; i++)
        cin >> tower[i];
}

void solution()
{
    for(int i=0; i<N; i++)
    {
        if(stk.empty())
        {
            answer[i] = 0;
        }
        while(!stk.empty())
        {
            int idx = stk.top().first;
            int height = stk.top().second;

            if(height >= tower[i])
            {
                answer[i] = idx + 1;
                break;
            }
            else 
            {
                stk.pop();
                
                if(stk.empty() == true)
                {
                    answer[i] = 0;
                }
            }
        }
        stk.push({i, tower[i]});
    }
}

void print()
{
    cout << answer[0];
    for(int i=1; i<N; i++)
        cout << " " << answer[i];
}

void solve()
{
    input();
    solution();
    print();
}

int main()
{
    std::cin.tie(NULL);
	std::ios::sync_with_stdio(false);
	// freopen("input.txt", "r", stdin);
    solve();
    return 0;
}