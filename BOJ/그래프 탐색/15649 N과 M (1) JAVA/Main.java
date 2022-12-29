// BOJ 15649 N과 M (1)

// 재귀 함수를 돌림
// 전에 풀었던 파이썬의 방식으로는 해결할 수 없었음
// depth 변수를 추가하여 배열에 index로 접근하는 방식을 사용
// 중복을 허용하지 않기 때문에 특정 원소를 정답 배열에 넣게 되면서 해당 배열에 방문 처리를 해줘야 함

import java.util.*;
import java.io.*;

public class Main {
    static int arr[];
    static boolean check[];
    static StringBuilder sb = new StringBuilder();

    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        arr = new int[M];
        check = new boolean[N + 1];

        combination(N, M, 0);

        System.out.println(sb);
    }

    public static void combination(int N, int M, int depth) {
        if (depth == M) {
            for (int i = 0; i < M; i++) {
                sb.append(arr[i] + " ");
            }
            sb.append("\n");
            return;
        }

        for (int i = 1; i <= N; i++) {
            if (check[i] == false) {
                check[i] = true;
                arr[depth] = i;
                combination(N, M, depth + 1);
                check[i] = false;
            }
        }
    }
}
