def tong(lst):
    """
    Hàm tính tổng các phần tử trong danh sách lst.
    """
    tong = 0
    for i in lst:
        if i%2 == 0:
            tong += i
    return tong
input_list = input("Nhập các số nguyên, ngăn cách bởi dấu phẩy: ")
num= list(map(int, input_list.split(',')))
result = tong(num)  
print(f"Tổng các số chẵn trong danh sách là: {result}")