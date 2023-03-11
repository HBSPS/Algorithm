// 11725 트리의 부모 찾기

// 인접리스트
    // 연결리스트 방식의 DFS를 사용
    // 단, 부모 노드를 알아야 하므로 기존의 DFS에서 fromNode와 toNode를 인자로 받아서 다음 DFS가 수행되기 전에 부모 노드를 저장

import java.io.*;
import java.util.*;

public class Main {
    static int N;
    static ArrayList<ArrayList<Integer>> arr;
    static int[] answer;
    static int[] visited;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());

        arr = new ArrayList<ArrayList<Integer>>();

        for (int i = 0; i < N + 1; i++) {
            arr.add(new ArrayList<Integer>());
        }

        for (int i = 0; i < N-1; i++) {
            st = new StringTokenizer(br.readLine());

            int fromNode = Integer.parseInt(st.nextToken());
            int toNode = Integer.parseInt(st.nextToken());

            arr.get(fromNode).add(toNode);
            arr.get(toNode).add(fromNode);
        }

        answer = new int[N+1];
        visited = new int[N+1];

        DFS(1, arr.get(1).get(0));

        for (int i = 2; i <= N; i++) {
            System.out.println(answer[i]);
        }
    }

    static void DFS(int fromNode, int toNode) {
        if (visited[toNode] != 1) {
            visited[toNode] = 1;

            answer[toNode] = fromNode;

            for (int i: arr.get(toNode)) {
                if (visited[i] != 1) {
                    DFS(toNode, i);
                }
            }
        }
    }
}