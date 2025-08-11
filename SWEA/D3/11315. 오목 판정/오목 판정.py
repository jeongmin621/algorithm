# 11315. 오목판정

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    board = []
    for _ in range(N):
        row = list(map(str, input().strip()))
        board.append(row)

    result = False

    for i in range(N):
        for j in range(N):
            # 기준점에 돌이 있다면 판별 시작
            if board[i][j] == 'o':
                r_cnt, c_cnt, rc1_cnt, rc2_cnt = 0, 0, 0, 0
                for d in range(4):
                    if j < N - 4 and board[i][j + d] == board[i][j + d + 1]:
                        r_cnt += 1
                    if i < N - 4 and board[i + d][j] == board[i + d + 1][j]:
                        c_cnt += 1
                    if i < N - 4 and j < N - 4 and board[i + d][j + d] == board[i + d + 1][j + d + 1]:
                        rc1_cnt += 1
                    if i > 3 and j < N - 4 and board[i - d][j + d] == board[i - d - 1][j + d + 1]:
                        rc2_cnt += 1

                if r_cnt == 4 or c_cnt == 4 or rc1_cnt == 4 or rc2_cnt == 4:
                    result = True
                if result:
                    break

    if result:
        total_result = 'YES'
    else:
        total_result = 'NO'

    print(f'#{test_case} {total_result}')
