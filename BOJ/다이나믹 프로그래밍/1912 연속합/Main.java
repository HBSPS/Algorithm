// 1912 연속 합

// DP 사용
    // 음수가 나오기 전까지의 합을 구해서 DP에 저장
    // 음수를 만난다면 음수를 연산한 뒤 여전히 양수라면 이어서 연산
    // 음수를 연산했을 때 음수가 된다면 해당 음수 앞까지의 수와 해당 음수는 연산에서 제외
        // 해당 음수 이후의 수 부터 다시 연산

import java.io.*;
import java.util.*;

public class Main {
    static int N;
    static int[] arr;
    static int[] dp;
    static int answer;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());

        arr = new int[N];
        dp = new int[N];

        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        answer = 0;

        dp[0] = Math.max(arr[0], 0);

        int minNum;
        if (arr[0] < 0) {
            minNum = arr[0];
        } else {
            minNum = Integer.MIN_VALUE;
        }
        boolean check = false;

        for (int i = 1; i < N; i++) {
            if (arr[i] < 0) {
                dp[i] = Math.max(dp[i - 1] + arr[i], 0);
                minNum = Math.max(minNum, arr[i]);
            }
            else {
                dp[i] = dp[i-1] + arr[i];
                check = true;
            }

            answer = Math.max(answer, dp[i]);
        }

        if (check) {
            System.out.println(answer);
        } else {
            System.out.println(minNum);
        }
    }
}