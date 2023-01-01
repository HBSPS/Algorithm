// BOJ 15655 N과 M (6)

// 백트래킹 이용
    // 입력 받은 배열을 오름차순으로 정렬

import java.util.*;
import java.io.*;

public class Main {
    static int[] arr, tmp;
    static boolean[] visited;
    static int N, M;
    static StringBuilder sb = new StringBuilder();

    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        arr = new int[N];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(arr);

        tmp = new int[M];
        visited = new boolean[N + 1];

        selector(N, M, 0);

        System.out.println(sb);
    }

    public static void selector(int N, int M, int depth) {
        if (depth == M) {
            for (int i = 0; i < M; i++) {
                sb.append(tmp[i]);
                sb.append(' ');
            }
            sb.append('\n');
            return;
        }

        for (int i = 0; i < N; i++) {
            if (depth > 0 && tmp[depth - 1] > arr[i]) {
                continue;
            }
            if (visited[i] == false) {
                visited[i] = true;
                tmp[depth] = arr[i];
                selector(N, M, depth + 1);
                visited[i] = false;
            }
        }
    }
}