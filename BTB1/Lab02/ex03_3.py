# Nhập một chuỗi các phần tử, cách nhau bởi dấu phẩy
input_str = input("Nhập các phần tử của list, cách nhau bởi dấu phẩy: ")
# Tạo list từ chuỗi nhập vào
lst = input_str.split(',')
# Tạo tuple từ list
tpl = tuple(lst)
print("Tuple:", tpl)
# Đảo ngược tuple
reversed_tpl = tpl[::-1]
print("Tuple sau khi đảo ngược:", reversed_tpl)