// 13549 숨바꼭질 3

// 한 정점에서 다른 정점까지의 최소비용을 구하는 문제이므로 다익스트라 사용
    // 단, 가중치가 0과 1 밖에 없기 때문에 0-1 BFS를 사용할 수 있다
        // 다익스트라의 최적화 버전
    // 덱을 사용하여 가중치가 0인 정점은 앞쪽 삽입, 가중치가 1인 정점을 뒤에 삽입
        // 가중치가 낮은 정점을 우선해서 방문하기 위해 -> 가중치가 곧 걸리는 시간이며 많은 횟수를 방문하더라도 가중치가 낮다면 더 적은 비용이라 할 수 있다

import java.io.*;
import java.util.*;

public class Main {
    static int N, K;
    static boolean[] visited;
    static int answer = Integer.MAX_VALUE;
    static final int MAX_RANGE = 1_000_000;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        visited = new boolean[MAX_RANGE + 1];

        BFS();

        System.out.println(answer);
    }

    static void BFS() {
        Deque<Node> dq = new ArrayDeque<>();
        dq.add(new Node(N, 0));

        while (!dq.isEmpty()) {
            Node node = dq.pollFirst();
            visited[node.pos] = true;

            if (node.pos == K) {
                answer = Math.min(answer, node.time);
            }

            if (node.pos * 2 <= MAX_RANGE && !visited[node.pos * 2]) {
                dq.addFirst(new Node(node.pos * 2, node.time));
            }

            if (node.pos + 1 <= MAX_RANGE && !visited[node.pos + 1]) {
                dq.addLast(new Node(node.pos + 1, node.time + 1));
            }

            if (node.pos - 1 >= 0 && !visited[node.pos - 1]) {
                dq.addLast(new Node(node.pos - 1, node.time + 1));
            }
        }
    }

    static class Node {
        int pos, time;

        Node(int pos, int time) {
            this.pos = pos;
            this.time = time;
        }
    }
}