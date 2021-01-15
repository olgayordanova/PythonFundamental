path = input()
path_lst = path.split('\\')

file_name, extention = path_lst[len(path_lst)-1].split('.')
print(f"File name: {file_name}")
print(f"File extension: {extention}")

