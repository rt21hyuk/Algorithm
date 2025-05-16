#include <iostream>
#include <vector>
using namespace std;

int R, C, T;
vector<vector<int>> maps, nextMaps;
vector<int> airPurifier;
int dr[4] = {-1, 0, 1, 0};
int dc[4] = {0, 1, 0, -1};

void diffusion() {
    nextMaps.assign(R, vector<int>(C, 0));
    for (int r = 0; r < R; r++) {
        for (int c = 0; c < C; c++) {
            if (maps[r][c] > 0) {
                int dust = maps[r][c], cnt = 0;
                for (int d = 0; d < 4; d++) {
                    int nr = r + dr[d], nc = c + dc[d];
                    if (nr < 0 || nc < 0 || nr >= R || nc >= C) continue;
                    if (maps[nr][nc] == -1) continue;
                    nextMaps[nr][nc] += dust / 5;
                    cnt++;
                }
                nextMaps[r][c] += dust - (dust / 5) * cnt;
            }
        }
    }
    for (int r = 0; r < R; r++)
        for (int c = 0; c < C; c++)
            if (maps[r][c] == -1)
                nextMaps[r][c] = -1;

    maps = nextMaps;
}

void operateAirPurifier() {
    int top = airPurifier[0], bottom = airPurifier[1];

    // 위쪽 반시계 방향
    for (int r = top - 1; r > 0; r--) maps[r][0] = maps[r - 1][0];
    for (int c = 0; c < C - 1; c++) maps[0][c] = maps[0][c + 1];
    for (int r = 0; r < top; r++) maps[r][C - 1] = maps[r + 1][C - 1];
    for (int c = C - 1; c > 1; c--) maps[top][c] = maps[top][c - 1];
    maps[top][1] = 0;

    // 아래쪽 시계 방향
    for (int r = bottom + 1; r < R - 1; r++) maps[r][0] = maps[r + 1][0];
    for (int c = 0; c < C - 1; c++) maps[R - 1][c] = maps[R - 1][c + 1];
    for (int r = R - 1; r > bottom; r--) maps[r][C - 1] = maps[r - 1][C - 1];
    for (int c = C - 1; c > 1; c--) maps[bottom][c] = maps[bottom][c - 1];
    maps[bottom][1] = 0;
}

int getFineDust() {
    int sum = 0;
    for (int r = 0; r < R; r++)
        for (int c = 0; c < C; c++)
            if (maps[r][c] > 0)
                sum += maps[r][c];
    return sum;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> R >> C >> T;
    maps.resize(R, vector<int>(C));
    for (int r = 0; r < R; r++) {
        for (int c = 0; c < C; c++) {
            cin >> maps[r][c];
            if (maps[r][c] == -1) {
                airPurifier.push_back(r);
            }
        }
    }

    while (T--) {
        diffusion();
        operateAirPurifier();
    }

    cout << getFineDust() << '\n';
    return 0;
}
