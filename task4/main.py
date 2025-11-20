import os

os.makedirs('analysis', exist_ok=True)
newText = []
with open('learning_python.txt', 'r', encoding='utf-8') as f:
    for line in f.readlines():
        line = line.replace('Python', 'C')
        newText.append(line)

with open('learning_c.txt', 'w', encoding='utf-8') as f:
        f.write(''.join(newText))

trueF = os.path.join('analysis', 'true.txt')
falseF = os.path.join('analysis', 'false.txt')
true, false = [], []

for line in newText:
    print(line.strip())
    ok = False
    while not ok:
        answer = input('Твердження істинне? (так/ні)\n').lower()
        if answer == 'так' or answer == 'ні':
            ok = True
        else:
            print('Помилка, повторіть ще раз')
        if answer == 'так':
            true.append(line)
        else:
            false.append(line)

with open(trueF, 'w', encoding='utf-8') as f:
    f.write(''.join(true))
with open(falseF, 'w', encoding='utf-8') as f:
    f.write(''.join(false))