import heapq

T = int(input())

for _ in range(T):

    n = int(input())
    arr = [list(map(int, input().split())) for _ in range((n // 10) + 1)]
    # n은 늘 홀수인 것을 고려하여 arr에 입력 받기

    min_heap = []
    max_heap = []
    result = []  # 홀수 번째마다 중앙값 저장할 리스트 생성
    # n이 10보다 작을때 arr 순회하며 각 pq에 추가
    if n < 10:
        for idx in range(n):
            if not max_heap or arr[0][idx] <= -1 * max_heap[0]:
                heapq.heappush(max_heap, -1 * arr[0][idx])
            else:
                heapq.heappush(min_heap, arr[0][idx])
            # 최소힙 최대힙 균형 맞추기
            if len(max_heap) > len(min_heap) + 1:
                heapq.heappush(min_heap, -1 * heapq.heappop(max_heap))
            elif len(min_heap) > len(max_heap):
                heapq.heappush(max_heap, -1 * heapq.heappop(min_heap))

            if (idx+1) % 2 == 1:
                result.append(-1 * max_heap[0])
    # n이 10이상 일때 arr 순회하며 각 pq에 추가
    else:
        for idx in range(n//10 + 1):
            for i in range(len(arr[idx])):
                if not max_heap or arr[idx][i] <= - max_heap[0]:
                    heapq.heappush(max_heap, -1 * arr[idx][i])
                else:
                    heapq.heappush(min_heap, arr[idx][i])
                # 최소힙 최대힙 균형 맞추기
                if len(max_heap) > len(min_heap) + 1:
                    heapq.heappush(min_heap, -1 * heapq.heappop(max_heap))
                elif len(min_heap) > len(max_heap):
                    heapq.heappush(max_heap, -1 * heapq.heappop(min_heap))

                if (i+1) % 2 == 1:
                    result.append(-1 * max_heap[0])
    # 여태 구한 중앙 값 개수 먼저 출력
    print(len(result))
    # result의 길이에 따라 중앙값들 순서대로 출력
    if len(result) < 10:
        for idx in range(len(result)):
            print(result[idx], end=' ')
        print()
    elif len(result) % 10 == 0:
        for idx in range(len(result)//10):
            for i in range(10):
                print(result[10*idx+i], end=' ')
            print()
    else:
        for idx in range(0, len(result), 10):
            print(*result[idx:idx+10])