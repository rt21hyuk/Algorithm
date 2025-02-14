#include <iostream>
#include <stack>
#include <string>

using namespace std;

string bracket;
int res = 1;
int result = 0;

void input() {
    cin >> bracket;
}

void solution() {
    stack<char> stk;

    for (int i = 0; i < bracket.length(); i++) {
        if (bracket[i] == '(') {
            res *= 2;
            stk.push(bracket[i]);
        }
        else if (bracket[i] == '[') {
            res *= 3;
            stk.push(bracket[i]);
        }
        else if (bracket[i] == ')') {
            if (stk.empty() || stk.top() != '(') {
                result = 0;
                break;
            }
            if (bracket[i - 1] == '(') {
                result += res;
            }
            res /= 2;
            stk.pop();
        }
        else if (bracket[i] == ']') {
            if (stk.empty() || stk.top() != '[') {
                result = 0;
                break;
            }
            if (bracket[i - 1] == '[') {
                result += res;
            }
            res /= 3;
            stk.pop();
        }
    }

    if (!stk.empty()) {
        result = 0;
    }

    cout << result << "\n";
}

void solve() {
    input();
    solution();
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    //freopen("input.txt", "r", stdin);
    solve();
    return 0;
}
