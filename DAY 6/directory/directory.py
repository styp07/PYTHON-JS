import os
from pathlib import Path

folder = Path('C:/Users/JAIRO STYP/OneDrive/Documentos/GITHUB/PYTHON-JS/DAY 6/directory/directory_alter')
file = folder / 'file.txt'

mi_file = open(file)
print(mi_file.read())
mi_file.close()
# path = os.chdir('C:\\Users\\JAIRO STYP\\OneDrive\\Documentos\\GITHUB\\PYTHON-JS\\DAY 6\\directory\\directory_alter')

#path = os.makedirs('C:\\Users\\JAIRO STYP\\OneDrive\\Documentos\\GITHUB\\PYTHON-JS\\DAY 6\\directory\\directory_alter\\next')

#os.rmdir('C:\\Users\\JAIRO STYP\\OneDrive\\Documentos\\GITHUB\\PYTHON-JS\\DAY 6\\directory\\directory_alter\\next')