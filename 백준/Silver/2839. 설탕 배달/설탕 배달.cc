#include <iostream>
#include <vector>
using namespace std;

int main()
{
	int n, mn=12345;
	cin >> n;
	int tmp1=n/5, tmp2=n/3;
	vector<int> sum_vec;
	
	for(int i=0; i<=tmp1; i++)
		{
			for(int j=0; j<=tmp2; j++)
			{
				if(n == 5*i + 3*j)
					sum_vec.push_back(i+j);
			}
		}
	
	for(int i=0; i<sum_vec.size(); i++)
		mn=min(mn, sum_vec[i]);
	
	if(mn==12345) mn=-1;
	cout << mn;
}
