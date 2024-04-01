from pathlib import Path, PureWindowsPath

# carpeta = Path('C:/Users/JAIRO STYP/OneDrive/Documentos/GITHUB/PYTHON-JS/DAY 6/path/path_ext/file.txt')

# ruta_windows = PureWindowsPath(carpeta)

# if not carpeta.exists():
#     print('Este archivo no existe')
# else:
#     print('Si existe')
base = Path.home()
guia =  Path(base, 'Europa', Path('Barcelona','Sagrada Familia'))
print(base)
print(guia)