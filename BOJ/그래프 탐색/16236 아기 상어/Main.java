// 16236 아기 상어

// 아기 상어가 그래프를 돌아다니며 물고기를 먹는다
    // 자신의 몸집보다 큰 물고기를 먹을 수 없으며 자신의 몸집 만큼의 물고기를 먹으면 몸집이 커진다
    // BFS 사용

// 상어는 자신과 가장 가까운 물고기를 먹는다
    // 그런 물고기가 여럿이라면 위쪽에 있는 것을 우선, 위쪽에 있는 물고기가 여럿이라면 왼쪽의 물고기를 가장 먼저 먹는다

import java.io.*;
import java.util.*;

class SharkMove {
    int x;
    int y;
    int dist;

    SharkMove(int x, int y, int dist) {
        this.x = x;
        this.y = y;
        this.dist = dist;
    }
}

public class Main {
    static int N;
    static int[][] arr;
    static int answer = 0;

    static int shark_size = 2;
    static int shark_eat = 0;

    static int[] dx = {-1, 0, 1, 0};
    static int[] dy = {0, -1, 0, 1};

    static Queue<SharkMove> q;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        arr = new int[N][N];

        q = new LinkedList<>();

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());

            for (int j = 0; j < N; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());

                if (arr[i][j] == 9) {
                    q.add(new SharkMove(i, j, 0));
                    arr[i][j] = 0;
                }
            }
        }

        BFS();
    }

    static void BFS() {
        while (true) {
            ArrayList<SharkMove> fish = new ArrayList<>();
            int[][] dist = new int[N][N]; // 이동한 횟수를 저장하는 테이블

            while (!q.isEmpty()) {
                SharkMove shark = q.poll();
                int x = shark.x;
                int y = shark.y;

                for (int i = 0; i < 4; i++) {
                    int nx = x + dx[i];
                    int ny = y + dy[i];

                    if (nx >= 0 && nx < N && ny >= 0 && ny < N) {
                        if (dist[nx][ny] == 0 && arr[nx][ny] <= shark_size) {
                            dist[nx][ny] = dist[x][y] + 1;
                            q.add(new SharkMove(nx, ny, dist[nx][ny]));
                            if (1 <= arr[nx][ny] && arr[nx][ny] <= 6 && arr[nx][ny] < shark_size) {
                                fish.add(new SharkMove(nx, ny, dist[nx][ny]));
                            }
                        }
                    }
                }
            }

            if (fish.size() == 0) {
                System.out.println(answer);
                return;
            }

            SharkMove currentFish = fish.get(0);
            for (SharkMove sharkMove : fish) {
                if (currentFish.dist > sharkMove.dist) {
                    currentFish = sharkMove;
                } else if (currentFish.dist == sharkMove.dist) {
                    if (currentFish.x > sharkMove.x) {
                        currentFish = sharkMove;
                    } else if (currentFish.x == sharkMove.x) {
                        if (currentFish.y > sharkMove.y) {
                            currentFish = sharkMove;
                        }
                    }
                }
            }

            arr[currentFish.x][currentFish.y] = 0;
            answer += currentFish.dist;
            shark_eat += 1;

            if (shark_size == shark_eat) {
                shark_size += 1;
                shark_eat = 0;
            }

            q.add(currentFish);
        }
    }
}
