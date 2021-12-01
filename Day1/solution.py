#!/usr/bin/python3

result = -1
current = 0

with open('input.txt') as f:
    for line in f.readlines():
        if int(line.strip()) > current:
            result += 1
        current = int(line)

print(result)
