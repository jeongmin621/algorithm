# 1974. 스도쿠 검증

from pprint import pprint

T = int(input())

for test_case in range(1, T + 1):
    # 입력받을 스도쿠 행렬
    sdoku_matrix = []
    for i in range(9):
        row = list(map(int, input().split()))
        sdoku_matrix.append(row)

    # 정답 초기화 (통과하지 못하는 영역이 있다면 정답에 0을 곱해서 0으로 만들기)
    result = 1

    ''' 박스 안 요소들 판별 '''
    # 작은 네모 안에 9개 숫자들 안 겹치는지 판별하기
    for box_i in range(3):  # 작은 네모 시작하는 지점 -> 0 0 0, 1 1 1, 2 2 2
        for box_j in range(3):

            # 판별할 때 사용할 1부터 9까지의 숫자를 담은 리스트
            num_list = []
            for num in range(1, 10):
                num_list.append(num)

            # 박스 안에 1부터 9까지의 숫자가 모두 있는지 판별할 boolean 변수
            box_is = True

            ''' 여기 안에서 부터는 박스 안 요소들 '''
            for box_in_i in range(3):
                for box_in_j in range(3):
                    this_item = sdoku_matrix[3 * box_i + box_in_i][3 * box_j + box_in_j]
                    if this_item in num_list:
                        num_list.remove(this_item)  # 숫자 리스트에 있다면 라스트에서 제거하기

            # 리스트가 비어있지 않다면 해당 박스는 False
            if num_list:
                box_is = False

            # 만약 통과하지 못한 박스가 나온다면 답은 0
            result = result * int(box_is)

    ''' 한 줄 요소들 판별 '''
    # 한 줄 안에 9개의 숫자들 안 겹치는지 판별하기

    # 가로 줄 부터 판별
    for r in range(9):

        # 판별할 때 사용할 1부터 9까지의 숫자를 담은 리스트
        num_list = []

        for num in range(1, 10):
            num_list.append(num)

        # 가로 줄 안에 1부터 9까지의 숫자가 모두 있는지 판별할 boolean 변수
        row_is = True

        for c in range(9):
            if sdoku_matrix[r][c] in num_list:
                num_list.remove(sdoku_matrix[r][c])  # 숫자 리스트에 있다면 제거하기

        # 리스트가 비어있지 않다면 해당 줄은 False
        if num_list:
            row_is = False

        # 만약 통과하지 못한 줄이 나온다면 답은 0
        result = result * int(row_is)

    # 세로 줄 판별
    for r in range(9):

        # 판별할 때 사용할 1부터 9까지의 숫자를 담은 리스트
        num_list = []

        for num in range(1, 10):
            num_list.append(num)

        # 세로 줄 안에 1부터 9까지의 숫자가 모두 있는지 판별할 boolean 변수
        column_is = True

        for c in range(9):
            if sdoku_matrix[c][r] in num_list:
                num_list.remove(sdoku_matrix[c][r])  # 숫자 리스트에 있다면 제거하기

        # 리스트가 비어있지 않다면 해당 줄은 False
        if num_list:
            column_is = False

        # 만약 통과하지 못한 줄이 나온다면 답은 0
        result = result * int(column_is)

    # 스도쿠가 옳은 지 출력
    print(f'#{test_case} {result}')
