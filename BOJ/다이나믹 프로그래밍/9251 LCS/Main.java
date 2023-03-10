// 9251 LCS

// 가장 긴 증가하는 부분 수열과 비슷하게 진행할 수 있음
    // 대신 가장 긴 증가하는 부분 수열이 아니라 두 개의 문자열을 비교하여 같은 부분의 길이를 찾는 것

// 마찬가지로 DP 사용가능
    // 문자열 두 개를 사용하므로 한 문자열에 대한 나머지 문자열로 비교
    // 두 번째 문자열의 길이와 같은 배열을 하나 생성하여 해당 글자까지의 최장 공통 부분수열의 길이를 저장
    // 두 문자열의 문자가 같은 경우 앞의 최장 공통 부분수열의 길이 + 1을 하여 배열에 저장
    // 각 문자에 대해 반복문을 돌리는 동안 임시 변수를 만들어 계속 0으로 초기화
        // 만약, 임시 변수의 값보다(특정 문자에 대해) 최장 공통 부분수열의 길이가 길다면 임시 변수를 해당 값으로 변경
    // 각 문자를 탐색하다가 두 문자가 같은 경우 임시 변수 + 1로 배열을 업데이트
    // 배열의 원소 중 가장 큰 값이 최장 공통 부분 수열의 길이

import java.io.*;
import java.util.*;

public class Main {
    static String firstString;
    static String secondString;
    static int length1, length2;

    static int[] check;
    static int cnt;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        firstString = st.nextToken();
        st = new StringTokenizer(br.readLine());
        secondString = st.nextToken();

        length1 = firstString.length();
        length2 = secondString.length();

        check = new int[length2];


        for (int i = 0; i < length1; i++) {
            cnt = 0;

            for (int j = 0; j < length2; j++) {
                if (cnt < check[j]) {
                    cnt = check[j];
                } else if (firstString.charAt(i) == secondString.charAt(j)) {
                    check[j] = cnt + 1;
                }
            }
        }

        int maxLength = 0;
        for (int i: check) {
            if (i > maxLength) {
                maxLength = i;
            }
        }
        System.out.println(maxLength);
    }
}