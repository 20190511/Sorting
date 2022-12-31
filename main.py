"""
A23. 안테나
https://www.acmicpc.net/problem/10825

정렬의 중간값에 설치하면 해결되는문제.

"""
n = int(input())
house = list(map(int,input().split()))
mid = (n-1)//2
house.sort()
print(house[mid])
