# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

my_str = 'АБВ ылоажы фыыдлх абв Зщышф вабвв ффлжв абВ'
my_list = my_str.split()
new_str = ' '.join(list(map(lambda elem: "" if 'абв' in elem.lower() else elem, my_list)))
print(new_str)
