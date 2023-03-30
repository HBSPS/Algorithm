// 9663 N-Queen

// N X N의 체스판에 N개의 퀸을 놓을 수 있는 경우의 수
    // 시간을 여유롭게 주기 때문에 브루트포스 가능
    // 백트래킹을 통해 N개의 퀸을 놓게 되면 count + 1
    // 재귀적으로 작동 -> DFS의 변형
// 퀸은 체스판의 가로, 세로, 대각선으로 끝까지 이동할 수 있기 때문에 한 행에 한 개 이상의 퀸이 올 수 없다
    // 따라서, 퀸이 각 행에 하나씩 놓여야만 N X N의 체스판에 N개의 퀸을 배치할 수 있는 것이다

import java.io.*;
import java.util.*;

public class Main {
    static int N;
    static int[] arr; // 체스판의 각 행을 의미. 배열의 각 원소는 열을 의미. arr[1] = 2라면 2행 3열에 퀸이 놓여있음을 의미
    static int answer;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        arr = new int[N];

        answer = 0;
        DFS(0);

        System.out.println(answer);
    }

    static void DFS(int depth) {
        if (depth == N) {
            answer++;
            return;
        }

        for (int i = 0; i < N; i++) {
            arr[depth] = i;

            if (isPossible(depth)) {
                DFS(depth + 1);
            }
        }
    }

    static boolean isPossible(int depth) {
        for (int i = 0; i < depth; i++) {

            // 여러개의 퀸이 같은 열에 있는 경우
            if (arr[depth] == arr[i]) {
                return false;
            }

            // 여러개의 퀸이 대각선에 있는 경우
            // depth - i == arr[depth] - arr[i] -> 행의 차이와 열의 차이가 같다 = 대각선에 위치한다
            if (Math.abs(arr[depth] - arr[i]) == Math.abs(depth - i)) {
                return false;
            }
        }

        return true;
    }
}