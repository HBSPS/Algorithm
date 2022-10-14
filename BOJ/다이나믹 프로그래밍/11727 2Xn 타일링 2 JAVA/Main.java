// BOJ 11727 2Xn 타일링 2

// 마찬가지로 arr[i] = arr[i-1] + 2 * arr[i-2]

import java.util.*;
import java.io.*;

public class Main {
    static int arr[];

    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());

        arr = new int[4+N];
        
        arr[0] = 0;
        arr[1] = 1;
        arr[2] = 3;
        arr[3] = 5;

        for (int i = 4; i <= N; i++) {
            arr[i] = (arr[i - 1] + 2 * arr[i - 2]) % 10007;
        }
        
        System.out.println(arr[N]);
    }
}
