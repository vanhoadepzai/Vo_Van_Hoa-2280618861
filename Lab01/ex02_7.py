strings = []

while True:
    s = input("Nhập chuỗi (nhập 'done' để kết thúc): ")
    if s.lower() == 'done':
        break
    strings.append(s.upper())

for s in strings:
    print(s)