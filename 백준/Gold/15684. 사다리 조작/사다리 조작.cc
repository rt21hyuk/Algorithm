#include <iostream>
#include <climits>

using namespace std;

int n, m, h, answer = INT_MAX;
int map[11][30];
bool visited[11][30];

void input() {
    cin >> n >> m >> h;
    for(int i=0; i<m; i++){
        int a, b;
        cin >> a >> b;
        visited[b][a] = true; // b와 b+1의 세로선이 a번 가로선에 의해 연결됨됨
    }
}

bool ladderGame() {
    for(int i=1; i<=n; i++) {
        int cur = i;
        for(int j=1; j<=h; j++) {
            if(visited[cur][j] == true) cur = cur + 1;
            else if(visited[cur-1][j] == true) cur = cur - 1;
        }
        if(cur != i) return false;
    }
    return true;
}

void selectLine(int idx, int cnt) {
    if(cnt >= 4) return;
    if(ladderGame() == true) {
        answer = min(answer, cnt);
        return;
    }
    for(int i=idx; i<=h; i++) {
        for(int j=1; j<n; j++) {
            if(visited[j][i] == true) continue;
            if(visited[j-1][i] == true) continue;
            if(visited[j+1][i] == true) continue;
            visited[j][i] = true;
            selectLine(i, cnt+1);
            visited[j][i] = false;
        }
    }
}

void solution() {
    selectLine(1, 0);
    if(answer == INT_MAX) cout << -1;
    else cout << answer;
}

void solve() {
    input();
    solution();
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    solve();
    return 0;
}