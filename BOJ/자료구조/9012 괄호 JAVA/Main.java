// BOJ 9012 괄호

// 시작하면서 두 import는 기본으로 한다고 생각하면 됨
import java.util.*;
import java.io.*;

// 백준의 경우 모든 코드는 public class Main안에 있어야 한다
public class Main {
    static int N;

    // Main 안에서는 함수를 자유롭게 만들어 사용할 수 있다
    // BufferedReader를 사용하기 위해서는 아래와 같이 main 함수를 선언해야 한다 -> 정해진 양식이라고 보면 됨
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        // 여기 윗 부분까지는 정해진 부분

        N = Integer.parseInt(st.nextToken());

        for (int i = 1; i <= N; i++) {
            String str = br.readLine();
            
            String ans = check(str);

            System.out.println(ans);
        }
    }

    // 각 경우에 대해 제대로 괄호가 닫혔는지 확인하는 부분
    public static String check(String str) {
        // 스택을 사용할 것이므로 new Stack을 이용해 스택 생성
        Stack<Character> stack = new Stack<>();

        for (int i = 0; i < str.length(); i++) {
            char tmp = str.charAt(i);

            // 여는 괄호 인 경우, 스택에 추가
            if (tmp == '(') {
                stack.push(tmp);
            }

            // 여는 괄호 인 경우, 스택에 있는 닫는 괄호를 하나 꺼낸다
            // 만약, 스택이 비어있다면 제대로 열고 닫지 않은 것이므로 No 반환
            // 처음에 여는 괄호가 있어야만 닫는 괄호가 존재할 수 있음. 따라서, 첫 괄호가 닫는 괄호라면 No 반환
            else if (stack.empty()) {
                return "NO";
            } else {
                stack.pop();
            }
        }

        // 모든 경우가 끝나고 스택에 남은것이 없으면 Yes, 잔여 괄호가 있다면 No
        if (stack.empty()) {
            return "YES";
        } else {
            return "NO";
        }
    }
}