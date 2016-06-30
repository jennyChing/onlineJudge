'''
Shortest Path  找不在樹上、離根最近的點，就直接窮舉 d[] 表格，找出最小的 d[b]

10801 - Lift Hopping

You are on floor 0 and would like to get to floor k as quickly as possible. Assume that you do not need to wait to board the first elevator you step into and (for simplicity) the operation of switching an elevator on some floor always takes exactly a minute. Of course, both elevators have to stop at that floor. Calculate the minimum number of seconds required to get from floor 0 to floor k (passing floor k while inside an elevator that does not stop there does not count as “getting to floor k”).
'''
if __name__ == '__main__':
    while True:
        try:
            elev = {}
            n, k = list(map(int, input().split()))
            elev_speed = list(map(int, input().split()))
            for i in range(n):
                elev_floors = set(list(map(int, input().split())))
                elev[elev_speed[i]] = elev_floors
            print(elev)
        except(EOFError):
            break


