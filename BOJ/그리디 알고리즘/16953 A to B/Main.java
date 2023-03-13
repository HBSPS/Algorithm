// 16953 A -> B

// 그리디 알고리즘 또는 BFS
    // 2 -> 4 -> 8 -> 81 -> 162
    // 거꾸로 생각해보면 162 -> 81 -> 8 -> 4 -> 2
    // 마찬가지로 40021 -> 4002 -> 2001 -> 200 -> 100
    // B를 A로 만든다고 생각할 때, B가 짝수인 경우는 2로 나누고 B가 홀수인 경우는 마지막 자리의 1을 제거한다

import java.io.*;
import java.util.*;

public class Main {
    static long A, B;
    static int count;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        A = Integer.parseInt(st.nextToken());
        B = Integer.parseInt(st.nextToken());
        count = 1;

        while (B != A) {
            if (B < A) {
                System.out.println(-1);
                System.exit(0);
            }

            if (B % 10 == 1) {
                B = B / 10;
            } else if (B % 2 == 0) {
                B = B / 2;
            } else {
                System.out.println(-1);
                System.exit(0);
            }

            count++;
        }

        System.out.println(count);
    }
}