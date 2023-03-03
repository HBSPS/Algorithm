// 14500 테트로미노

// 브루트 포스
    // 한 정점으로 4칸까지 갈 수 있음
    // 백트래킹으로 풀 수 있음

// 단, ㅗ, ㅜ, ㅓ, ㅏ의 경우 한번에 그리는 것이 불가능 하므로 depth가 2일 때 탐색을 추가로 해줘야 한다
    // 나머지는 한 정점으로 부터 한번에 그리는 것이 가능하기 때문에 DFS로 해결할 수 있음

import java.io.*;
import java.util.*;

public class Main {
    static int N, M;
    static int[][] arr;
    static boolean[][] visit;

    static int[] dx = {1, -1, 0, 0};
    static int[] dy = {0, 0, 1, -1};
    static int max = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        arr = new int[N][M];
        visit = new boolean[N][M];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());

            for (int j = 0; j < M; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                visit[i][j] = true;
                DFS(arr[i][j], 1, i, j);
                visit[i][j] = false;
            }
        }

        System.out.println(max);
    }

    static void DFS(int sum, int depth, int x, int y) {
        if (depth == 4) {
            max = Math.max(max, sum);
            return;
        }

        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (nx < 0 || nx >= N || ny < 0 || ny >= M) {
                continue;
            }

            if (!visit[nx][ny]) {
                if (depth == 2) {
                    visit[nx][ny] = true;
                    DFS(sum + arr[nx][ny], depth + 1, x, y);
                    visit[nx][ny] = false;
                }

                visit[nx][ny] = true;
                DFS(sum + arr[nx][ny], depth + 1, nx, ny);
                visit[nx][ny] = false;
            }
        }
    }
}
