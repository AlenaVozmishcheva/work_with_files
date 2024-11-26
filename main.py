import os

relative_path = "data_path_1/test_file_1.txt"
absolute_path = os.path.abspath(relative_path)
print(absolute_path)

for folders in os.walk("."):
    print(f"Папки: {folders}")
for files in os.walk("."):
    print(f"Файлы: {files}")
