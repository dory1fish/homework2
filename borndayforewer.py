while True:
    age = int(input('В каком году родился Пушкин?'))
    day = None
    if age == 1799:
        day = int(input('Какого числа родился Пушкин?'))
        while day != 26:
            day = int(input('Какого числа родился Пушкин?'))
        break
print('Верно')
