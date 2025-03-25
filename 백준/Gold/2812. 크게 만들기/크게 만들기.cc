#include <iostream>
#include <vector>
#include <stack>
#include <string>

using namespace std;

int main() {
    int n, k;
    cin >> n >> k;
    
    string num;
    cin >> num;

    vector<char> stack;
    int r = 0;

    for (int i = 0; i < n; ++i) {
        char current = num[i];
        while (!stack.empty() && r < k && stack.back() < current) {
            stack.pop_back();
            r++;
        }
        stack.push_back(current);
    }

    // 필요한 길이만큼 자르기 (n - k 자릿수 유지)
    while (stack.size() > n - k) {
        stack.pop_back();
    }

    for (char c : stack) {
        cout << c;
    }
    cout << '\n';

    return 0;
}