# Nhập chuỗi số nhị phân, ngăn cách bởi dấu phẩy
numbers = input("Nhập các số nhị phân 4 ký tự, ngăn cách bởi dấu phẩy: ").split(',')

# Kiểm tra và in kết quả
for num_str in numbers:
    num_str = num_str.strip()
    if len(num_str) == 4 and all(c in '01' for c in num_str):
        num = int(num_str, 2)
        if num % 5 == 0:
            print(f"{num_str} ({num}) chia hết cho 5")
        else:
            print(f"{num_str} ({num}) không chia hết cho 5")
    else:
        print(f"'{num_str}' không phải là chuỗi nhị phân 4 ký tự hợp lệ")