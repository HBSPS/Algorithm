// 11053 가장 긴 증가하는 부분 수열

// i번쨰 숫자까지의 가장 긴 증가하는 수열
    // i번째 숫자보다 작은 숫자까지의 가장 긴 증가하는 수열 + 1
    // 전체 배열 N의 가장 긴 증가하는 수열의 길이 = 배열의 각 숫자까지의 가장 긴 증가하는 수열의 길이

import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer((br.readLine()));

        int N = Integer.parseInt(st.nextToken());

        int[] arr = new int[N];
        int[] dp = new int[N];
        Arrays.fill(dp, 1);

        st = new StringTokenizer(br.readLine());

        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < i; j++) {
                if (arr[i] > arr[j]) {
                    dp[i] = Math.max(dp[i], dp[j] + 1);
                }
            }
        }

        Arrays.sort(dp);

        System.out.println(dp[dp.length - 1]);
    }
}
