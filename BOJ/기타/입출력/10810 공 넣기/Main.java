// 10810 공 넣기

// 자바의 배열
    // 자바의 배열은 자료형 변수명 = new 자료형[배열길이]로 선언한다

// 반복문
    // 파이썬에서 사용하던 for item in list:를 자바에서도 사용할 수 있다
        // for (int i : list)로 사용할 수 있다

import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        int[] bucket = new int[N];

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());

            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());
            int ballNum = Integer.parseInt(st.nextToken());

            for (int j = start - 1; j < end; j++) {
                bucket[j] = ballNum;
            }
        }

        for (int j : bucket) {
            System.out.print(j + " ");
        }
    }
}
