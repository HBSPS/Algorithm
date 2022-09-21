// BOJ 11729 하노이 탑 이동 순서

// N 원판을 세번째 기둥으로 옮기기 위해 1 ~ N-1 원판을 두번째 기둥으로 이동
// N 원판을 세번째 기둥으로 이동
// 1 ~ N-1 원판을 세번째 기둥으로 이동
// 원판이 한 개인 경우 첫번째 기둥에서 세번째 기둥으로 이동하고 종료

// N 원판을 옮기기 위해 1 ~ N-1 원판이 이동 -> N-1 원판을 옮기기 위해 1 ~ N-2 원판이 이동... => 재귀 사용

import java.util.*;
import java.io.*;

public class Main {
    static int N; // 전체 원판의 수
    static int from, mid, to; // from : 현재 원판이 있는 곳(기둥1) / mid : 원판이 거쳐가는 곳(기둥2) / to : 원판이 이동할 곳(기둥3)

    // 시간초과 때문에 출력에서 시간을 줄이기 위해 사용
    // StringBuilder를 통해 만들고 sb.append()를 통해 출력 문자열 추가
    // System.out.println(sb)를 통해 StringBuilder안의 내용 출력
    public static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        // N을 입력 -> 첫번째 기둥에 들어가는 원판의 갯수
        N = Integer.parseInt(st.nextToken());

        // 하노이탑의 최소 이동 = 2^N - 1
        // 자바의 거듭제곱 표현 : Math.pow(대상 수, 거듭제곱 횟수)
        sb.append(Math.round(Math.pow(2, N) - 1) + "\n");
        
        // N개의 원판을 첫번째 기둥에서 세번쨰 기둥으로 이동
        hanoi(N, 1, 2, 3);
        
        System.out.println(sb);
    }
    
    public static void hanoi(int N, int from, int mid, int to) {
        // 첫번째 기둥에 원판이 한 개인 경우 첫번째 기둥에서 세번째 기둥으로 이동
        if (N == 1) {
            sb.append(from + " " + to + "\n");
            return;
        }
        // 원판이 한 개를 초과하는 경우
        else {
            hanoi(N-1, from, to, mid); // 1 ~ N-1 원판을 두번째 기둥으로 이동
            sb.append(from + " " + to + "\n"); // N 원판을 세번째 기둥으로 이동;
            hanoi(N-1, mid, from, to); // 1 ~ N-1 원판을 세번째 기둥으로 이동
        }
    }
}