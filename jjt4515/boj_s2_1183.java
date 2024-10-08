package org.example;

// 문제: BOJ 1183 약속
// 날짜: 2024/10/08
// 풀이: A-B를 각각 구한 뒤 정렬하였다. 중간값의 |A-B+T|를 최소로 만들어주면 되기 때문에
// N이 홀수면 T의 개수는 1, 짝수면 T의 개수는 N/2번째 - N/2-1번째에 + 1이라는 식을 세워 풀었다.

import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(in.readLine());
        int[] input = new int[N];
        StringTokenizer st;
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(in.readLine());
            input[i] = Integer.parseInt(st.nextToken()) - Integer.parseInt(st.nextToken());
        }
        Arrays.sort(input);

        if(N%2==1) System.out.println(1);
        else System.out.println(Math.abs(input[N/2]-input[N/2-1])+1);
    }
}
