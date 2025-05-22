# Xóa một phần tử khỏi dictionary theo key

# Khởi tạo dictionary mẫu
my_dict = {
    'name': 'Hoa',
    'age': 20,
    'class': 'Python'
}

# Nhập key cần xóa
key_to_delete = input("Nhập key cần xóa: ")

# Kiểm tra và xóa key nếu tồn tại
if key_to_delete in my_dict:
    del my_dict[key_to_delete]
    print(f"Đã xóa key '{key_to_delete}'.")
else:
    print(f"Key '{key_to_delete}' không tồn tại trong dictionary.")

# In dictionary sau khi xóa
print("Dictionary sau khi xóa:", my_dict)