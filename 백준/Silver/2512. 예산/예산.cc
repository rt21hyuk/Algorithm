#include <iostream>
#include <algorithm>

using namespace std;

int n, totalCost, answer=1;
int costs[10001];

void input() {
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> costs[i];
	}
	cin >> totalCost;
}

void solve() {
	sort(costs, costs + n);
	int left = 1, right = costs[n - 1], curTotalCost;

	while (left <= right) {
		curTotalCost = 0;
		int mid = (left + right) / 2;
		for (int i = 0; i < n; i++) {
			curTotalCost += min(costs[i], mid);
		}
		if (curTotalCost <= totalCost) {
			answer = mid;
			left = mid + 1;
		}
		else right = mid - 1;
	}
}

void solution() {
	input();
	solve();
	cout << answer;
}

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	//freopen("input.txt", "r", stdin);
	solution();
	return 0;
}