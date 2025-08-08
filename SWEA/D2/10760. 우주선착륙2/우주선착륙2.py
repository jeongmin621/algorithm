T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    matrix = []
    for _ in range(N):
        row = list(map(int, input().split()))
        matrix.append(row)

    result = 0

    for i in range(N):
        for j in range(M):
            # 착륙지: [i, j]

            lower_item_list = []    # 착륙지 보다 낮은 영역들만 담을 리스트
            for di in range(-1, 2):
                for dj in range(-1, 2):

                    # 자기 자신은 제외
                    if di == 0 and dj == 0:
                        continue

                    if 0 <= (i + di) < N and 0 <= (j + dj) < M:
                        if matrix[i + di][j + dj] < matrix[i][j]:
                            lower_item_list.append(matrix[i + di][j + dj])

            if len(lower_item_list) >= 4:
                result += 1

    print(f'#{test_case} {result}')