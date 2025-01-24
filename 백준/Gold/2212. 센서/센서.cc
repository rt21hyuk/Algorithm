#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int n, k, ans = 0;
vector<int> sensors;
vector<int> spaces;

void input() {
	cin >> n >> k;
	sensors.resize(n);
	spaces.resize(n-1);
	for (int i = 0; i < n; i++) {
		cin >> sensors[i];
	}
	sort(sensors.begin(), sensors.end());
}

void solution() {
	for (int i = 0; i < n-1; i++) {
		spaces[i] = sensors[i+1] - sensors[i];
	}
	sort(spaces.begin(), spaces.end());
	
	for (int i = 0; i < n-k; i++) {
		ans = ans + spaces[i];
	}
	cout << ans;
}

void solve() {
	input();
	solution();
}

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	//freopen("input.txt", "r", stdin);
	solve();
	return 0;
}