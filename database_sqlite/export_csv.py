import os
import csv

try:
    import base as db
    import crud as crd
except:
    pass

def export(connectionn):
    root = os.getcwd()
    root = os.path.join(root,'base','csv')
    path1 = os.path.join(root,'Inventario.csv')
    with open(path1, 'w', newline='') as file:
        writer = csv.writer(file)
        row_list = crd.get_todos('inventario',connectionn)
        writer.writerows(row_list)

    path2 = os.path.join(root,'Ventas.csv')
    with open(path2, 'w', newline='') as file:
        writer = csv.writer(file)
        row_list = crd.get_todos('ventas',connectionn)
        writer.writerows(row_list)

if __name__=='__main__':
    try:
        export(db.create_connection)
    except:
        pass
