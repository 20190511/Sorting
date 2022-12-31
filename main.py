"""
카드정렬
https://www.acmicpc.net/problem/1715

 <<피드백>>
  1. 계속해서 Sorting되는 자료구조를 얻고싶다면 우선순위 큐를 이용하는 것이 편하다.

 <<heapq 사용법>>
 heap = [5,4,6,2,4,6,4]
  ->해당 리스트(heap)가 heapq 객체에 heap 형태로 들어가있다.
  
 heapq.heapify(heap)
 heapq.heappush(heap,data)
 heapq.heappop(heap)


  ex)
  heap = []
  heapq.heappush(heap,4)
  heapq.heappush(heap,3)
  heapq.heappush(heap,2)
  heap.pop()
  heap.append(1)
  print(heap)
  #1이 마지막에 들어간상태로 삭제하고 힙 재형성
  heapq.heappop(heap) 
  print(heap)

  >>
  [2, 4, 1]
  [1, 4]

"""
import heapq
n = int(input())
heap = []
for i in range(n):
  data = int(input())
  heapq.heappush(heap,data)
result = 0
while len(heap) > 1:
  print(heap)
  one = heapq.heappop(heap)
  two = heapq.heappop(heap)
  sums = one+two
  result += sums
  heapq.heappush(heap,sums)

print(result)
  
"""
아래 방식대로 풀 수 있으나, 시간이 초과됨.
n = int(input())
card = []
for i in range(n):
  card.append(int(input()))

card.sort(reverse=True)

sums = 0
while len(card)>2:
  curr = card[-1]+card[-2]
  sums += curr
  card.pop()
  card.pop()
  card.append(curr)
  card.sort(reverse=True)

print(sums+card[-1]+card[-2])

"""