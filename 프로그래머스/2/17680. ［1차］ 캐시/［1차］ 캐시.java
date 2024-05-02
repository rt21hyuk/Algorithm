import java.util.*;

class Solution {
    static Queue<String> q = new LinkedList<>();

    public int solution(int cacheSize, String[] cities) {
        int answer = 0;
        
        if (cacheSize == 0) {
            return 5 * cities.length;
        }
        
        for (int i = 0; i < cities.length; i++) {
            cities[i] = cities[i].toLowerCase();

            if (q.size() < cacheSize) {
                if (q.contains(cities[i])) {
                    answer += 1;
                    q.remove(cities[i]);
                    q.add(cities[i]);
                } else {
                    answer += 5;
                    q.add(cities[i]);
                }
            } else {
                if (q.contains(cities[i])) {
                    answer += 1;
                    q.remove(cities[i]);
                    q.add(cities[i]);
                } else {
                    answer += 5;
                    q.poll();
                    q.add(cities[i]);
                }
            }
        }

        return answer;
    }
}