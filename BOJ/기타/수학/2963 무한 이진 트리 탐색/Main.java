// 2963 무한 이진 트리 탐색

// 반례
    // *RRLLR
    // 267

import java.io.*;
import java.math.*;
import java.util.*;

public class Main {
    static String search;
    static char[] arr;
    static int count = 0;

    static final BigInteger multiply_2 = new BigInteger("2");
    static final BigInteger add_3 = new BigInteger("3");
    static final BigInteger multiply_5 = new BigInteger("5");

    static BigInteger answer;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        search = st.nextToken();
        arr = search.toCharArray();

        answer = new BigInteger("1");

        for (char item: arr) {
            if (item == 'L') {
                answer  = L(answer);
            } else if (item == 'R') {
                answer = R(answer, count);
            } else if (item == '*') {
                answer = STAR(answer, count);
                count++;
            }
        }

        System.out.println(answer);
    }

    static BigInteger L(BigInteger prevNode) {
        return prevNode.multiply(multiply_2);
    }

    static BigInteger R(BigInteger prevNode, int count) {
        return prevNode.multiply(multiply_2).add(add_3.pow(count));
    }

    static BigInteger STAR(BigInteger prevNode, int count) {
        return prevNode.multiply(multiply_5).add(add_3.pow(count));
    }
}