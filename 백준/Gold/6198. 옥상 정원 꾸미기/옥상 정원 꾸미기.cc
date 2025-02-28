#include <iostream>
#include <vector>
#include <stack>

using namespace std;

int n;
long long answer = 0;
vector<int> buildings;

void input() {
    cin >> n;
    buildings.resize(n);
    for (int i = 0; i < n; i++) {
        cin >> buildings[i];
    }
}

void solution() {
    stack<int> stk;
    for (int cur = 0; cur < n; cur++) {
        int curH = buildings[cur];
        while (!stk.empty() && stk.top() <= curH) {
            stk.pop();
        }
        answer += stk.size();
        stk.push(curH);
    }
    cout << answer;
}

void solve() {
    input();
    solution();
}

int main(int argc, char* argv[]) {
    std::cin.tie(NULL);
    std::ios::sync_with_stdio(false);
    //freopen("input.txt", "r", stdin);
    solve();
    return 0;
}
