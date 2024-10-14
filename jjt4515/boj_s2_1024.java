// 날짜: 2024/10/1
// 문제: 백준 1024 수열의 함(https://www.acmicpc.net/problem/1024)
// 풀이: N을 L로 나누고 거기에 (N-1)/2를 뺀 수가 최소가 된다.
// 이 최소 수부터 연속으로 1씩 더해주며 L 갯수 만큼의 수를 더했을 때 N이 나오면 종료
// 조건 만족못시키면 -1 출력하도록 하였다.

// 이제 자바를 연습해볼랍니다.

package org.example;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int L = Integer.parseInt(st.nextToken());

        while(true) {
            int min = N/L - ((L-1)/2);
            if(min < 0 || L > 100) {
                System.out.println(-1);
                System.exit(0);
            }

            int sum = (min*2+L-1)*L/2;

            if(sum == N) {
                for (int i = 0; i < L; i++) {
                    System.out.print((min+i) + " ");
                }
                System.exit(0);
            }

            L++;

        }

    }
}
