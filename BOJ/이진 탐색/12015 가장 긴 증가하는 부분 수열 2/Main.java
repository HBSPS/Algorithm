// 12015 가장 긴 증가하는 부분 수열 2

// 이전 문제 보다 범위가 늘어남
    // 같은 방법을 사용하면 시간초과 발생

// 값의 범위가 1,000,000이므로 N^2의 알고리즘은 사용할 수 없다
    // 최대 NlogN의 알고리즘을 사용해야 한다
        // 입력 배열의 모든 원소를 한 번 순회해야 하므로 N의 시간 복잡도는 기본으로 필요
        // 사용할 수 있는 logN 알고리즘 -> 이분탐색

// 가장 긴 증가하는 부분 수열을 출력하는 것이 아니라 길이만 구하면 된다
    // 수열의 구성은 상관없고 길이만 구할 수 있으면 된다

// [10, 20, 30, 15,40]이 입력되는 경우
    // [10]
    // [10, 20]
    // [10, 20, 30]
    // 15는 배열의 마지막 값인 30보다 작다
        // 15가 들어가기에 적절한 자리를 찾아서 값을 수정한다
        // [10, 15, 30]
    // [10, 15, 30, 40] -> 기대 결과는 [10, 20, 30, 40]이므로 차이가 있지만 배열의 길이는 같다

    // 증가하는 부분 수열은 오름차순으로 이루어져 있기 때문에 이분탐색을 사용할 수 있다
        // 이분탐색을 통해 적절한 자리를 찾아야 한다

import java.io.*;
import java.util.*;


public class Main {
    static int N;
    static int[] arr;

    static ArrayList<Integer> LIS;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        arr = new int[N];

        st = new StringTokenizer(br.readLine());

        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        LIS = new ArrayList<>();
        LIS.add(0);

        for (int i: arr) {
            if (LIS.get(LIS.size() - 1) < i) LIS.add(i);
            else changeValueOfLIS(i);
        }

        System.out.println(LIS.size() - 1);
    }

    static void changeValueOfLIS(int value) {
        int start = 0;
        int end = LIS.size() - 1;

        while (start < end) {
            int mid = (start + end) / 2;

            if (LIS.get(mid) >= value) end = mid;
            else start = mid + 1;
        }

        LIS.set(end, value);
    }
}