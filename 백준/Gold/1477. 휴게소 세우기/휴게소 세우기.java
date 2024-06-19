//import java.io.*;
//import java.util.*;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());
		int l = Integer.parseInt(st.nextToken());
		
		int[] nextStops = new int[n+2];
		nextStops[0]=0; nextStops[n+1]=l;
		

		if(n > 0) {
			st = new StringTokenizer(br.readLine());
			for(int i=1; i<=n; i++) {
				nextStops[i] = Integer.parseInt(st.nextToken());
			}
		}
		
		Arrays.sort(nextStops);
		
		int left = 1;
		int right = l-1;
		
		while(left <= right) {
			int mid = (left + right) / 2;
			int sum = 0;
			
			for(int i=1; i<nextStops.length; i++) {
				sum += (nextStops[i] - nextStops[i-1] - 1) / mid;
			}
			
			if(sum > m) {
				left = mid + 1;
			}	else {
				right = mid - 1;
			}
		}
		System.out.println(left);
	}
}