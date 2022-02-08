# Программа переводит текст из файла .srt на русский язык
# Максимально колличество символов для перевода 15114*2
# Для перевода нужно указать полный путь к файлу
# Новый файл с переводом сохраняется в директорию с оригинальным файлом
# новый файл с переводом это готовый файл субтитров готовый к использованию

import googletrans
import re
from googletrans import Translator
translator = Translator()



f = r'D:\Desktop\Python and Django Full Stack Web Developer Bootcamp Course\03 HTML Level One - Basics\010 HTML Level One -Part Three - Lists-en.srt'
with open(f, 'r') as old_file:
    content_old = old_file.readlines()


    
def full_path(open_path_old):
    old_name_file = open_path_old
    len_a = int(len(old_name_file))
    c = len_a - old_name_file[::-1].find('\\')
    # Name of new file
    new_name_file = old_name_file[c:len_a].replace("-en", "-ru(3)")
        # path to save new file
    path_save_file = old_name_file[:c]
    full_path = path_save_file + new_name_file
    return full_path

# извлекаем строки с буквами на англ языке и записываем в новую переменную (строку с переносами)
new_file = []
for x in content_old:
    if re.findall("[a-zA-Z]", x):
        new_file.append(x)

new_file_len = int(len(new_file))
new_file_half = int(new_file_len / 2)
new_file_01 = new_file[:new_file_half]
new_file_02 = new_file[new_file_half:]

# перевод текста с англ на рус
result_01 = translator.translate("".join(new_file_01), dest='ru')
trans_file_01 = result_01.text

result_02 = translator.translate("".join(new_file_02), dest='ru')
trans_file_02 = result_02.text

trans_file = trans_file_01 +"\n" + trans_file_02
trans_file_line = trans_file.splitlines()

finish_file = ""
count_index = 0
for y in content_old:
    if re.findall("[a-zA-Z]", y):
        finish_file += trans_file_line[count_index] + "\n"
        count_index += 1
    else:
        finish_file += y

with open(full_path(f), 'w') as save_file:
    save_file.write(finish_file)


print("Finish translate")

