import sys
input =sys.stdin.readline

k = int(input())
quest = list(input().split())

def dfs_max(idx, temp):
    global max_flag, max_result
    if max_flag:
        return    

    if len(max_result) == k+1:
        max_flag = True
        print(max_result)
        return

    for i in range(9,-1,-1):
        if not visited[i]:
            if quest[idx] == '>':
                if temp > i:     
                    max_result += str(i)
                    visited[i] = 1             
                    dfs_max(idx+1, i)
                    visited[i] = 0
                    max_result = max_result[:-1]
            else:
                if temp < i:
                    max_result += str(i)
                    visited[i] = 1             
                    dfs_max(idx+1, i)
                    visited[i] = 0
                    max_result = max_result[:-1]


def dfs_min(idx, temp):
    global min_flag, min_result
    if min_flag:
        return    

    if len(min_result) == k+1:
        min_flag = True
        print(min_result)
        return

    for i in range(10):
        if not visited[i]:
            if quest[idx] == '>':
                if temp > i:     
                    min_result += str(i)
                    visited[i] = 1             
                    dfs_min(idx+1, i)
                    visited[i] = 0
                    min_result = min_result[:-1]
            else:
                if temp < i:
                    min_result += str(i)
                    visited[i] = 1             
                    dfs_min(idx+1, i)
                    visited[i] = 0
                    min_result = min_result[:-1]

visited = [0] * 10  
max_result = ''
max_flag = False
for i in range(9,-1,-1):
    max_result += str(i)
    visited[i] = 1
    dfs_max(0,i)
    visited[i] = 0
    max_result = max_result[:-1]


visited = [0] * 10
min_result = ''
min_flag = False
for i in range(10):
    min_result += str(i)
    visited[i] = 1
    dfs_min(0,i)
    visited[i] = 0
    min_result = min_result[:-1]