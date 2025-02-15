#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int N, H;
vector<int> obsUp, obsDown;

int binarySearchDown(const vector<int>& obsList, int x) {
    int left = 0, right = N / 2 - 1;
    while (left <= right) {
        int mid = (left + right) / 2;
        if (obsList[mid] <= x) {
            left = mid + 1;
        }
        else {
            right = mid - 1;
        }
    }
    return N / 2 - left;
}

void input() {
    cin >> N >> H;
    for (int i = 0; i < N; ++i) {
        int barrier;
        cin >> barrier;
        if (i % 2 == 0) {
            obsDown.push_back(barrier);
        }
        else {
            obsUp.push_back(barrier);
        }
    }
    sort(obsUp.begin(), obsUp.end());
    sort(obsDown.begin(), obsDown.end());
}

void solution() {
    int obsMinNum = N;
    int obsMinCount = 0;

    for (int h = 1; h <= H; ++h) {
        int obsUpNum = binarySearchDown(obsUp, H - h);
        int obsDownNum = binarySearchDown(obsDown, h - 1);
        int obsTotalNum = obsUpNum + obsDownNum;

        if (obsTotalNum < obsMinNum) {
            obsMinNum = obsTotalNum;
            obsMinCount = 1;
        }
        else if (obsTotalNum == obsMinNum) {
            obsMinCount++;
        }
    }

    cout << obsMinNum << " " << obsMinCount << endl;
}

void solve() {
    input();
    solution();
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    // freopen("input.txt", "r", stdin);
    solve();
    return 0;
}
