// 11444 피보나치 수 6

// 주어진 N의 범위가 매우 크기 때문에 long 타입을 쓰더라도 시간초과 발생

// 피보나치 수열을 행렬 곱으로 해결
    // Fn+1   Fn
    // Fn     Fn-1
    // 행렬 곱의 성질을 이용하게 되면 계속 N을 반으로 나누며 진행하기 때문에 O(logN)으로 계산 가능

import java.io.*;
import java.util.*;

public class Main {
    static long N;
    static final long DIVIDE = 1_000_000_007L;
    static final long[][] ORIGINAL = {{1, 1}, {1, 0}};
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Long.parseLong(st.nextToken());

        long[][] matrix = {{1, 1}, {1, 0}};

        // N번쨰 제곱의 [0][0]은 Fn+1이므로 N-1번째 [0][0]을 구해야 Fn이 된다
        System.out.println(divide(matrix, N-1)[0][0]);
    }

    public static long[][] divide(long[][] matrix, long N) {
        if (N == 1 || N == 0) {
            return matrix;
        }

        // 행렬을 반으로 나눠서
        long[][] halfMatrix = divide(matrix, N / 2);

        // 해당 행렬을 제곱
        halfMatrix = multiply(halfMatrix, halfMatrix);

        // 만약, 지수가 홀수 였다면 반으로 나눌 수 없기 때문에 기본 행렬을 한 번 곱해준다
        if (N % 2 == 1L) {
            halfMatrix = multiply(halfMatrix, ORIGINAL);
        }

        return halfMatrix;
    }

    public static long[][] multiply(long[][] target1, long[][] target2) {
        long[][] result = new long[2][2];

        result[0][0] = ((target1[0][0] * target2[0][0]) + target1[0][1] * target2[1][0]) % DIVIDE;
        result[0][1] = ((target1[0][0] * target2[0][1]) + target1[0][1] * target2[1][1]) % DIVIDE;
        result[1][0] = ((target1[1][0] * target2[0][0]) + target1[1][1] * target2[1][0]) % DIVIDE;
        result[1][1] = ((target1[1][0] * target2[0][1]) + target1[1][1] * target2[1][1]) % DIVIDE;

        return result;

    }
}