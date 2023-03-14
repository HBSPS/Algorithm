// 11660 구간 합 구하기 5

// DP 사용
    // 누적합을 저장하고 있는 별도의 테이블을 만든다
    // 해당 테이블을 초기화 할 때는 N+1로 초기화 한다
        // 문제에서 계상하고자 하는 좌표의 값이 0이 아닌 1부터 시작하기 때문
    // 결론적으로 구하고자 하는 구간의 직전까지 누적합 + 구하고자 하는 구간의 값 - 직전까지 누적합을 더했을 때 중복되는 부분을 하면 답을 구할 수 있다

import java.io.*;
import java.util.*;

public class Main {
    static int N, M;
    static int[][] table;
    static int[][] dp;

    static StringBuilder sb;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        sb = new StringBuilder();

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        table = new int[N][N];
        dp = new int[N+1][N+1];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());

            for (int j = 0; j < N; j++) {
                table[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        setDpTable();

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int x1 = Integer.parseInt(st.nextToken());
            int y1 = Integer.parseInt(st.nextToken());
            int x2 = Integer.parseInt(st.nextToken());
            int y2 = Integer.parseInt(st.nextToken());

            getAnswer(x1, y1, x2, y2);
        }

        System.out.print(sb.toString());
    }

    static void setDpTable() {
        for (int i = 1; i < N + 1; i++) {
            for (int j = 1; j < N + 1; j++) {
                dp[i][j] = dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1] + table[i - 1][j - 1];
            }
        }
    }

    static void getAnswer(int x1, int y1, int x2, int y2) {
        int answer = 0;
        answer = dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1];

        sb.append(answer);
        sb.append('\n');
    }
}