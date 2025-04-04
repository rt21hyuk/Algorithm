#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int n;
int cost[1001];
vector<pair<int, int>> assignments;

bool cmp(const pair<int, int>& a, const pair<int, int>& b) {
    if (a.second == b.second) { // 과제 점수가 같은 경우, 마감일이 짧은 것부터 오름차순 정렬
        return a.first < b.first;
    }
    return a.second > b.second; // 과제 점수 기준으로 내림차순 정렬
}

void input() {
    cin >> n; assignments.reserve(n);
    for (int i = 0; i < n; i++) {
        int d, w;
        cin >> d >> w;
        assignments.push_back({ d, w });
    }
    sort(assignments.begin(), assignments.end(), cmp);
}

void solution() {
    int res = 0;
    for (int i = 0; i < n; i++) {
        for (int j = assignments[i].first; j > 0; j--) {
            if (!cost[j]) {
                cost[j] = assignments[i].second;    // 과제 점수가 높은 것들부터 해서 cost라는 배열에 넣음
                res += assignments[i].second;       // 예를 들어 , 마감일이 4이고 점수가 50이라면, 인덱스 4를 가지고 있는 cost라는 배열에 50을 저장한다. 
                break;                              // 이후에 마감일 4이고 점수가 40이 들어왔을 경우 마감일 1~3 일을 차례대로 훑어보면서 빈자리에 넣어준다. 
                                                    // 만약 빈자리가 없다면, 이전에 더 높은 점수를 가지는 과제들이 해당 자리를 차지 했다고 생각
            }
        }
    }
    cout << res;
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