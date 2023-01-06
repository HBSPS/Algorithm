// BOJ 15665 N과 M (11)

// 백트래킹 이용
// 중복되지 않는 수열만 출력해야 하므로 집합을 사용하여 중복 검사
// 길이가 M인 수열이 집합안에 있는지 확인하여 없다면 출력, 있다면 return
// 같은 수를 여러 번 골라도 되기 때문에 visit에 관한 처리는 하지 않아도 된다

import java.util.*;
import java.io.*;

public class Main {
    static int[] arr, tmp;
    // static boolean[] visited;
    static int N, M;
    static HashSet<String> answer;
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
        // visited = new boolean[N + 1];
        answer = new HashSet<>();

        selector(N, M, 0);

        System.out.println(sb);
    }

    public static void selector(int N, int M, int depth) {
        if (depth == M) {
            if (!answer.contains(Arrays.toString(tmp))) {
                answer.add(Arrays.toString(tmp));
                for (int i = 0; i < M; i++) {
                    sb.append(tmp[i]);
                    sb.append(' ');
                }
                sb.append('\n');
                return;
            }
            return;
        }

        for (int i = 0; i < N; i++) {
            tmp[depth] = arr[i];
            selector(N, M, depth + 1);

        }
    }
}