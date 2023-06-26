"""Напишите функцию группового переименования файлов. Она должна:
принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
принимать параметр количество цифр в порядковом номере.
принимать параметр расширение исходного файла.
Переименование должно работать только для этих файлов внутри каталога.
принимать параметр расширение конечного файла.
принимать диапазон сохраняемого оригинального имени.
Например, для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
3. Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами."""
import os


def rename_files(begin_extention: str, end_extention: str, folder: str, amount_numbers: int = 1, diapason=None,
                 name: str = 'file'):
    os.chdir(folder)
    if diapason is None:
        diapason = [0, 3]
    file_num = 10 ** (amount_numbers - 1)
    new_file = []
    for fl in os.listdir(path=folder):
        #print(fl)
        if fl.endswith(begin_extention):
            new_file.append(name[diapason[0]:diapason[1] + 1])
            new_file.append(str(file_num))
            new_file.append(".")
            new_file.append(end_extention)
            new_name = "".join(new_file)
            os.renames(fl, new_name)
            print(f"Переименован файл {fl} в {new_name}")
            file_num += 1
        new_file.clear()


rename_files("pdf", "doc", r'C:\Users\gusev\OneDrive\JAVA_GEEK_BRAINS\python углубление\Seminar_7\data', 2, [1, 7], 'newfile')
