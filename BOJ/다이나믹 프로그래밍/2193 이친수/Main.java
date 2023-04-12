// 2193 이친수

// 이친수는 피보나치 수열과 동일한 형태를 띠게 된다

import java.io.*;
import java.util.*;

public class Main {
    static int N;
    static long[] dp;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());

        dp = new long[N+1];

        if (N == 1) {
            dp[1] = 1;
        } else if (N == 2) {
            dp[2] = 1;
        } else {
            dp[1] = 1;
            dp[2] = 1;

            for (int i = 3; i <= N; i++) {
                dp[i] = dp[i-2] + dp[i-1];
            }
        }

        System.out.println(dp[N]);
    }
}