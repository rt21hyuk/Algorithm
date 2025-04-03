#include <iostream>
#include <vector>

using namespace std;

int h, w, answer = 0;
vector<int> blocks;

void input() {
    cin >> h >> w;
    blocks.resize(w);
    for (int i = 0; i < w; i++)
        cin >> blocks[i];
}

void solution() {
    for (int i = 1; i < w-1; i++) {
        int left = 0, right = 0;
        for (int l = i-1; l >= 0; l--) {
            left = max(left, blocks[l]);
        }
        for (int r = i+1; r < w; r++) {
            right = max(right, blocks[r]);
        }
        if (min(left, right) > blocks[i]) answer = answer + min(left, right) - blocks[i];
    }
    cout << answer << "\n";
}

void solve() {
    input();
    solution();
}

int main() {
    cin.tie(NULL);
    ios::sync_with_stdio(false);
    //freopen("input.txt", "r", stdin);
    solve();
    return 0;
}