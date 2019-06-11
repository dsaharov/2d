#!/usr/bin/env python3
import sys

def run2d(grid):
    biggest = max([len(row) for row in grid])
    grid = [
        '{}{}'.format(
            row,
            ''.join([' ' for i in range(biggest-len(row))])
        ) for row in grid if row[0] != '#'
    ]
    fuel = 2
    cargo = 0
    x = 0
    y = 0
    vx = 0
    vy = 0
    while fuel > 0:
        fuel -= 1
        try:
            op = grid[y][x]
        except:
            return
        if op == '>':
            vx = 1
            vy = 0
        elif op == '<':
            vx = -1
            vy = 0
        elif op == '^':
            vx = 0
            vy = -1
        elif op == 'v':
            vx = 0
            vy = 1
        elif op == 'o':
            sys.stdout.write(chr(cargo))
            sys.stdout.flush()
        elif op == 'l':
            sys.stdout.write(chr(fuel))
            sys.stdout.flush()
        elif op == 'c':
            sys.stdout.write('{}'.format(cargo))
            sys.stdout.flush()
        elif op == 'f':
            sys.stdout.write('{}'.format(fuel))
            sys.stdout.flush()
        elif op == '+':
            cargo += 1
        elif op == '-':
            cargo = max(0, cargo-1)
        elif op == 'L':
            if cargo > 0:
                if (vx, vy) == (-1, 0):
                    vx = 0
                    vy = -1
                elif (vx, vy) == (0, 1):
                    vx = 1
                    vy = 0
        elif op == 'J':
            if cargo > 0:
                if (vx, vy) == (1, 0):
                    vx = 0
                    vy = -1
                elif (vx, vy) == (0, 1):
                    vx = -1
                    vy = 0
        elif op == 'F':
            if cargo > 0:
                if (vx, vy) == (-1, 0):
                    vx = 0
                    vy = 1
                elif (vx, vy) == (0, -1):
                    vx = 1
                    vy = 0
        elif op == '7':
                if cargo > 0:
                    if (vx, vy) == (1, 0):
                        vx = 0
                        vy = 1
                    elif (vx, vy) == (0, -1):
                        vx = -1
                        vy = 0
        elif op in ['1', '2', '3', '4', '5', '6','8','9']:
            fuel += ord(op) - ord('0')
        elif op == 'i':
            fuel = int(input())
        elif op == '/':
            if cargo < 1:
                x += vx
                y += vy
        elif op == 'I':
            cargo = int(input())

        x += vx
        y += vy

if __name__ == '__main__':
    try:
        tar_file = sys.argv[1]
    except:
        print('Usage: 2d.py [path/to/file.2d]')

    try:
        with open(tar_file) as f:
            rows = [row for row in f]
    except:
        print('ERROR: Could not open file {}'.format(tar_file))
    try:
        run2d(rows)
    finally:
        print()
