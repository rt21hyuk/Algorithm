#include <iostream>
#include <algorithm>
#include <vector>

#define Blank 0
#define House 1
#define Chicken 2
#define MAX 51

struct Point {
    int x, y;
};

int N, M, minVal = INT32_MAX;
int chickenCnt = 0;
int cityMap[MAX][MAX];
int dist[MAX][MAX];
std::vector<Point> chickenLocations;

int minValue(int a, int b) {
    return (a < b) ? a : b;
}

void initDist() {
    for (int j = 0; j < N; j++) {
        for (int i = 0; i < N; i++) {
            if (dist[j][i] != INT32_MAX) {
                dist[j][i] = INT32_MAX;
            }
        }
    }
}

void calTotalDist() {
    int sum = 0;

    for (int j = 0; j < N; j++) {
        for (int i = 0; i < N; i++) {
            if (dist[j][i] != INT32_MAX) {
                sum += dist[j][i];
            }
        }
    }

    minVal = minValue(minVal, sum);
    initDist();
}

void calDist(int x, int y) {
    for (int j = 0; j < N; j++) {
        for (int i = 0; i < N; i++) {
            if (cityMap[j][i] == House) {
                dist[j][i] = minValue(abs(j - y) + abs(i - x), dist[j][i]);
            }
        }
    }
}

void input() {
    std::cin >> N >> M;

    for (int j = 0; j < N; j++) {
        for (int i = 0; i < N; i++) {
            std::cin >> cityMap[j][i];

            if (cityMap[j][i] == Chicken) {
                chickenCnt++;
                chickenLocations.push_back({ i, j });
            }

            dist[j][i] = INT32_MAX;
        }
    }
}

void solution() {
    int n = chickenCnt, k = M;

    std::vector<int> indices;
    std::vector<int> selectionMask;

    for (int i = 0; i < n; i++) {
        indices.push_back(i);
    }

    for (int i = 0; i < n - k; i++) {
        selectionMask.push_back(0);
    }

    for (int i = 0; i < k; i++) {
        selectionMask.push_back(1);
    }


    do {
        for (int i = 0; i < selectionMask.size(); i++) {
            if (selectionMask[i] == 1) {
                calDist(chickenLocations[i].x, chickenLocations[i].y);
            }
        }
        calTotalDist();
    } while (std::next_permutation(selectionMask.begin(), selectionMask.end()));

    std::cout << minVal;
}

void solve() {
    input();
    solution();
}

int main(int argc, char* argv[]) {
    std::cin.tie(NULL);
    std::ios::sync_with_stdio(false);

    // freopen("Input.txt", "r", stdin);
    solve();

    return 0;
}
