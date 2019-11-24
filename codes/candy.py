#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solve(M, n_list, solutions):
    if M > len(solutions) or M < 0:
        return

    if (M == 0):
        solutions[M] = [0, "输，没能拿最后一个"]
        return
    if (M in n_list):
        solutions[M] = [1, "赢，全部拿走"]
        return
    for k in n_list:
        if (M-k > 0 and solutions[M-k][0] == 0):
            solutions[M] = [1, "赢，拿掉{}个剩余{}个致对手输".format(k, M-k)]
            return

    solutions[M] = [0, "无必赢方案"]
    return


def candy(M, n_list):
    solutions = [0, ""] * (M + 1)  # solutions: 1 - 先玩者赢；0 - 先玩者输；
    for i in range(M + 1):
        solve(i, n_list, solutions)
        print(i, solutions[i][1])

if __name__ == "__main__":
    M = int(input("糖果总数(正整数)："));
    n_list = input("每次拿的糖果数(空格分割，正整数列表：").split(" ");
    n_list = sorted([int(i) for i in set(n_list + [1])]);
    assert all([i > 0 for i in n_list]);
    candy(M, n_list)

