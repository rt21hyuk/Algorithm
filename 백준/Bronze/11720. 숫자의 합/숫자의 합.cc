#include <iostream>
#include <string>

using namespace std;
int main() {
	int n, sum=0;
	string s;
	cin >> n >> s;
	
	// char s = 1, (int)s = 49
	
	for(int i=0; i<n; i++)
	{
		sum += (int)s[i]-48;
	}
	cout << sum << "\n";
	return 0;			
}
