def trycap(t_data):
    fist=t_data[0]
    second=t_data[-1]   
    return fist, second
input_data = eval(input("Nhập dữ liệu:(1, 2, 3) "))
fist, second = trycap(input_data)
print(f"Phần tử đầu tiên là: {fist}")
print(f"Phần tử thứ hai là: {second}")