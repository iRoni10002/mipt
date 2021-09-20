import zipfile
import os

path_ = input()
flg = True
while flg:
    try:
        os.chdir(os.path.abspath(path_))
        flg = False
    except OSError:
        print('ERROR: Could not find  the directory')
        path_ = input()

namedir_ = input()
flg = True
while flg:
    try:
        with zipfile.ZipFile(namedir_, 'r') as zip:
            zip.extractall(namedir_[::-4])
            flg = False
    except OSError:
        print('ERROR: Could not find the directory')
        namedir_ = input()

arr = []
for cur_dir, dirs, files in os.walk('.'):
    if str(files).count('.py'):
        print(cur_dir)
        arr.append(cur_dir)
arr.sort()

with open('aboba3.txt', 'w') as file:
    file.write('\n'.join(arr))
    file.close()
