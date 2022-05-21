#question => https://codeforces.com/problemset/problem/1/A
import math
def countFlagstones(m, n, a):
    #Theatre Square -> n × m  flagstones -> a × a
    return math.ceil(m/a) * math.ceil(n/a)
