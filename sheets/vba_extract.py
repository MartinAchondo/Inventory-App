import os
import shutil
from zipfile import ZipFile

def extraer(book_name):
    book = 'vba_' + book_name + '.xlsm'
    path_book = os.path.join(os.getcwd(),'sheets','vba_xlsm',book)
    book2 = book.replace('xlsm','zip')
    path_book2 = os.path.join(os.getcwd(),'sheets','vba_xlsm',book2)
    shutil.copy(path_book,path_book2)
    with ZipFile(path_book2, 'r') as zipObj:
    # Get a list of all archived file names from the zip
        listOfFileNames = zipObj.namelist()
        # Iterate over the file names
        for fileName in listOfFileNames:
            # Check filename endswith csv
            if fileName.endswith('vbaProject.bin'):
                # Extract a single file from zip
                new_path = os.path.join(os.getcwd(),'sheets','bin_vbaprojects')
                zipObj.extract(fileName, new_path)
                new_path1 = os.path.join(new_path,fileName)
                name = 'vbaProject_' + book_name + '.bin'
                new_path2 = os.path.join(new_path,name)
                os.remove(new_path2)
                os.rename(new_path1,new_path2)
    os.remove(path_book2)


if __name__=='__main__':

    extraer('inventario')
    extraer('ventas')
    extraer('historial')
    extraer('tienda')
    extraer('fotos')