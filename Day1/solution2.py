#!/usr/bin/python3

result = 0
current = 0

with open('input.txt') as f:
    lines = f.readlines()
    current = sum([int(line.strip()) for line in lines[:3]])
    for i in range(3, len(lines)):
        new_curr = current - int(lines[i - 3].strip()) + int(lines[i].strip())
        if new_curr > current:
            result += 1
        current = new_curr

print(result)
