# 20551. 증가하는 사탕 수열

T = int(input())

for tc in range(1, T + 1):
    A, B, C = map(int, input().split())

    result = 0

    if A >= 1 and B >= 2 and C >= 3:
        while not A < B < C:
            while not B < C:
                B -= 1
                result += 1
            while not A < B:
                A -= 1
                result += 1

    else:
        result = -1

    print(f'#{tc} {result}')