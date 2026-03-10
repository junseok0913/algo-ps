'''
입력으로 인한 시간초과
'''
import sys
input = sys.stdin.readline

num_list = []
n = int(input())

for i in range(n):
    num_list.append(int(input()))

print('\n'.join(map(str, sorted(num_list))))