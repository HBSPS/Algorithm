// 1629 곱셈

// 모듈러의 성질
    // (A * B) % C
    // = (A % C * B % C) % C

// 분할해서 문제를 생각해야 한다
    // 입력이 10 11 12인 경우
    // 10^11 % 12
    // = ((10^5 * 10^5) * 10) % 12
    // = ((10^5 * 10^5) % 12 * 10 % 12) % 12
    // ...


import java.io.*;
import java.util.*;

public class Main {
    static long C;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        long A = Long.parseLong(st.nextToken());
        long B = Long.parseLong(st.nextToken());
        C = Long.parseLong(st.nextToken());

        long answer = pow(A, B);

        System.out.println(answer);
    }

    public static long pow(long A, long B) {
        if (B == 1) {
            return A % C;
        }

        long temp = pow(A, B / 2);

        if (B % 2 == 1) {
            // temp, A의 최댓값은 int형의 최댓값과 동일
                // int * int가 long의 범위를 넘지 않으니 temp * temp는 long으로 표현 가능
                // 단, A를 곱하게 되면서 long의 범위를 넘기 때문에 자료형 주의
            // temp * temp * A % C
            // = ((temp * temp) * A) % C
            // = ((temp * temp) % C * A % C) % C
            return (temp * temp % C) * A % C;
        }

        return temp * temp % C;
    }
}