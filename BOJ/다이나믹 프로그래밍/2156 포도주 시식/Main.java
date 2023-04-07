// 2156 포도주 시식

// DP 사용
    // i 번째 위치에서
        // i-1까지의 최대
        // i-2까지의 최대 + i 번째
        // i-3까지의 최대 + i-1 번째 + i 번째

import java.io.*;
import java.util.*;

public class Main {
    static int N;

    static int[] arr;
    static int[]dp;

    static int answer;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());

        arr = new int[N];
        dp = new int[N];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            arr[i] = Integer.parseInt(st.nextToken());
        }

        if (N == 1) {
            answer = arr[0];
        }
        else if (N == 2) {
            answer = arr[0] + arr[1];
        }
        else {
            dp[0] = arr[0];
            dp[1] = arr[0] + arr[1];
            dp[2] = compare(arr[0] + arr[2], arr[1] + arr[2], arr[0] + arr[1]);

            for (int i = 3; i < N; i++) {
                dp[i] = compare(dp[i-3] + arr[i-1] + arr[i], dp[i-2] + arr[i], dp[i-1]);
            }

            answer = dp[0];
            for (int item: dp) {
                if (answer < item) {
                    answer = item;
                }
            }
        }

        System.out.println(answer);
    }

    static int compare(int a, int b, int c) {
        int tmp = Math.max(a, b);

        return Math.max(tmp, c);
    }
}