#show files in your current directory
from pathlib import Path

p1=Path()
#in Path.glob() give a search pattern in argument
for files in p1.glob('*.py'): #use * for all files of .py(or use .xls, .txt) extension
    print(files)


for files in p1.glob('*.*'): #list all files, '*' means all files in current directory
    print(files) #only shows file not directory

for files in p1.glob('*'):
    print(files) #to show also directory