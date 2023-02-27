// 14002 가장 긴 증가하는 부분 수열 4

// i번쨰 숫자까지의 가장 긴 증가하는 수열
    // i번째 숫자보다 작은 숫자까지의 가장 긴 증가하는 수열 + 1
    // 전체 배열 N의 가장 긴 증가하는 수열의 길이 = 배열의 각 숫자까지의 가장 긴 증가하는 수열의 길이

// 단, 가장 긴 증가하는 부분 수열도 함께 출력해야 한다
    // 가장 긴 증가하는 부분 수열을 담은 배열을 추가

// 배열과 리스트
    // 배열: 크기가 정해져 있다
    // 리스트: 크기가 정해져 있지 않고 동적으로 변화 -> java.util.ArrayList

import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer((br.readLine()));
        StringBuilder sb = new StringBuilder();

        int N = Integer.parseInt(st.nextToken());

        int[] arr = new int[N];
        int[] dp = new int[N];
        dp[0] = 1;

        st = new StringTokenizer(br.readLine());

        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        int max_count = 1;

        for (int i = 1; i < N; i++) {
            dp[i] = 1;

            for (int j = 0; j < i; j++) {
                if (arr[i] > arr[j]) {
                    dp[i] = Math.max(dp[i], dp[j] + 1);
                    max_count = Math.max(max_count, dp[i]);
                }
            }
        }

        sb.append(max_count).append("\n");

        // 가장 긴 부분 수열 구하기
        Stack<Integer> answer = new Stack<>();


        for (int i = N - 1; i >= 0; i--) {
            if (max_count == dp[i]) {
                answer.push(arr[i]);
                max_count--;
            }
        }

        while(!answer.isEmpty()) {
            sb.append(answer.pop()).append(" ");
        }

        System.out.println(sb.toString());
    }
}
