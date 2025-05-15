# Tìm các số trong khoảng 2000 đến 3200 chia hết cho 7 nhưng không phải bội của 5

result = []
for i in range(2000, 3201):
    if i % 7 == 0 and i % 5 != 0:
        result.append(i)

print(result)