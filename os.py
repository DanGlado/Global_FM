from settings import *
print("Список команд для ввода:"
"\n1 - crdir [dir name] - Создание папки (с указанием имени)"
"\n2 - deldir [dir name] - Удаление папки по имени"
"\n3 - cddir [dir name] - cddir .. - Перемещение между папками (в пределах рабочей папки) - заход в папку по имени, выход на уровень вверх"
"\n4 - mkfile [filename1 filename2 ...] - Создание пустых файлов с указанием имени"
"\n5 - wrfile [filename]- Запись текста в файл"
"\n6 - catfile [filename]- Просмотр содержимого текстового файла"
"\n7 - rm [filename1 filename2 ...] - Удаление файлов по имени"
"\n8 - cpfile [filename1 filename2 ...] - Копирование файлов из одной папки в другую"
"\n9 - mvfile [filename1 filename2 ...] - Перемещение файлов"
"\n10 - renamef [filename] [new_filename] - Переименование файлов")

command = input("Введите команду: ")
all_commands = ["crdir", "deldir", "cddir", "mkfile", "wrfile", "catfile", "rm", "cpfile", "mvfile", "renamef"]
node = os.path.abspath(wd)
def crdir(dirname):
    print("Создание папки...")
    os.mkdir(node+"\\"+dirname)


while command != 'exit':
    lis = command.split()
    if lis[0] in all_commands and len(lis) > 1:
        if lis[0] == "crdir":
            try:
                crdir(lis[1])
            except FileExistsError:
                print('Директория с таким названием уже существует!')
        elif lis[0] == "deldir":

            pass
        elif lis[0] == "cddir":
            pass
        elif lis[0] == "mkfile":
            pass
        elif lis[0] == "wrfile":
            pass
        elif lis[0] == "catfile":
            pass
        elif lis[0] == "rm":
            pass
        elif lis[0] == "cpfile":
            pass
        elif lis[0] == "mvfile":
            pass
        elif lis[0] == "renamef":
            pass
    else:
        print("Проверьте наличие синтаксической ошибки в команде и корректность аргументов!")
    command = input("Введите команду: ")
