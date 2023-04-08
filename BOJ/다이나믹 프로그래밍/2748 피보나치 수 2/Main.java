// 2748 피보나치 수 2

// DP 사용

import java.io.*;
import java.util.*;

public class Main {
    static int N;
    static long[] fib;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());

        fib = new long[91];
        fib[0] = 0;
        fib[1] = 1;
        fib[2] = 1;

        if (N == 1) {
            System.out.println(fib[1]);
        } else if (N == 2) {
            System.out.println(fib[2]);
        } else {
            getFib();
            System.out.println(fib[N]);
        }
    }

    static void getFib() {
        for (int i = 3; i <= 90; i++) {
            fib[i] = fib[i-2] + fib[i-1];
        }
    }
}