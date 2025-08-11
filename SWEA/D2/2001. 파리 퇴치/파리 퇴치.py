# 2001. 파리퇴치

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())  # (N X N): 영역, (M X M): 파리채의 크기

    matrix = []
    for _ in range(N):
        row = list(map(int, input().split()))
        matrix.append(row)

    max_sum_v = 0
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            # 전체 영역 중에서 파리채가 칠 수 있는 영역
            sum_v = 0
            for mi in range(M):
                for mj in range(M):
                    sum_v += matrix[i + mi][j + mj]
            if sum_v >= max_sum_v:
                max_sum_v = sum_v

    print(f'#{test_case} {max_sum_v}')
