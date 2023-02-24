// 10844 쉬운 계단 수

// 마지막 자릿수가 i(1<=i<=8)인 경우
    // 뒤에서 두 번째 자릿수가 (i-1)인 경우 + 뒤에서 두 번째 자릿수가 (i+1)인 경우
// 마지막 자릿수가 0인 경우
    // 뒤에서 두 번째 자릿수가 1인 경우
// 마지막 자릿수가 9인 경우
    // 뒤에서 두 번째 자릿수가 8인 경우

// 단, 나누는 수가 1,000,000,000이므로 int의 범위인 약 2,000,000을 초과한다
    // 따라서, long 자료형을 사용해야 한다

import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        long DIVIDE = 1000000000;

        long[][] dp = new long[N+1][10];
        
        // 한 자릿수인 경우
        for (int i = 1; i < 10; i++) {
            dp[1][i] = 1;
        }

        // 두 자릿수 이상인 경우
        for (int i = 2; i <= N; i++) {
            for (int j = 0; j < 10; j++) {
                if (j == 9) {
                    dp[i][j] = dp[i-1][8] % DIVIDE;
                }
                else if (j == 0) {
                    dp[i][j] = dp[i-1][1] % DIVIDE;
                }
                else {
                    dp[i][j] = (dp[i-1][j-1] + dp[i-1][j+1]) % DIVIDE;
                }
            }
        }

        long answer = 0;
        for (int i = 0; i < 10; i++) {
            answer += dp[N][i];
        }

        System.out.println(answer % DIVIDE);
    }
}
