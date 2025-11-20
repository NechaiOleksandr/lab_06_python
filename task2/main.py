print('Введіть числа (end щоб вийти):')
while True:
    text = input()
    if text == "end":
        break
    try:
        text = int(text)
    except ValueError:
        print('Помилка')
        continue
    with open('numbers.txt', 'a', encoding='utf-8') as f:
        f.write(f'{text}')
        f.write(' - парне\n' if text % 2 == 0 else ' - непарне\n')