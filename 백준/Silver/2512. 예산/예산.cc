#include <iostream>
#include <algorithm>

using namespace std;

int n, totalCost, maxCost = 1, curCost = 1;
int costs[10001];

int getCosts(int limitCost) {
	int cost = 0;
	for (int i = 0; i < n; i++) {
		if (costs[i] < limitCost) cost += costs[i];
		else cost += limitCost;
	}
	return cost;
}

void binarySearch() {
	int left = 1, right = totalCost, mid;
	while (left <= right) {
		mid = (left + right) / 2;
		int curTotalCost = getCosts(mid);
		if (curTotalCost <= totalCost) left = mid + 1;
		else if (curTotalCost > totalCost) right = mid - 1;
	}
	maxCost = left - 1;
}

void input() {
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> costs[i];
		if (maxCost < costs[i]) maxCost = costs[i];
	}
	cin >> totalCost;
}

void solve() {
	if (getCosts(100001) <= totalCost) return;
	binarySearch();
}

void solution() {
	input();
	solve();
	cout << maxCost;
}

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	//freopen("input.txt", "r", stdin);
	solution();
	return 0;
}