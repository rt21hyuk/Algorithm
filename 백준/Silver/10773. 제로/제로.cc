#include <iostream>
#include <stack>

using namespace std;

int n, answer = 0;
stack<int> stk;

void input() {
	cin >> n;
}

void solve() {
	for (int i = 0; i < n; i++) {
		int temp;
		cin >> temp;

		if (temp == 0) stk.pop();
		else stk.push(temp);
	}
	while(!stk.empty()) {
		answer += stk.top();
		stk.pop();
	}
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