// 1010 다리 놓기

// 조합 사용
    // 두 다리가 겹치지 않도록 강 건너와 다리를 연결
        // 동쪽에서 M개의 사이트 중 N개의 사이트를 고르기만 한다면 서쪽 사이트와 1대1로 연결이 가능
    // 조합 공식
        // n+1 C r+1 = n C r + n C r+1
        // n C n = n C 0 = 1

import java.io.*;
import java.util.*;

public class Main {
    static int T;
    static int[][] dp = new int[31][31];

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        StringBuilder sb = new StringBuilder();

        T = Integer.parseInt(st.nextToken());

        for (int i = 1; i < 31; i++) {
            dp[i][i] = 1;
            dp[i][0] = 1;
        }

        for (int i = 2; i < 31; i++) {
            for (int j = 1; j < 31; j++) {
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j];
            }
        }

        for (int i = 0; i < T; i++) {
            st = new StringTokenizer(br.readLine());

            int N = Integer.parseInt(st.nextToken());
            int M = Integer.parseInt(st.nextToken());

            sb.append(dp[M][N]).append('\n');
        }

        System.out.println(sb);
    }
}