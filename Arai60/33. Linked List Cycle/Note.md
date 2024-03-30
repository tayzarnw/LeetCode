# 33. Linked List Cycle

## Solution 1. Memorized visited nodes

過去に尋ねたnodeをvisited_nodes, set を用いて保存し、前に進むたびに過去に尋ねたことがあるか確認する

Time complexity : O(N)

全てのnodeを処理するため

Space complexity : O(N) worst case
ループの始まるに戻る時にプログラムは終了し、その時には全てのNodeはsetに保存されているため


## Solution 2. Modify visited nodes
過去に尋ねたnodeの値(val)をNoneとして変更しておく。
nodeのvalがNoneになっているところに辿り着けば、過去に尋ねたことがわかる

Time complexity : O(N)

Solution 1 を同じ理由

Space Complexity: O(1)
N個分の記憶する変数を用意せず、そのまま以前からの与えられたメモリ領域だけを変更するため

## Solution 3. Floyd's Tortoise and Hare algorithm

通常のスピードでListNodeをまわるカメと倍速でまわるウサギがいるとする。
もし、ListNodesにCycleが存在しなければ、ウサギの方が先に終了のNoneに辿り着ける。
一方でCycleが存在すれば、ウサギの方が先にCycleに入り回り続ける。
カメものちにCycleに入り、同じCycleを一緒に回っているため、ウサギもカメもいつか同じNodeでまた会う。
その時点でCycleが存在することがわかる。

Time complexity : O(N)

Solution 1 を同じ理由, うさぎが二倍のスピードだがO(N/2)のため, O(N)

Space Complexity: O(1)
