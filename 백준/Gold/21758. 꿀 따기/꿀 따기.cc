#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int n, answer=0;
vector<int> area;
vector<int> prefix;

void input() {
	cin >> n;
	area.resize(n);
	prefix.resize(n);
	for (int i = 0; i < n; i++) cin >> area[i];
	prefix[0] = area[0];
	for (int i = 1; i < n; i++) prefix[i] = prefix[i - 1] + area[i];
}

void solve() {
	for (int i = 1; i < n - 1; i++) answer = max(answer, (prefix[i] - area[0]) + (prefix[n-2] - prefix[i - 1])); // 꿀통이 벌 사이에 위치
	//cout << answer << "\n";
	for (int i = 1; i < n - 1; i++) answer = max(answer, (prefix[n-1] - area[0] - area[i]) + (prefix[n - 1] - prefix[i])); // 오른쪽에 꿀통이 위치, 좌측에 벌 고정
	//cout << answer << "\n";
	for (int i = 1; i < n - 1; i++) answer = max(answer, (prefix[n-1] - area[i] - area[n-1]) + (prefix[i-1])); // 왼쪽에 꿀통이 위치, 우측에 고정

	/*for (int i = 1; i < n - 1; i++) {
		cout << (prefix[n-1] - area[0] - area[i]) << " " << (prefix[n - 1] - prefix[i]) << " -> " << (prefix[n - 1] - area[0] - area[i]) + (prefix[n - 1] - prefix[i]) << "\n";
	}*/

	/*for (int i = 1; i < n - 1; i++) {
		cout << (prefix[n - 1] - area[i] - area[n - 1]) << " " << prefix[i-1] << " -> " << (prefix[n - 1] - area[i] - area[n - 1]) + (prefix[i-1]) << "\n";
	}*/

	cout << answer;
}

void solution() {
	input();
	solve();
}

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	//freopen("input.txt", "r", stdin);
	solution();
	return 0;
}