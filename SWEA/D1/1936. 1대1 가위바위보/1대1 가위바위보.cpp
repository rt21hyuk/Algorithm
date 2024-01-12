#define  si 1
#define rock 2
#define paper 3

#include<iostream>

using namespace std;

int main(int argc, char** argv)
{
	int a, b;
    std::cin >> a >> b;
    
    if(a == si)
    {
    	if(b == rock)   std::cout << 'B';
        else std::cout << 'A';
    }
    else if(a == rock)
    {
        if(b == si) std::cout << 'A';
        else std::cout << 'B';
    }
    else if(a == paper)
    {
        if(b == si) std::cout << 'B';
        else std::cout << 'A';
    }
    
	return 0;//정상종료시 반드시 0을 리턴해야합니다.
}