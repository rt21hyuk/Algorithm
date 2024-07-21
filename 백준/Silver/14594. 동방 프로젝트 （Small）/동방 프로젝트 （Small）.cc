#include <iostream>

using namespace std;

int main() {
    int n, m;
    cin >> n >> m; // n은 벽을 설치할 위치의 개수, m은 설치할 벽의 개수

    bool wall[n-1]; // 벽의 상태를 나타내는 배열, 벽의 개수는 n-1개
    
    // 벽 배열 모두 true로 초기화
    for (int i = 0; i < n - 1; i++) {
        wall[i] = true;
    }
    
    // m개의 벽 설치
    for (int i = 0; i < m; i++) {
        int x, y;
        cin >> x >> y;
        
        // 벽을 설치할 구간 [x, y-1]을 false로 설정
        for (int j = x - 1; j < y - 1; j++) {
            wall[j] = false;
        }
    }
    
    int cnt = 0;
    // 남아있는 true의 개수 세기
    for (int i = 0; i < n - 1; i++) {
        if (wall[i] == true)
            cnt++;
    }
    
    // 남아있는 true의 개수에 1을 더한 값을 출력
    cout << cnt + 1;
    
    return 0;
}
