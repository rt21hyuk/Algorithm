#include <iostream>
#include <vector>

using namespace std;

int N;
int edge[101][101] = {0, };

void input()
{
    cin >> N;
    for(int i=0; i<N; i++)
    {
        for(int j=0; j<N; j++)
        {
            cin >> edge[i][j];
        }
    }
}

void floydwarshall()
{
    for(int k=0; k<N; k++)
    {
        for(int i=0; i<N; i++)
        {
            for(int j=0; j<N; j++)
            {
                if(edge[i][k] == 1 && edge[k][j] == 1)
                {
                    edge[i][j] = 1;
                }
            }
        }
    }

    for(int i=0; i<N; i++)
    {
        for(int j=0; j<N; j++)
        {
            cout << edge[i][j] << " ";
        }
        cout << "\n";
    }
}

void solution()
{
    floydwarshall();
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