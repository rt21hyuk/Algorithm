#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>

using namespace std;

int N, target;
vector<int> numArr;

void input() {
    cin >> N >> target;
    numArr.resize(N);
    for (int i = 0; i < N; ++i) {
        cin >> numArr[i];
    }
}

void solution() {
    int left = 0, right = 0, sum = 0, minLen = INT_MAX;

    while (true) {
        if (sum >= target) {
            minLen = min(minLen, right - left);
            sum -= numArr[left];
            ++left;
        } else if (right == N) {
            break;
        } else if (sum < target) {
            sum += numArr[right];
            ++right;
        }
    }

    if (minLen == INT_MAX) {
        cout << 0 << endl;
    } else {
        cout << minLen << endl;
    }
}

void solve() {
    input();
    solution();
}

int main() {
    cin.tie(NULL);
    ios::sync_with_stdio(false);
    // freopen("input.txt", "r", stdin);
    solve();
    return 0;
}