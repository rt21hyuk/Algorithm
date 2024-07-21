#include <iostream>
#include <algorithm>
using namespace std;

int main() {
	int n;
	long long arr[10000];
	long long min = 0;

	cin >> n;

	for (int i = 0; i < n; i++) {
		cin >> arr[i];
	}

	// 근손실 정도를 정렬
	sort(arr, arr + n);

	// 3. 운동기구의 개수가 홀수인 경우
	if (n % 2 == 1) {
		min = arr[n - 1];	// 마지막 가장 큰 값을 따로 저장
		n--;

		for (int i = 0; i < n / 2; i++) {
			// 마지막 값을 제외한 최소, 최대값의 합
			long long tempMin = arr[i] + arr[(n - 1) - i];
			if (tempMin > min) {	// 마지막 값보다 크면
				min = tempMin;	// 최솟값을 초기화
			}
		}
	}

	// 2. 운동기구의 개수가 짝수인 경우
	else {
		for (int i = 0; i < n / 2; i++) {
			// 마지막 값을 제외한 최소, 최대값의 합
			long long tempMin = arr[i] + arr[(n - 1) - i];
			if (tempMin > min) {	// 마지막 값보다 크면
				min = tempMin;	// 최솟값을 초기화
			}
		}
	}

	cout << min;

	return 0;
}