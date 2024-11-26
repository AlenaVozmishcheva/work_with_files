import os

relative_path = "data_path_1/test_file_1.txt"
absolute_path = os.path.abspath(relative_path)
print(absolute_path)