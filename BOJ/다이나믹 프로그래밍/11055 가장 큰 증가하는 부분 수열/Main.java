// 11055 가장 큰 증가하는 부분 수열

// DP 사용
    // 원소들을 담은 뒤 원소를 순회하는 과정
        // 해당 원소가 이전 원소보다 큰 경우 DP 테이블을 업데이트

import java.io.*;
import java.util.*;

public class Main {
    static int N;
    static int[] arr;
    static int[] dp;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());

        arr = new int[N];
        dp = new int[N];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        dp[0] = arr[0];
        getDP();

        getAnswer();
    }

    static void getDP() {
        for (int i = 0; i < N; i++) {
            dp[i] = arr[i];
            for (int j = 0; j < i; j++) {
                if (arr[i] > arr[j]) {
                    dp[i] = Math.max(dp[i], dp[j] + arr[i]);
                }
            }
        }
    }

    static void getAnswer() {
        int max = Integer.MIN_VALUE;
        for (int item: dp) {
            if (max < item) {
                max = item;
            }
        }

        System.out.println(max);
    }
}
