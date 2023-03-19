// 11404 플로이드

// 플로이드 워셜 사용
    // 버스를 이용하여 A에서 B로 가는 비용의 최솟값을 구해야 하기 때문에 모든 경우에 대해 순회해야 한다
        // 모든 노드에 대해 최소 비용을 구해야 하기 떄문에 플로이드-워셜을 사용해야 한다
    // N의 최댓값이 100이고 시간 제한이 1초이므로 100^3(=1,000,000) 즉 N^3으로 문제 해결 가능
        // 각 비용의 최댓값은 100,000이고 노드의 갯수는 최대 100개 이므로 자신의 노드를 제외한 모든 노드를 최대 비용으로 거쳐가는 경우인 99 * 100,000(= 9,900,000)보다 큰 값으로 최댓값을 설정해야 함

import java.io.*;
import java.util.*;

public class Main {
    final static int MAX_COST = 10_000_000;
    static int N, M;

    static int[][] table;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());

        M = Integer.parseInt(st.nextToken());

        table = new int[N][N];

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (i == j) {
                    table[i][j] = 0;
                } else {
                    table[i][j] = MAX_COST;
                }
            }
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());

            int from = Integer.parseInt(st.nextToken()) - 1;
            int to = Integer.parseInt(st.nextToken()) - 1;
            int cost = Integer.parseInt(st.nextToken());

            table[from][to] = Math.min(table[from][to], cost);
        }

        getMinCost();

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (table[i][j] == MAX_COST) {
                    table[i][j] = 0;
                }
            }
        }

        for (int[] items: table) {
            for (int item: items) {
                System.out.print(item);
                System.out.print(' ');
            }
            System.out.println();
        }
    }

    static void getMinCost() {
        for (int wayPoint = 0; wayPoint < N; wayPoint++) { // 경유지 노드
            for (int from = 0; from < N; from++) { // 출발지 노드
                for (int to = 0; to < N; to++) { // 도착지 노드
                    if (table[from][to] > table[from][wayPoint] + table[wayPoint][to]) {
                        table[from][to] = table[from][wayPoint] + table[wayPoint][to];
                    }
                }
            }
        }
    }
}