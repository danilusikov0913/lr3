#!/usr/bin/env python3
n = 64
for i in range(n):  # кроликов
    for j in range(n):  # гусей
        if i * 4 + j * 2 == n:
            print('{} кроликов и {} гусей'.format(i, j))
