# 10760. 우주선착륙2

T = int(input())

for test_case in range(1, T + 1):
    # N: 구역의 행, M: 구역의 열
    N, M = map(int, input().split())

    matrix = []
    for _ in range(N):
        row = list(map(int, input().split()))
        matrix.append(row)

    result = 0

    for i in range(N):
        for j in range(M):
            ''' 착륙지는 [i, j] 부분 '''
            count = 0   # 조건을 만족하는 주변 영역들의 개수를 셀 변수
            item_list = []  # 착륙지 주변 영역들을 담을 리스트
            lower_list = []   # 착륙지 보다 더 낮은 주변 영역들을 담을 리스트

            for item_i in range(-1, 2):
                for item_j in range(-1, 2):

                    # 자기 자신은 제외
                    if item_i == 0 and item_j == 0:
                        continue
                    # 전체 범위 내에서만, 주변 영역들을 리스트에 담기
                    if 0 <= (i + item_i) < N and 0 <= (j + item_j) < M:
                        item_list.append(matrix[i + item_i][j + item_j])

            # 영역 리스트 순회하면서 조건에 맞는 영역들의 개수가 4개 이상이면 카운트
            for idx in range(len(item_list)):
                if matrix[i][j] > item_list[idx]:
                    lower_list.append(item_list[idx])
                    count += 1

            # 카운트가 4개 이상이면 후보지에 포함
            if count >= 4:
                result += 1

    # 후보지 개수 출력
    print(f'#{test_case} {result}')
