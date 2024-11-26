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
print()

new_dir = "data_path_2/new_folder"
os.mkdir(new_dir)
path = os.path.join(os.getcwd(), "data_path_2", "new_folder")
print(f"Путь к созданной папке: {path}")

os.rmdir("data_path_2/new_folder")
print()


""""Текст для задания:

Если б мишки были пчелами,
То они бы нипочем,
Никогда и не подумали,
Так высоко строить дом.

1.Вам необходимо написать функцию которая запишет в
файл следующий текст. Записать должно именно так как
указано в задании (а именно не сплошной текст а несколько
строк в столбик).

2.Вам необходимо написать функцию которая бы считала
текст из созданного вами в первом задании файла и вывела
результат в консоль. Вывести его нужно именно так как и
было записано, построчно без разрывов между строками."""

def write_text():
    with open('data_path_1/test_file_1.txt', 'w', encoding='utf-8')as file:
        file.write('Если б мишки были пчелами,\n')
        file.write('То они бы нипочем,\n')
        file.write('Никогда и не подумали,\n')
        file.write('Так высоко строить дом.')
    return
write_text()




