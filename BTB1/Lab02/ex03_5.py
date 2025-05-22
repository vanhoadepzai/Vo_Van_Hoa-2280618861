# Đếm số lần xuất hiện của mỗi phần tử trong một list và lưu vào dictionary

def count_elements(lst):
    result = {}
    for item in lst:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result

# Nhập list từ bàn phím
input_str = input("Nhập các phần tử của list, cách nhau bởi dấu cách: ")
my_list = input_str.split()
# Nếu muốn chuyển sang số nguyên:
# my_list = [int(x) for x in input_str.split()]

counts = count_elements(my_list)
print(counts)