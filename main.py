"""
A25. 실패율
https://school.programmers.co.kr/learn/courses/30/lessons/42889

피드백
 0. Stages를 Sort를 해서 푸는것 보다 -> .count() 하는 것이 더 빠르다.
 1. 이중리스트의 열 값만 가져오고 싶다면 다음과 같이 작성한다.
    results = [item[0] for item in result]
 2. 리스트 원소개수
  list.count()를 쓰면 구할 수 있다.
"""


def solution(N, stages):
    result = []
    total = len(stages)
    for i in range(1,N+1):
        count = stages.count(i)
        if count == 0:
            result.append((i,0))
        else:
            result.append((i,count/total))
            total -= count
    result = sorted(result, key=lambda x:(-x[1]))
    results = [item[0] for item in result]
    """
    for i in range(N):
        results.append(result[i][0])
    """
    return results

n1 = 5
stages1 = [2, 1, 2, 6, 2, 4, 3, 3]
n2 = 4
stages2 = [4,4,4,4,4]
print(solution(n1,stages1))
print(solution(n2,stages2))