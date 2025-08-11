# 1979. 단어 퍼즐

from pprint import pprint

T = int(input())

for test_case in range(1, T + 1):
    # N:  퍼즐 가로 세로 길이, K: 단어의 길이
    N, K = map(int, input().split())
    matrix = []
    for _ in range(N):
        row = list(map(int, input().split()))
        matrix.append(row)
    # pprint(matrix)

    result = 0

    # 가로 방향일 때
    for i in range(N):
        for j in range(N - K + 1):
            # 첫 번째 칸이거나 바로 이전 칸이 0일 경우에만
            if j == 0 or (j >= 1 and matrix[i][j - 1] == 0):
                # 1인지 판별
                if matrix[i][j] == 1:
                    row_count = 0
                    # 현재 칸부터 가로 방향으로 K 칸을 다 더하면 K가 되는 지
                    for plus_item in range(K):
                        row_count += matrix[i][j + plus_item]

                    # 1이 연달아 K개인 경우에, 마지막 칸이거나 다음 칸이 0일 경우에만
                    if row_count == K:
                        if (j + K) == N or (j + K < N and matrix[i][j + K] == 0):
                            result += 1
                            # print(f'[{i},{j}]에서 가로방향으로 길이 {K}의 단어 들어갈 수 있음')

    # 세로 방향일 때
    for i in range(N - K + 1):
        for j in range(N):
            # 첫 번째 칸이거나 바로 이전 칸이 0일 경우에만
            if i == 0 or (i >= 1 and matrix[i - 1][j] == 0):
                # 1인지 판별
                if matrix[i][j] == 1:
                    column_count = 0
                    # 현재 칸부터 세로 방향으로 K 칸을 다 더하면 K가 되는 지
                    for plus_item in range(K):
                        column_count += matrix[i + plus_item][j]

                    # 1이 연달아 K개인 경우에, 마지막 칸이거나 다음 칸이 0일 경우에만
                    if column_count == K:
                        if (i + K) == N or (i + K < N and matrix[i + K][j] == 0):
                            result += 1
                            # print(f'[{i},{j}]에서 세로방향으로 길이 {K}의 단어 들어갈 수 있음')

    print(f'#{test_case} {result}')
