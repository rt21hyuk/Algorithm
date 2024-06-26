import java.util.*;

class Solution {
    public int solution(int temperature, int t1, int t2, int a, int b, int[] onboard) {
        int lenOnBoard = onboard.length;
        int k = 1000 * 100;
        t1 += 10; t2 += 10; temperature += 10;
        
        int[][] dp = new int[onboard.length][51];
        for(int i=0; i<onboard.length; i++) {
            for(int j=0; j<51; j++) {
                dp[i][j] = k;
            }
        }
        
        dp[0][temperature] = 0;
        
        int flag = 1;
        if(temperature > t2) {
            flag = -1;
        }
        
        for(int i=1; i<lenOnBoard; i++) {
            for(int j=0; j<51; j++) {
                int minV = k;
                if((onboard[i] == 1 && t1 <= j && j <= t2) || onboard[i] == 0) {
                    // 1. 에어컨을 키지 않고 실외온도와 달라서 실내온도가 -flag 되는 경우
                    if(0 <= j+flag && j+flag <= 50)
                        minV = Math.min(minV, dp[i-1][j+flag]);
                    // 2. 에어컨을 키지 않고 현재온도 j가 실외온도랑 같아서 변하지 않는 경우
                    if(j == temperature)
                        minV = Math.min(minV, dp[i-1][j]);
                    // 3. 에어컨을 키고 현재온도가 변하는 경우
                    if(0 <= j-flag && j-flag <= 50)
                        minV = Math.min(minV, dp[i-1][j-flag] + a);
                    // 4. 에어컨을 키고 현재온도가 희망온도라서 온도가 변하지 않는 경우
                    if(t1 <= j && j <= t2)
                        minV = Math.min(minV, dp[i-1][j] + b);
                }
                
                dp[i][j] = minV;
            }
        }
        
        int answer = dp[lenOnBoard-1][0];
        for(int i=1; i<51; i++)
            answer = Math.min(answer, dp[lenOnBoard-1][i]);
        
        return answer;
    }
}