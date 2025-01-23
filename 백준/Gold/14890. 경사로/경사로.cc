#include <iostream>
#include <vector>

using namespace std;

int n, l, answer = 0;
int areas[101][101];

void input() {
    cin >> n >> l;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> areas[i][j];
        }
    }
}

bool canPlaceSlope(vector<int>& road) {
    int visited[101] = {0};
    for (int i = 0; i < n - 1; i++) {
        if (road[i] == road[i + 1]) continue; // 높이가 같으면 넘어감
        if (road[i] + 1 == road[i + 1]) { // 오르막길
            if (i - l + 1 < 0) return false; // 경사로 설치 공간 부족
            for (int j = i; j > i - l; j--) {
                if (road[j] != road[i] || visited[j]) return false;
                visited[j] = 1;
            }
        } else if (road[i] - 1 == road[i + 1]) { // 내리막길
            if (i + l >= n) return false; // 경사로 설치 공간 부족
            for (int j = i + 1; j <= i + l; j++) {
                if (road[j] != road[i + 1] || visited[j]) return false;
                visited[j] = 1;
            }
        } else {
            return false; // 높이 차이가 1 이상인 경우
        }
    }
    return true;
}

void solution() {
    // 행 검사
    for (int i = 0; i < n; i++) {
        vector<int> road(n);
        for (int j = 0; j < n; j++) {
            road[j] = areas[i][j];
        }
        if (canPlaceSlope(road)) answer++;
    }

    // 열 검사
    for (int j = 0; j < n; j++) {
        vector<int> road(n);
        for (int i = 0; i < n; i++) {
            road[i] = areas[i][j];
        }
        if (canPlaceSlope(road)) answer++;
    }

    cout << answer;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    input();
    solution();
    return 0;
}
