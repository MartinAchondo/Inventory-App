import os
import csv

try:
    import base as db
    import crud as crd
except:
    pass

def edit(connectionn):
    ans = crd.get_todos_dic('ventas',connectionn)
    for dic in ans: 
        id = dic['id']
        if id>66:
            print(id)
            dic['fecha'] = '2021/09/28'
            #dic['descuento'] = '0%'
            print(dic)
            ans2 = crd.actualizar(dic,{'id':id},'ventas',connectionn)

def edit_1(connectionn):
    ans = crd.get_todos_dic('ventas',connectionn)
    for dic in ans: 
        id = dic['id']
        if id==21:
            print(id)
            dic['fecha'] = '2021/07/28'
            dic['descuento'] = '0%'
            dic['precioventa'] = int(dic['precioventa']*0.9)
            print(dic)
            ans2 = crd.actualizar(dic,{'id':id},'ventas',connectionn)

def edit_2(connectionn):
    ans = crd.get_todos_dic('inventario',connectionn)
    ans_2 = crd.get_todos_dic('ventas',connectionn)
    for dic in ans_2:
        id = dic['id']
        if id>20:
            cod = dic['codigo']
            #print(cod)
            for dic_inv in ans:
                if cod == dic_inv['codigo']:
                    dic['precioreal'] = dic_inv['preciotienda']
                
                    descuento = 100-int(dic['precioventa']/0.9)*100//int(dic['precioreal'])
                    dic['descuento'] = str(descuento)+"%"
                    ans2 = crd.actualizar(dic,{'id':id},'ventas',connectionn)
                    



if __name__=='__main__':
    try:
        #edit_1(db.create_connection)
        #edit_2(db.create_connection)
        edit(db.create_connection)
    except Exception as e:
        print(e)
