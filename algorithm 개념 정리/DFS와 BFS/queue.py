import sys
sys.stdin = open('inputq.txt')
from collections import deque

q = deque()
for i in range(3):
    q.append(int(input()))
print(q)
for i in range(len(q)):
    print(q.popleft())