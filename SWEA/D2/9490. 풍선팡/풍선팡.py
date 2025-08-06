# 9490. 풍선팡

T = int(input())

for test_case in range(1, T + 1):
    # N: 행, M: 열
    N, M = map(int, input().split())

    # 풍선에 든 꽃가루의 개수 (행렬 입력 받기)
    matrix = []
    for _ in range(N):
        row = list(map(int, input().split()))
        matrix.append(row)

    max_sum_v = 0  # 최대 꽃가루 합 초기화

    # 위치 선택
    for row_item in range(N):
        for column_item in range(M):
            sum_v = 0  # 꽃가루 합 초기화

            # 선택한 풍선
            main_position = matrix[row_item][column_item]
            sum_v += main_position

            # 같이 터지는 풍선
            step = main_position  # 선택한 풍선 안에 있는 수만큼 상하좌우 풍선이 터짐
            for i in range(step):

                # step 범위 내, 상 위치에 풍선이 존재한다면 포함
                this_row_item = row_item - i
                if this_row_item > 0:
                    top_position = matrix[this_row_item - 1][column_item]
                    sum_v += top_position

                # step 범위 내, 하 위치에 풍선이 존재한다면 포함
                this_row_item = row_item + i
                if this_row_item < (N - 1):
                    bottom_position = matrix[this_row_item + 1][column_item]
                    sum_v += bottom_position

                # step 범위 내, 좌 위치에 풍선이 존재한다면 포함
                this_column_item = column_item - i
                if this_column_item > 0:
                    left_position = matrix[row_item][this_column_item - 1]
                    sum_v += left_position

                # step 범위 내, 우 위치에 풍선이 존재한다면 포함
                this_column_item = column_item + i
                if this_column_item < (M - 1):
                    right_position = matrix[row_item][this_column_item + 1]
                    sum_v += right_position

            # 현재 꽃가루 합이 최대값보다 크거나 같을 때 최대값 갱신
            if sum_v >= max_sum_v:
                max_sum_v = sum_v

    print(f'#{test_case} {max_sum_v}')
