T = int(input())

for Tc in range(1,T+1):
    arr= list(map(int, input().split()))
    sum1 = 0
    for i in arr:
        if i % 2== 1:
            sum1 += i
    print(f'#{Tc} {sum1}')