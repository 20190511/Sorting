"""
국영수
https://www.acmicpc.net/problem/10825


<피드백>
1. 내림차순은 input data를 애초에 -붙여서 넣으면 편하다.
2. sorted(array,key=lambda x:(x[0],x[-1],...))
"""

n = int(input())
database = []
for i in range(n):
  name,kor,eng,mat = input().split()
  database.append([-int(kor),int(eng),-int(mat),name])

database.sort()
#database = sorted(database,key=lambda x:(-x[0],x[1],-x[2],x[3]))
for i in range(n):
  print(database[i][3])