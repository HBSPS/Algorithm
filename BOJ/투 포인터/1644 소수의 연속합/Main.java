// 1644 소수의 연속합

// 에라토스테네스의 체
    // N까지의 소수를 구하기 위해 루트 N까지 각 배수들을 모두 제거

// 투포인터
    // 투포인터를 이용해서 목표 수 보다 크다면 start를 +1
    // 목표 수 보다 작다면 end를 +1

import java.util.*;
import java.io.*;

public class Main {
    static int MAX_SIZE = 4000000;
    static boolean[] isPrime = new boolean[MAX_SIZE + 1]; // 해당 값이 소수인지 여부
    static ArrayList<Integer> prime = new ArrayList<>(); // N까지의 소수 리스트
    static int N;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());

        getPrimeNumbers();

        int answer = 0;
        int start = 0;
        int end = 0;

        while (true) {
            int sum = sum(start, end);

            if (sum == N) {
                answer++;
                end++;
            } else if (sum < N) {
                end++;
            } else {
                start++;
            }

            if (start == prime.size() || end == prime.size() || start > end) break;
        }

        System.out.println(answer);
    }

    static void getPrimeNumbers() {
        isPrime[0] = isPrime[1] = true;

        for (int i = 2; i * i <= MAX_SIZE; i++) {
            if (!isPrime[i]) {
                for (int j = i * i; j <= MAX_SIZE; j += i) {
                    isPrime[j] = true;
                }
            }
        }

        for (int i = 0; i <= MAX_SIZE; i++) {
            if (!isPrime[i]) {
                prime.add(i);
            }
        }
    }

    static int sum(int start, int end) {
        int sum = 0;
        for (int i = start; i <= end; i++) {
            sum += prime.get(i);
        }

        return sum;
    }
}
    