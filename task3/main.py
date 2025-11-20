rows = []
with open('learning_python.txt', 'r', encoding='utf-8') as f:
    for line in f.readlines():
        rows.append(line.strip())
rows.sort(key=len)
for row in rows:
    print(row)