# !/usr/bin/env python
# -*- coding: utf-8 -*-
# programmers 게임 맵 최단거리

from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def solution(maps):
    n = len(maps)
    m = len(maps[0])

    queue = deque([(0, 0)])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx > n - 1 or ny < 0 or ny > m - 1:
                continue

            if maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx, ny))

    if maps[n - 1][m - 1] == 1:
        return -1
    else:
        return maps[n - 1][m - 1]