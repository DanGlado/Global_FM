import os
print("Добро пожаловать в найстройки Файлового Менеджера \n")
print("Текущая рабочая папка: ", os.getcwd())
wd = input("Установите корневую директорию (ввести полный путь): ")
def get_wd(wd):
    try:
        os.chdir(wd)
    except FileNotFoundError:
        print("Создана новая директория!")
        os.mkdir(wd)
        os.chdir(wd)

get_wd(wd)
print("Текущая рабочая папка: ", os.getcwd())