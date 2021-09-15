#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
import sys
if __name__ == '__main__':
    print( 'Введите координаты первой точки')
    a1 = float(input("Введите  x1? "))
    a2 = float(input("Введите  y1? "))
    print('Введите координаты второй точки')
    b1 = float(input("Введите  x2? "))
    b2 = float(input("Введите  y2? "))
S1 = ((a1**2 + a2**2)**1/2)
S2 = ((b1**2 + b2**2)**1/2)
if S1 == S2:
    print("Точки А и B одинаково отдалены от начала координат")
    exit(1)
elif S1<S2:
    print("Точка А  находится ближе к началу координат")
    exit(2)
else: S1>S2
print("Точка B  находится ближе к началу координат")
exit(3)
