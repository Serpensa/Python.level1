Задача-1:
#Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os
def create_directory()
n=1
while n<10
		dir_path = os.path.join(os.getcwd(), ("dir_" + str(n)))
		try:
			os.mkdir(dir_path)
		except FileExistsError:
			print('Такая директория уже существует')
	n+=1



import os
def delete_directory()
n=1
while n<10
		dir_path = os.path.join(os.getcwd(), ("dir_" + str(n)))
		try:
			os.rmdir(dir_path)
		except FileExistsError:
			print('Такая директория не существует')
	n+=1

create_directory()
delete_directory()


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

import os
 def show_dirs():
 	current_dirs = [os.listdir(os.path.join(os.getcwd()))]
    print(current_dirs)
 
 show_dirs()

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
import os
import shutil
 def copy_file():

        shutil.copyfile=(file, (file+'copy'))
    
copy_file()



def go_to_dir(path):
    os.chdir(path)