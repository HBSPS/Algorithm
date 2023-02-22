// 25314 코딩은 체육과목 입니다

// 자바의 반복문: for
    // JS와 사용이 비슷하다
        // 단, let i = 0으로 선언하던 JS와는 다르게 int i = 0으로 선언해야 한다

// print와 println
    // System.out.print()는 줄을 바꾸지 않는다
    // System.out.println()은 줄을 자동으로 바꾼다

import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());

        for (int i = 0; i < N / 4; i++) {
            System.out.print("long ");
        }

        System.out.print("int");
    }
}