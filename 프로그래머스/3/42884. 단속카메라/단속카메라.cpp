#include <algorithm>
#include <string>
#include <vector>

using namespace std;

int solution(vector<vector<int>> routes) {
    int answer = 1;
    sort(routes.begin(), routes.end());
    int end = routes[0][1];
    for(auto route:routes)
    {
        if(end < route[0]) {
        // 현재차가 나가는 부분보다 뒤에 차가 들어온다면
            answer++;
            end = route[1];
        }
        else if(end >= route[1]) end = route[1]; 
        // 현재차보다 다음차가 나가는 거리가 짧다면 갱신
    }
    return answer;
}