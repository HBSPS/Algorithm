// 1991 트리 순회

// 전위, 중위, 후위 순회한 결과를 반환
    // 그래프 탐색
    // 재귀적으로 작동할 수 있다
    // 단, 중요한 것은 노드간의 연결 관계를 표현하는 것
        // 노드에 관한 클래스를 생성하고 왼쪽 노드, 오른쪽 노드를 담을 수 있도록 한다
        // 별도의 메소드를 통해 노트 트리의 정보를 업데이트 하는 과정을 거친다

import java.io.*;
import java.util.*;

public class Main {
    static int N;
    static Node head = new Node('A', null, null);

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());

            char middleNodeName = st.nextToken().charAt(0);
            char leftNodeName = st.nextToken().charAt(0);
            char rightNodeName = st.nextToken().charAt(0);

            insertNode(head, middleNodeName, leftNodeName, rightNodeName);
        }

        preOrder(head);
        System.out.println();
        inOrder(head);
        System.out.println();
        postOrder(head);
    }
    static class Node {
        char nodeName;
        Node leftNode, rightNode;

        Node(char nodeName, Node leftNode, Node rightNode) {
            this.nodeName = nodeName;
            this.leftNode = leftNode;
            this.rightNode = rightNode;
        }
    }

    static void insertNode(Node currentNode, char middleNodeName, char leftNodeName, char rightNodeName) {
        if (currentNode.nodeName == middleNodeName) { // 현재 노드의 이름과 입력받은 노드의 이름이 같은 경우
            currentNode.leftNode = (leftNodeName == '.') ? null : new Node(leftNodeName, null, null); // 왼쪽 노드의 이름이 .이 아닌 경우 왼쪽 노드에 새로운 노드를 만들어 저장
            currentNode.rightNode = (rightNodeName == '.') ? null : new Node(rightNodeName, null, null); //오른쪽 노드의 이름이 .이 아닌 경우 오른쪽 노드에 새로운 노드를 만들어 저장
        } else { // 현재 노드의 이름과 입력받은 노드의 이름이 다른 경우
            if (currentNode.leftNode != null) insertNode(currentNode.leftNode, middleNodeName, leftNodeName, rightNodeName); // 현재 노드의 왼쪽 노드가 존재하는 경우, 현재 노드를 왼쪽 노드로 변경 + 나머지 입력값 그대로 전달 -> 결과적으로 현재 노드의 왼쪽 노드에 대해 위의 과정을 반복. 두 번쨰 입력의 경우 현재 노드는 A이므로 위의 조건 만족 X 만약 해당 조건문이 실행되어 재귀적으로 작동하게 되면 현재 노드는 B가 되므로 B노드에 자식 노드들을 추가할 수 있음
            if (currentNode.rightNode != null) insertNode(currentNode.rightNode, middleNodeName, leftNodeName, rightNodeName); // 현재 노드의 오른쪽 노드가 존재하는 경우, 현재 노드를 오른쪽 노드로 변경 + 나머지 입력값 그대로 전달 -> 결과적으로 현재 노드의 오른쪽 노드에 대해 위의 과정을 반복
        }
    }

    static void preOrder(Node node) {
        if (node == null) return;
        System.out.print(node.nodeName);
        preOrder(node.leftNode);
        preOrder(node.rightNode);
    }

    static void inOrder(Node node) {
        if (node == null) return;
        inOrder(node.leftNode);
        System.out.print(node.nodeName);
        inOrder(node.rightNode);
    }

    static void postOrder(Node node) {
        if (node == null) return;
        postOrder(node.leftNode);
        postOrder(node.rightNode);
        System.out.print(node.nodeName);
    }
}