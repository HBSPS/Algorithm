// 1916 최소비용 구하기

// 특정 노드에서 특정 노드로 가는 최소 비용을 구하는 문제이므로 다익스트라 사용
    // 다익스트라는 순차 탐색과 우선순위 큐 방식이 있음

import java.io.*;
import java.util.*;

class Node implements Comparable<Node> {
    int nodeNumber, dist;

    Node(int nodeNumber, int dist) {
        this.nodeNumber = nodeNumber;
        this.dist = dist;
    }

    @Override
    public int compareTo(Node target) {
        if (this.dist < target.dist) {
            return -1;
        }

        return 1;
    }
}

public class Main {
    static int N, M, start, end;
    static final int INF = Integer.MAX_VALUE;
    static ArrayList<ArrayList<Node>> graph = new ArrayList<>();
    static int[] costTable = new int[10001];

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());

        M = Integer.parseInt(st.nextToken());

        for (int i = 0; i <= N; i++) {
            graph.add(new ArrayList<>());
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());

            int from = Integer.parseInt(st.nextToken());
            int to = Integer.parseInt(st.nextToken());
            int cost = Integer.parseInt(st.nextToken());

            graph.get(from).add(new Node(to, cost));
        }

        st = new StringTokenizer(br.readLine());
        start = Integer.parseInt(st.nextToken());
        end = Integer.parseInt(st.nextToken());

        Arrays.fill(costTable, INF);

        getAnswer();

        System.out.print(costTable[end]);
    }

    static void getAnswer() {
        PriorityQueue<Node> pq = new PriorityQueue<>();

        pq.add(new Node(start, 0));
        costTable[start] = 0;

        while(!pq.isEmpty()) {
            Node node = pq.poll();
            int dist = node.dist;
            int nodeNumber = node.nodeNumber;

            if (costTable[nodeNumber] < dist) {
                continue;
            }

            for (int i = 0; i < graph.get(nodeNumber).size(); i++) {
                int cost = costTable[nodeNumber] + graph.get(nodeNumber).get(i).dist;

                if (cost < costTable[graph.get(nodeNumber).get(i).nodeNumber]) {
                    costTable[graph.get(nodeNumber).get(i).nodeNumber] = cost;
                    pq.add(new Node(graph.get(nodeNumber).get(i).nodeNumber, cost));
                }
            }
        }
    }
}