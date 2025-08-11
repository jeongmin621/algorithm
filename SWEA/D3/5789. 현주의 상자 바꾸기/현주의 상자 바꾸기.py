T = int(input())

for Tc in range(T):
    N, Q = map(int,input().split())
    arr = [0] * N
    for i in range(1,Q+1):
        L, R = map(int, input().split())
        for j in range(L-1,R):
            arr[j] = i
    result = ' '.join(map(str,arr))
    print(f"#{Tc+1} {result}")