lines = []
with open('learning_python.txt', 'r', encoding='utf-8') as f:
    for line in f.readlines():
        lines.append(line.strip())
lines.sort(key=len)
for line in lines:
    print(line)