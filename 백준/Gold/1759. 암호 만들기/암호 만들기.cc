#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int l, c, cnt=0;
char ch[15];
vector<string> pwds;

void input() {
    cin >> l >> c;
    for(int i=0; i<c; i++) cin >> ch[i];
    sort(ch, ch+c);
}

void dfs(string str, int depth, int idx, int vowelNum) {
    if(ch[idx] == 'a' || ch[idx] == 'e' || ch[idx] == 'i' || ch[idx] == 'o' || ch[idx] == 'u') vowelNum++;
    str.push_back(ch[idx]);
    
    if(str.length() == l) {
        if(vowelNum >= 1 && (l-vowelNum) >= 2)
            pwds.push_back(str);
        return;
    }
    
    for(int i=idx+1; i<c; i++) {
        dfs(str, depth+1, i, vowelNum);
    }
}

void solution() {
    for(int i=0; i<c; i++) dfs("", 0, i, 0);
    for(auto pwd:pwds) cout << pwd << "\n";
}

void solve() {
    input();
    solution();
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    solve();
    return 0;
}