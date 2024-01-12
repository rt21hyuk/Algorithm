#include<iostream>

using namespace std;
int frq_score, frq_idx;
int scores[101] = {0,};

void Init()
{
    frq_score=-1, frq_idx=-1;
    for(int i=0; i<101; i++)
    {
        scores[i] = 0;
    }
}
int main(int argc, char** argv)
{
	int T, idx;
    std::cin >> T;
    
    for(int i=0; i<T; i++)
    {
        Init();
        std::cin >> idx;
        for(int j=0; j<1000; j++)
        {
         	int score;
            std::cin >> score;
            scores[score]++;
            if(frq_score <= scores[score]) 
            {
                frq_score = scores[score];
                frq_idx = score;
            }
        }
         std::cout  << "#" <<idx << " " << frq_idx << "\n";
    }
	return 0;//정상종료시 반드시 0을 리턴해야합니다.
}