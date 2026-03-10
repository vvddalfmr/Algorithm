import sys
import heapq

def solution():
    input = sys.stdin.readline
    
    n = int(input())
    max_heap = []
    
    for _ in range(n):
        x = int(input())
        
        if x == 0:
            if not max_heap:
                print(0)
            else:
                print(-heapq.heappop(max_heap))
        else:
            heapq.heappush(max_heap, -x)

if __name__ == '__main__':
    solution()