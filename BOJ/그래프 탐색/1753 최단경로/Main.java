// 1753 최단경로

// 한 정점에서 다른 정저까지의 최단 거리를 구하는 것 + 간선의 가중치는 자연수 (0 이상)
    // 다익스트라 사용

import java.io.*;
import java.util.*;

class Node implements Comparable<Node> {
    int dist;
    int number;

    Node(int dist, int number) {
        this.dist = dist;
        this.number = number;
    }

    @Override
    public int compareTo(Node target) {
        return this.dist - target.dist;
    }
}

public class Main {
    static final int INF = 2_000_000_000;
    static int V, E, K;
    static ArrayList<ArrayList<Node>> table;
    static int[] dist_arr;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        V = Integer.parseInt(st.nextToken());
        E = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        K = Integer.parseInt(st.nextToken());

        table = new ArrayList<>();
        for (int i = 0; i < V + 1; i++) {
            table.add(new ArrayList<>());
        }

        dist_arr = new int[V + 1];
        Arrays.fill(dist_arr, INF);

        for (int i = 0; i < E; i++) {
            st = new StringTokenizer(br.readLine());

            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());

            table.get(u).add(new Node(w, v));
        }

        dijkstra();

        for (int i = 1; i < V + 1; i++) {
            if (dist_arr[i] == INF) {
                System.out.println("INF");
            } else {
                System.out.println(dist_arr[i]);
            }
        }
    }

    static void dijkstra() {
        PriorityQueue<Node> pq = new PriorityQueue<>();
        boolean[] visited = new boolean[V + 1];

        pq.add(new Node(0, K));
        dist_arr[K] = 0;

        while (!pq.isEmpty()) {
            Node current_node = pq.poll();
            int dist = current_node.dist;
            int number = current_node.number;

            if (!visited[number]) {
                visited[number] = true;

                for (Node node: table.get(number)) {
                    if (!visited[node.number] && dist_arr[node.number] > (dist_arr[number] + node.dist)) {
                        dist_arr[node.number] = dist_arr[number] + node.dist;
                        pq.add(new Node(dist_arr[node.number], node.number));
                    }
                }
            }
        }
    }
}