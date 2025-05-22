# Chương trình đảo ngược một danh sách

def reverse_list(lst):
    return lst[::-1]

# Ví dụ sử dụng
my_list = [1, 2, 3, 4, 5]
reversed_list = reverse_list(my_list)
print("Danh sách ban đầu:", my_list)
print("Danh sách sau khi đảo ngược:", reversed_list)