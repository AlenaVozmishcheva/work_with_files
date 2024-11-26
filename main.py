import os

relative_path = "data_path_1/test_file_1.txt"
absolute_path = os.path.abspath(relative_path)
print(f"Нормализованный абсолютный путь к файлу test_file_1.txt {absolute_path}")
print()

for folders in os.walk("."):
    print(f"Папки: {folders}")
for files in os.walk("."):
    print(f"Файлы: {files}")
print()

my_cwd = os.getcwd()
base_dir = "data_path_2"
file_name = "test_file_3.txt"
full_path = os.path.join(my_cwd, base_dir, file_name)
print(f"Нормализованный абсолютный путь к файлу test_file_3.txt {full_path}")
print()

full_path_1 = os.path.join(os.getcwd(), "data_path_2", "test_file_3.txt")
print(f"Нормализованный абсолютный путь к файлу test_file_3.txt {full_path_1}")
