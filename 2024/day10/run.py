import sys
from typing import List
sys.path.insert(0, '../../')
import os
import math
import copy
from itertools import permutations
from helper.helper import getFile, mymap, myfilter, download_input, hash_string, hashes_equal, key, key3, UP, DOWN, LEFT, RIGHT, dUP, dRIGHT, dDOWN, dLEFT, bound, get_grid

download_input(os.path.abspath(os.curdir))

# 1081, 721
# pretty happy, bfs, had some skill issues, can't complain

def part1():
    data = getFile(os.path.join(os.curdir, 'input.txt')).strip()

    data = data.split('\n')

    ans = 0

    grid = get_grid(data)

    for i in range(len(data)):
        for j in range(len(data[i])):
            grid[(i, j)] = int(grid[(i, j)])

    for i in range(len(data)):
        for j in range(len(data[0])):
            if grid[(i, j)] == 0: # bfs

                points = [(i, j, 0)]
                vis = {}

                while len(points):
                    ii, jj, n = points.pop()
                    vis[(ii, jj)] = 0
                    
                    if n == 9:
                        ans += 1
                        continue

                    for di, dj in [UP, DOWN, LEFT, RIGHT]:
                        ni = ii + di
                        nj = jj + dj

                        if (ni, nj) in grid and (ni, nj) not in vis:
                            if grid[(ni, nj)] == n + 1: # valid
                                points.append((ni, nj, n + 1))
        
    return ans 


def part2():
    data = getFile(os.path.join(os.curdir, 'input.txt')).strip()

    data = data.split('\n')

    ans = 0

    grid = get_grid(data)

    for i in range(len(data)):
        for j in range(len(data[i])):
            grid[(i, j)] = int(grid[(i, j)])

    for i in range(len(data)):
        for j in range(len(data[0])):
            if grid[(i, j)] == 0: # bfs

                points = [(i, j, 0)]
                vis = {}

                while len(points):
                    ii, jj, n = points.pop()
                    
                    if n == 9:
                        ans += 1
                        continue

                    for di, dj in [UP, DOWN, LEFT, RIGHT]:
                        ni = ii + di
                        nj = jj + dj

                        if (ni, nj) in grid and (ni, nj) not in vis:
                            if grid[(ni, nj)] == n + 1: # valid
                                points.append((ni, nj, n + 1))
        
    return ans 

print(f'part1: {part1()}')
print(f'part2: {part2()}')
