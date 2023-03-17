// 9465 스티커

// 각 스티커까지의 누적합을 DP 테이블에 저장
    // 단, 변을 맞대고 있는 스티커는 함께 사용할 수 없기 때문에 주의

import java.io.*;
import java.util.*;

public class Main {
    static int T;
    static int N;

    static int[][] table;
    static int[][] dp;

    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        T = Integer.parseInt(st.nextToken());
        for (int i = 0; i < T; i++) {
            st = new StringTokenizer(br.readLine());

            N = Integer.parseInt(st.nextToken());
            table = new int[2][N];
            dp = new int[2][N];

            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                table[0][j] = Integer.parseInt(st.nextToken());
            }

            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                table[1][j] = Integer.parseInt(st.nextToken());
            }

            getDpTable(N);
            getAnswer();
        }

        System.out.println(sb.toString());
    }

    static void getDpTable(int N) {
        dp[0][0] = table[0][0];
        dp[1][0] = table[1][0];
        if (N > 1){
            dp[0][1] = table[1][0] + table[0][1];
            dp[1][1] = table[0][0] + table[1][1];

            for (int index = 2; index < N; index++) {
                dp[0][index] = Math.max(dp[1][index - 1], dp[1][index - 2]) + table[0][index];
                dp[1][index] = Math.max(dp[0][index - 1], dp[0][index - 2]) + table[1][index];
            }
        }
    }

    static void getAnswer() {
        int max = 0;

        for (int[] row: dp) {
            for (int item: row) {
                if (item > max) {
                    max = item;
                }
            }
        }

        sb.append(max);
        sb.append('\n');
    }
}