import os

# Directorio de archivos
os.chdir('C:\\Users\\marti\\OneDrive\\Desktop\\Data CMF\\Pdfs\\Hechos Esenciales\\Marzo 2016 - Marzo 2010')

i = 0

# Renombrar listado de archivos definidos
for file in os.listdir():

    # Al nuevo archivo de le aplicara el nombre entre "", mas un n° secuenciado
    new_file_name = "Archivo-{}.pdf". format(i) # Nombre de archivo y formato
    os.rename(file, new_file_name)

    i = i +1