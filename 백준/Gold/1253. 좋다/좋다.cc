#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int n, answer = 0;
vector<int> nums;

void input() {
    cin >> n;
    nums.resize(n);
    for(int i=0; i<n; i++) {
        cin >> nums[i];
    }
    sort(nums.begin(), nums.end());
}

void binarySearch(int target) {
    int left=0, right=n-1;
    while(left < right) {
        if(left == target) {
            left++;
            continue;
        }
        if(right == target) {
            right--;
            continue;
        }
        if(nums[left] + nums[right] < nums[target]) left++;
        else if(nums[left] + nums[right] > nums[target]) right--;
        else {
            answer++;
            return;
        }
    }
    return;
}

void solution() {
    for(int i=0; i<n; i++) {
        binarySearch(i);
    }
    cout << answer;
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