
T = int(input())

for tc in range(1, T + 1):
    # 카드 한 덱 dict 만들기
    card_T = ['S', 'D', 'H', 'C']
    card_dict = {}
    for t in card_T:
        card_dict[t] = []
        for num in range(1, 14):
            card_dict[t].append(num)

    S = list(map(str, input().strip()))

    is_duplicate = False

    # 문자열의 인덱스가 0 또는 3의 배수인 문자는 카드의 무늬
    for i in range(0, len(S), 3):
        key = S[i]

        # 그 다음 두 칸은 카드의 숫자
        num = 0
        for j in range(1, 3):
            num *= 10
            num += int(S[i + j])

        # 딕셔너리에 있으면 지우고 없으면 중복 판정
        if num in card_dict[key]:
            card_dict[key].remove(num)
        else:
            is_duplicate = True

    result_list = []
    for num_list in card_dict.values():
        result_list.append(len(num_list))

    result = ''
    if is_duplicate:
        result = 'ERROR'
    else:
        result = str(result_list).replace(',', '')[1:-1]

    print(f'#{tc} {result}')
