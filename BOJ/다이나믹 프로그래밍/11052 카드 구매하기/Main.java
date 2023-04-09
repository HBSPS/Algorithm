// 11052 카드 구매하기

// DP 사용
    // N장의 카드를 사야 하는데 가장 큰 비용을 지불하는 방법
    // N장의 카드를 구매하는 방법
        // 1. 1장의 카드 팩 + N-1장의 카드를 구매
        // 2. 2장의 카드 팩 + N-2장의 카드를 구매
        // ...

import java.io.*;
import java.util.*;

public class Main {
    static int N;
    static int[] price;
    static int[] dp;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());

        price = new int[N+1];
        dp = new int[N+1];

        st = new StringTokenizer(br.readLine());
        for (int i = 1; i <= N; i++) {
            price[i] = Integer.parseInt(st.nextToken());
        }

        for (int i = 1; i <= N; i++) {
            for (int j = 1; j <= i; j++) {
                dp[i] = Math.max(dp[i], dp[i - j] + price[j]); // i장의 카드를 구매하는 경우 = i-j장의 카드를 구매 + j장의 카드 팩 구매
            }
        }

        System.out.println(dp[N]);
    }
}