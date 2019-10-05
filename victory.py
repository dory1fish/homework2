while True :
    age1 = int(input('Год рождения Джессики Честейн?'))
    # 1977

    age2 = int(input('Год рождения Блейк Лайвли?'))
    # 1987

    age3 = int(input('Год рождения Скарлетт Йоханссон?'))
    # 1984

    age4 = int(input('Год рождения Софи Тёрнер?'))
    # 1996

    age5 = int(input('Год рождения Эмилии Кларк?'))
    # 1986
    right_answers = 0

    if age1 == 1977:
        right_answers += 1

    if age2 == 1987:
        right_answers += 1

    if age3 == 1984:
        right_answers += 1

    if age4 == 1996:
        right_answers += 1

    if age5 == 1986:
        right_answers += 1

    all_answers = 5
    print('правильных ответов: ', right_answers)
    print('неправильных ответов: ', all_answers - right_answers)
    print('% правильных ответов: ', right_answers * 100 // all_answers)
    print('% неправильных ответов: ', (all_answers - right_answers) * 100 // all_answers)

    question = input('Хотите ли начать игру сначала?')
    if question == 'нет':
        break