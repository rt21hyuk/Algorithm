#include <iostream>
#include <cstdio>
#include <cmath>
#include <queue>

using namespace std;

const int SIZE = 21;

int n;
int arr[SIZE][SIZE];
int arrCopy[SIZE][SIZE];
int maxBlock = 0;
int selection[5] = { 0, };

void input() {
	cin >> n;
	for (int i = 0; i < n; i++)
		for (int j = 0; j < n; j++)
			cin >> arr[i][j];
}

void findMax() {
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			if (maxBlock < arrCopy[i][j]) maxBlock = arrCopy[i][j];
		}
	}
}

void printArr() {
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cout << arrCopy[i][j] << " ";
		}
		cout << "\n";
	}
	cout << "\n";
}

void moveRight() {
	for (int i = 0; i < n; i++) {
		queue<int> q;
		for (int j = n - 1; j >= 0; j--) {
			if (arrCopy[i][j] != 0) q.push(arrCopy[i][j]);
			arrCopy[i][j] = 0;
		}
		int j = n - 1;
		while (!q.empty()) {
			//arrCopy[i][j] = q.front();
			int front = q.front();
			q.pop();
			if (!q.empty() && q.front() == front) {
				q.pop();
				front *= 2;
			}
			arrCopy[i][j] = front;
			j--;
		}
	}
}
void moveUp() {
	for (int j = 0; j < n; j++) {
		queue<int> q;
		for (int i = 0; i < n; i++) {
			if (arrCopy[i][j] != 0) q.push(arrCopy[i][j]);
			arrCopy[i][j] = 0;
		}
		int i = 0;
		while (!q.empty()) {
			int front = q.front();
			q.pop();
			if (!q.empty() && q.front() == front) {
				q.pop();
				front *= 2;
			}
			arrCopy[i][j] = front;
			i++;
		}
	}
}

void moveLeft() {
	for (int i = 0; i < n; i++) {
		queue<int> q;
		for (int j = 0; j < n; j++) {
			if (arrCopy[i][j] != 0) q.push(arrCopy[i][j]);
			arrCopy[i][j] = 0;
		}
		int j = 0;
		while (!q.empty()) {
			int front = q.front();
			q.pop();
			if (!q.empty() && q.front() == front) {
				q.pop();
				front *= 2;
			}
			arrCopy[i][j] = front;
			j++;
		}
	}
}

void moveDown() {
	for (int j = 0; j < n; j++) {
		queue<int> q;
		for (int i = n-1; i >= 0; i--) {
			if (arrCopy[i][j] != 0) q.push(arrCopy[i][j]);
			arrCopy[i][j] = 0;
		}
		int i = n - 1;
		while (!q.empty()) {
			int front = q.front();
			q.pop();
			if (!q.empty() && q.front() == front) {
				q.pop();
				front *= 2;
			}
			arrCopy[i][j] = front;
			i--;
		}
	}
}

void action() {
	//cout << "INIT: \n";
	//printArr();
	for (int i = 0; i < 5; i++) {
		int dir = selection[i];
		if (dir == 0) moveRight();
		else if (dir == 1) moveUp();
		else if (dir == 2) moveLeft();
		else if (dir == 3) moveDown();
		
		/*if (dir == 0) cout << "Right \n";
		else if (dir == 1) cout << "Up \n";
		else if (dir == 2) cout << "Left \n";
		else if (dir == 3) cout << "Down \n";*/

		//printArr();
	}
	findMax();
}

void copyArr() {
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			arrCopy[i][j] = arr[i][j];
		}
	}
}

void dfs(int depth) {
	if (depth == 5) {
		copyArr();
		action();
		return;
	}

	for (int i = 0; i < 4; i++) {
		selection[depth] = i;
		dfs(depth + 1);
	}
}

void solution() {
	dfs(0);
	cout << maxBlock;
}

void solve() {
	input();
	solution();
}

int main(int argc, char* argv[]) {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	//freopen("input.txt", "r", stdin);
	solve();
	return 0;
}