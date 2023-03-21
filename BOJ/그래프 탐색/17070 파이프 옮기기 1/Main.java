// 17070 파이프 옮기기 1

// 처음에 BFS로 시도했으나 시간 초과 발생 -> 같은 노드를 여러번 방문하기 떄문
    // 따라서, DFS로 목적지까지 연결한 뒤 정답을 + 1

import java.io.*;
import java.util.*;

public class Main {
    static int N;
    static int answer = 0;
    static int[][] table;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());

        table = new int[N+1][N+1];

        for (int i = 1; i <= N; i++) {
            st = new StringTokenizer(br.readLine());

            for (int j = 1; j <= N; j++) {
                table[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        DFS(1, 2, 'R');

        System.out.println(answer);
    }

    // R: 가로, C: 세로, D: 대각선
    // x: 세로, y: 가로
    public static void DFS(int x, int y, char dir) {
        if (x == N && y == N) {
            answer++;
            return;
        }

        switch(dir) {
            case 'R': // 직전 파이프가 가로인 경우
            {
                if (y + 1 <= N && table[x][y+1] == 0) {
                    DFS(x, y+1, 'R');
                }
                break;
            }
            case 'C': // 직전 파이프가 세로인 경우
            {
                if (x + 1 <= N && table[x+1][y] == 0) {
                    DFS(x+1, y, 'C');
                }
                break;
            }
            case 'D': // 직전 파이프가 대각선인 경우
            {
                if (y + 1 <= N && table[x][y+1] == 0) {
                    DFS(x, y+1, 'R');
                }
                if (x + 1 <= N && table[x+1][y] == 0) {
                    DFS(x+1, y, 'C');
                }
                break;
            }
        }

        // 각 경우에 대해 대각선 이동을 할 수 있기 때문에 대각선은 모든 case에서 확인
        if (x + 1 <= N && y + 1 <= N && table[x][y+1] == 0 && table[x+1][y] == 0 && table[x+1][y+1] == 0) {
            DFS(x+1, y+1, 'D');
        }
    }
}