import sys
sys.stdin = open('input.txt')
from pprint import pprint

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    case = list(map(int, input().split()))
    max_p = case[-1]
    for i in