#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int n, m, k;
int A[11][11];          // 겨울에 추가되는 영양분 정보
int nutrients[11][11];  // 현재 각 칸의 영양분
vector<int> trees[11][11];  // 각 칸에 있는 나무들의 나이 (오름차순 유지)

int dr[8] = {-1,-1,-1,0,0,1,1,1};
int dc[8] = {-1,0,1,-1,1,-1,0,1};

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    cin >> n >> m >> k;
    
    // A배열 입력 및 초기 영양분 5로 초기화
    for (int i = 1; i <= n; i++){
        for (int j = 1; j <= n; j++){
            cin >> A[i][j];
            nutrients[i][j] = 5;
        }
    }
    
    // 초기 나무 정보 입력 (1-indexed)
    for (int i = 0; i < m; i++){
        int r, c, age;
        cin >> r >> c >> age;
        trees[r][c].push_back(age);
    }
    
    // 각 칸의 나무를 나이순으로 정렬
    for (int i = 1; i <= n; i++){
        for (int j = 1; j <= n; j++){
            if (!trees[i][j].empty()){
                sort(trees[i][j].begin(), trees[i][j].end());
            }
        }
    }
    
    // k년 동안 반복
    while(k--){
        // 봄 & 여름
        for (int i = 1; i <= n; i++){
            for (int j = 1; j <= n; j++){
                if(trees[i][j].empty()) continue;
                vector<int> alive;
                int deadNutrition = 0;
                // 나이가 낮은 나무부터 영양분 섭취
                for (int age : trees[i][j]){
                    if(nutrients[i][j] >= age){
                        nutrients[i][j] -= age;
                        alive.push_back(age + 1);
                    } else {
                        deadNutrition += age / 2;
                    }
                }
                // 죽은 나무가 준 영양분을 즉시 반영
                nutrients[i][j] += deadNutrition;
                trees[i][j] = alive;
            }
        }
        
        // 가을 (번식)
        for (int i = 1; i <= n; i++){
            for (int j = 1; j <= n; j++){
                if(trees[i][j].empty()) continue;
                int reproduceCount = 0;
                // 번식 가능한 나무 수 세기 (나이가 5의 배수)
                for (int age : trees[i][j]){
                    if(age % 5 == 0)
                        reproduceCount++;
                }
                if(reproduceCount > 0){
                    for (int d = 0; d < 8; d++){
                        int ni = i + dr[d], nj = j + dc[d];
                        if(ni < 1 || ni > n || nj < 1 || nj > n)
                            continue;
                        // 번식하는 나무만큼 새로운 나무(나이 1)를 추가
                        for (int cnt = 0; cnt < reproduceCount; cnt++){
                            trees[ni][nj].push_back(1);
                        }
                    }
                }
            }
        }
        
        // 겨울 : 각 칸에 추가 영양분 공급
        for (int i = 1; i <= n; i++){
            for (int j = 1; j <= n; j++){
                nutrients[i][j] += A[i][j];
                // 새로 추가된 나무가 섞였을 수 있으므로 매년 정렬 (각 칸의 나무 수가 많지 않다면 충분함)
                if(!trees[i][j].empty()){
                    sort(trees[i][j].begin(), trees[i][j].end());
                }
            }
        }
    }
    
    // 남은 나무의 총 개수 계산
    long long result = 0;
    for (int i = 1; i <= n; i++){
        for (int j = 1; j <= n; j++){
            result += trees[i][j].size();
        }
    }
    
    cout << result;
    return 0;
}
