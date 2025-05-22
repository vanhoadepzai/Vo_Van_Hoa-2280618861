import re

s = "-100#^sdfkj8902w3ir021@swf-20"

# Tìm tất cả các số nguyên trong chuỗi, bao gồm cả số âm
numbers = re.findall(r'-?\d+', s)
sum_pos = sum(int(n) for n in numbers if int(n) > 0)
sum_neg = sum(int(n) for n in numbers if int(n) < 0)

print("Giá trị dương:", sum_pos)
print("Giá trị âm:", sum_neg)