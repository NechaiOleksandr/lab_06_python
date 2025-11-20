import os
import datetime

def getCurrentTime():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

if not os.path.exists('guest_book.txt'):
    with open('guest_book.txt', 'w', encoding='utf-8') as f:
        f.write(f'Файл створено: {getCurrentTime()}\nОстання зміна: {getCurrentTime()}\n\n')

while True:
    name = input("Введіть ім'я (end щоб вийти): ")
    if name == 'end':
        break

    text = f'{getCurrentTime()} > Вітаю, {name}\n'
    print(text)
    with open('guest_book.txt', 'r+', encoding='utf-8') as f:
        lines = f.readlines()
        lines[1] = f'Остання зміна: {getCurrentTime()}\n'
        f.seek(0)
        f.writelines(lines)
        f.write(text)