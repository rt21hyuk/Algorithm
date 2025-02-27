#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int target;
vector<long long> dp;

void input() {
    cin >> target;
}

void solution() {
    queue<long long> q;
    for (int i = 0; i <= 9; i++) {
        q.push(i);
        dp.push_back(i);
    }
    while (!q.empty()) {
        long long num = q.front();
        int last = num % 10;
        q.pop();
        
        for (int i = 0; i < last; i++) {
            long long newNum = num * 10 + i;
            q.push(newNum);
            dp.push_back(newNum);
        }
    }
    if (target >= dp.size()) cout << -1;
    else cout << dp[target];
}

void solve() {
    input();
    solution();
}

int main(int argc, char* argv[]) {
    std::cin.tie(NULL);
    std::ios::sync_with_stdio(false);
    //freopen("Input.txt", "r", stdin);
    solve();
    return 0;
}
