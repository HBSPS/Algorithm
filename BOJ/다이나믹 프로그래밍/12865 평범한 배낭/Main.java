// 12865 평범한 배낭

// DP 사용

import java.io.*;
import java.util.*;

public class Main {
    static int N, K;
    static int[][] dpTable;
    static int[][] items;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        dpTable = new int[N + 1][K + 1]; // row: 아이템의 갯수, column: 무게
        items = new int[N + 1][2]; // weight, value

        for (int i = 1; i <= N; i++) {
            st = new StringTokenizer(br.readLine());

            items[i][0] = Integer.parseInt(st.nextToken());
            items[i][1] = Integer.parseInt(st.nextToken());
        }

        for (int weight = 1; weight <= K; weight++) { // 가방의 최대 무게
            for (int item = 1; item <= N; item++) { // item
                dpTable[item][weight] = dpTable[item-1][weight];

                // 가방의 전체 무게에서 현재 item의 무게를 뺀 값이 0 이상이라면 -> 물건을 더 담을 수 있다면
                if (weight - items[item][0] >= 0) {
                    dpTable[item][weight] = Math.max(dpTable[item-1][weight], items[item][1] + dpTable[item-1][weight - items[item][0]]);
                }
            }
        }

        System.out.println(dpTable[N][K]);
    }
}