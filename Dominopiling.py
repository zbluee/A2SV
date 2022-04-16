#Question -> https://codeforces.com/problemset/problem/50/A


def dominoPilling(m,n):
    return int((m*n)/2)

m,n = list(map(int,input().split()))

print(dominoPilling(m,n))
