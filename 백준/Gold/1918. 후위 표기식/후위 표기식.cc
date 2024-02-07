#include <iostream>
#include <stack>
#include <typeinfo>
using namespace std;

string str;

void input()
{
    cin >> str;
}

bool isAlpha(char ch)
{
    if(ch >= 'A' and ch <= 'Z')  return true;
    return false;
}

void postfix()
{
    string answer;
    stack<char> operators;
    for(int i=0; i<str.length(); i++)
    {
        char ch = str[i];
        if(isAlpha(ch)) 
        {
            answer = answer + ch;
            continue;
        }
        if(ch == '(')
        {
            operators.push(ch);
            continue;
        }
        if(ch == ')')
        {
            while(operators.top() != '(')
            {
                answer = answer + operators.top();
                operators.pop();
            }
            operators.pop();
            continue;
        }
       if(ch == '*' || ch == '/')
        {
            while(!operators.empty() && (operators.top() == '*' || operators.top() == '/'))
            {
                answer = answer + operators.top();
                operators.pop();
            }
        }
        else
        {
            while(!operators.empty() && operators.top() != '(')
            {
                answer = answer + operators.top();
                operators.pop();
            }
        }
        operators.push(ch);
    }
    while(!operators.empty())
    {
        answer = answer + operators.top();
        operators.pop();
    }
    cout << answer << "\n";
}

void solution()
{
    postfix();
}

void solve()
{
    input();
    solution();
}

int main()
{
    cin.tie(NULL);
    ios::sync_with_stdio(false);
	// freopen("input.txt", "r", stdin);
    solve();
    return 0;
}