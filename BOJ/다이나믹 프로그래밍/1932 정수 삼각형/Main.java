// 1932 정수 삼각형

// DP 사용
    // 각 줄의 양 끝은 자신의 값 + 직전 양 끝 값
    // 양 끝이 아닌 값은 자신의 대각선에 있는 값 중 큰 값 + 자기 자신의 값
    // 삼각형의 모든 수는 양의 정수이므로 가장 마지막줄에 있는 숫자 중에 최댓값을 찾으면 됨

import java.io.*;
import java.util.*;

public class Main {
    static int[][] tree;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());

        tree = new int[N][];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());

            tree[i] = new int[i+1];

            for (int j = 0; j < i + 1; j++) {
                int tmp = Integer.parseInt(st.nextToken());

                tree[i][j] = tmp;

                if (i > 0 && j == 0) {
                    tree[i][j] = tmp + tree[i-1][0];
                } else if (i > 0 && j == i) {
                    tree[i][j] = tmp + tree[i-1][i-1];
                } else if (i > 0) {
                    tree[i][j] = tmp + Math.max(tree[i-1][j-1], tree[i-1][j]);
                }
            }
        }

        int max = 0;
        for (int item: tree[N-1]) {
            if (item > max) {
                max = item;
            }
        }

        System.out.println(max);
    }
}