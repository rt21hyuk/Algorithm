#include<iostream>
#include<stack>

using namespace std;

int n, height;
stack<pair<int, int>> stk;

void input() {
    cin >> n;
}

void solution() {
    for(int i=0; i<n; i++) {
        cin >> height;

        while(!stk.empty()) {
            if(height <= stk.top().second){
                cout << stk.top().first << " ";
                break;
            }
            stk.pop();
        }
        if(stk.empty()) {
            cout << 0 << " ";
        }
        stk.push({i+1, height});
    }
}

void solve() {
    input();
    solution();
}

int main(int argc, char** argv)
{
    cin.tie(NULL);
    ios_base::sync_with_stdio(false);
    solve();
    return 0;
}