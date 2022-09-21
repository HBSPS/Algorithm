// BOJ 1021 회전하는 큐

import java.util.*;
import java.io.*;

public class Main {
    static int N, M;
    static int[] arr;
    static int cntL; // 왼쪽으로 회전 수행 횟수
    static int cntR; // 오른쪽으로 회전 수행 횟수
    static int total; // 전체 횟수

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        // 공백을 기준으로 N과 M을 입력
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        // 왼쪽과 오른쪽 회전을 구분하기 위해 두개의 덱 생성 -> dqL : 왼쪽으로 회전할 때 사용 / dqR : 오른쪽으로 회전할 때 사용
        Deque<Integer> dqL = new LinkedList<>();
        Deque<Integer> dqR = new LinkedList<>();

        // 사용자의 입력 값으로 덱 초기화
        for (int i = 1; i <= N; i++) {
            dqL.add(i);
            dqR.add(i);
        }

        // 사용자가 찾고자 하는 요소 저장
        arr = new int[M];
        st = new StringTokenizer(br.readLine()); // 줄 바꿔서 다시 입력받기 위해 사용하는 것

        for (int i = 0; i < M; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        // 전체 카운트 수
        total = 0;

        // 찾고자 하는 모든 경우에 대해
        for (int i = 0; i < M; i++) {
            // 왼쪽 회전과 오른쪽 회전을 비교
            cntL = 0;
            cntR = 0;

            // 덱의 맨 앞의 요소가 찾고자 하는 요소와 같아질 때 까지 왼쪽으로 회전
            while (dqL.peek() != arr[i]) {
                dqL = LRotate(dqL);
                cntL++;
            }
            // 덱의 맨 앞의 요소가 찾고자 하는 요소와 같아질 때 까지 오른쪽으로 회전
            while (dqR.peek() != arr[i]) {
                dqR = RRotate(dqR);
                cntR++;
            }

            // 각각의 경우 덱의 맨 앞 요소 제거
            dqL.removeFirst();
            dqR.removeFirst();

            // 왼쪽과 오른쪽 중, 더 적게 걸리는 방향을 카운트
            total += Math.min(cntL, cntR);
        }

        System.out.println(total);
    }
    

    // 왼쪽으로 덱 회전
    public static Deque<Integer> LRotate(Deque<Integer> dq) {
        dq.addLast(dq.removeFirst());

        return dq;
    }

    // 오른쪽으로 덱 회전
    public static Deque<Integer> RRotate(Deque<Integer> dq) {
        dq.addFirst(dq.removeLast());

        return dq;
    }
}