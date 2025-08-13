# 4047. 영준이의 카드 카운팅

T = int(input())

for tc in range(1, T + 1):
    S = list(map(str, input().strip()))  # TXY -> T: 무늬, XY: 숫자

    # 한 덱의 카드 dict 만들기
    card = {}
    card_T = ['S', 'D', 'H', 'C']
    for i in range(4):
        card[card_T[i]] = []
        for j in range(1, 14):
            card[card_T[i]].append(j)

    result = True

    for idx in range(0, len(S), 3):
        # 카드의 무늬 -> 인덱스가 0이거나 3의 배수인 경우만 골라서
        this_card_T = S[idx]
        # 그 카드의 숫자
        num_str = []
        for d in range(1, 3):
            num_str.append(S[idx + d])
        num = int(''.join(num_str))

        # dict 에서 빼기
        if num in card[this_card_T]:
            card[this_card_T].remove(num)
        else:
            result = False

    result_list = []
    for num_list in list(card.values()):
        result_list.append(len(num_list))
    if result:
        result = str(result_list).replace(',', '')[1:-1]
    else:
        result = 'ERROR'

    print(f'#{tc} {result}')

