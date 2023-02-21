// 2480 주사위 세개

// 자바 한 줄에 여러 입력
    // BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    // StringTokenizer st = new StringTokenizer(br.readLine());

    // int a = Integer.parseInt(st.nextToken());
    // int b = Integer.parseInt(st.nextToken());
    // int c = Integer.parseInt(st.nextToken());

// 자바의 기본 문법: 조건문
    // if / else if / else로 사용

// 자바의 배열 선언
    // 자료형 변수이름 = new 자료형[배열길이]
    // 정렬은 Arrays.sort(정렬대상)

import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int[] dice = new int[3];

        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());

        dice[0] = a;
        dice[1] = b;
        dice[2] = c;

        if (a == b && b == c) {
            System.out.println(10000 + a * 1000);
            return;
        } else if (a == b) {
            System.out.println(1000 + a * 100);
            return;
        } else if (b == c) {
            System.out.println(1000 + b * 100);
            return;
        } else if (c == a) {
            System.out.println(1000 + c * 100);
            return;
        } else {
            Arrays.sort(dice);
            System.out.println(dice[dice.length - 1] * 100);
        }
    } 
}
