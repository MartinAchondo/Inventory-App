import os
import sqlite3

def query(sql,connectionn):
    connection = connectionn()
    try:
        cur = connection.cursor()
        cur.execute(sql)
        datos = cur.fetchall()
        connection.commit()
        return datos
    except Exception as e:
        print(e)
        return False

def query_dic(sql,connectionn):
    connection = connectionn()
    connection.row_factory = sqlite3.Row
    try:
        cur = connection.cursor()
        cur.execute(sql)
        datos = cur.fetchall()
        connection.commit()
        ans = [{k:item[k] for k in item.keys()} for item in datos]
        return ans
    except Exception as e:
        print(e)
        return False

def query_columnas(sql,connectionn):
    connection = connectionn()
    connection.row_factory = sqlite3.Row
    try:
        cur = connection.cursor()
        cur.execute(sql)
        datos = cur.fetchone()
        connection.commit()
        ans = datos.keys()
        return ans
    except Exception as e:
        print(e)
        return False 

def contar(tabla,connectionn):
    connection = connectionn()
    sql = '''SELECT COUNT(*) FROM {}'''.format(tabla)
    try:
        cur = connection.cursor()
        cur.execute(sql)
        datos = cur.fetchone()
        connection.commit()
        return datos[0]
    except Exception as e:
        print(e)
        return False

def crear_dato(data,tabla,connectionn):
    connection = connectionn()
    root = os.path.dirname(os.path.realpath(__file__))
    path_sql = os.path.join(root, 'tables_insert.sql')
    fd = open(path_sql,'r')
    sqlFile = fd.read()
    fd.close()
    sqlcommands = sqlFile.split(';')
    sql = ''''''
    for query in sqlcommands:
        if tabla in query:
            sql += query
            break 
    try:
        cur = connection.cursor()
        cur.execute(sql,data)
        connection.commit()
        return True
    except Exception as e:
        print(e)
        return False

#Se actualiza por filtro (id o coidog o lo que sea)
def actualizar(data_nueva,data_filtro,tabla,connectionn):
    connection = connectionn()
    sql = ''' 
        UPDATE {}
        '''.format(tabla)
    sql_where, data_filtro = WHERE(data_filtro)
    sql_set, data_nueva = SET(data_nueva)
    sql = sql + sql_set + sql_where

    data = dict()
    data.update(data_nueva)
    data.update(data_filtro)
    try:
        cur = connection.cursor()
        cur.execute(sql,data)
        connection.commit()
        return True
    except Exception as e:
        print(e)
        return False

def get_todos(tabla,connection):
    connection = connection()
    sql = '''
        SELECT * FROM {}
        '''.format(tabla)
    try:
        cur = connection.cursor()
        cur.execute(sql)
        datos = cur.fetchall()
        connection.commit()
        return datos
    except Exception as e:
        print(e)
        return []   

def get_todos_dic(tabla,connection):
    connection = connection()
    connection.row_factory = sqlite3.Row
    sql = '''
        SELECT * FROM {}
        '''.format(tabla)
    try:
        cur = connection.cursor()
        cur.execute(sql)
        datos = cur.fetchall()
        connection.commit()
        ans = [{k:item[k] for k in item.keys()} for item in datos]
        return ans
    except Exception as e:
        print(e)
        return []  

def get_algunos(data_filtro,tabla,connection):
    connection = connection()
    sql = '''
        SELECT * FROM {}
        '''.format(tabla)
    sql_where, data_filtro = WHERE(data_filtro)
    sql = sql + sql_where
    try:
        cur = connection.cursor()
        cur.execute(sql,data_filtro)
        datos = cur.fetchall()
        connection.commit()
        return datos
    except Exception as e:
        print(e)
        return []    

def get_algunos_dic(data_filtro,tabla,connection):
    connection = connection()
    connection.row_factory = sqlite3.Row
    sql = '''
        SELECT * FROM {}
        '''.format(tabla)
    sql_where, data_filtro = WHERE(data_filtro)
    sql = sql + sql_where
    try:
        cur = connection.cursor()
        cur.execute(sql,data_filtro)
        datos = cur.fetchall()
        connection.commit()
        ans = [{k:item[k] for k in item.keys()} for item in datos]
        return ans
    except Exception as e:
        print(e)
        return []    

#[[['fecha','lugar'],'ventas'],[['tipo','costo'],'inventario'],[['tipo'],'codigos']],'codigo',{'cantidad':1},db.create_connection
def get_n_tablas(data,union,filtro,connectionn):
    connection = connectionn()
    sql,data_filtro = JOIN(data,union,filtro)
    try:
        cur = connection.cursor()
        cur.execute(sql,data_filtro)
        datos = cur.fetchall()
        connection.commit()
        return datos
    except Exception as e:
        print(e)
        return [] 

def get_n_tablas_dic(data,union,filtro,connectionn):
    connection = connectionn()
    connection.row_factory = sqlite3.Row
    sql,data_filtro = JOIN(data,union,filtro)
    try:
        cur = connection.cursor()
        cur.execute(sql,data_filtro)
        datos = cur.fetchall()
        connection.commit()
        ans = [{k:item[k] for k in item.keys()} for item in datos]
        return ans
    except Exception as e:
        print(e)
        return [] 

def borrar(data_filtro,tabla,connection):
    connection = connection()
    sql = '''
        DELETE FROM {}
        '''.format(tabla)
    sql_where, data_filtro = WHERE(data_filtro)
    sql = sql + sql_where
    try:
        cur = connection.cursor()
        cur.execute(sql,data_filtro)
        connection.commit()
        return True
    except Exception as e:
        print(e)
        return False    

def JOIN(data,union,filtro):
    #data1,tabla1 = data.pop(0)
    L_get = list()
    L_tablas = list()
    for datax,tablax in data:
        L_tablas.append(tablax)
        tablax = [tablax]
        tablax *= len(datax)
        add_t = lambda s1,s2: s1 + "." + s2
        data_n = list(map(add_t,tablax,datax))
        L_get.append(data_n)

    tabla1 = L_tablas.pop(0)
    sql = '''SELECT '''
    sql_gets = ''''''
    for tipos in L_get:
        for data_y in tipos:
            sql_gets = sql_gets + data_y +','
    sql_gets = sql_gets[:-1]
    sql_from = ''' FROM {}'''.format(tabla1)
    sql = sql + sql_gets + sql_from
    
    sql_join = '''''' 
    for tablas in L_tablas:
        sql_join += ''' INNER JOIN {}'''.format(tablas)
        x1 = tabla1 + '.' + union
        x2 = tablas + '.' + union 
        sql_join += ''' ON {}={}'''.format(x1,x2)
    sql += sql_join
    dic_filtro = dict()
    for filtrox in filtro:
        filtro_n =  tabla1 + '.' + filtrox
        dic_filtro[filtro_n] = filtro[filtrox]
    sql_where,data_filtro = WHERE(dic_filtro) 
    sql += ' ' + sql_where
    return (sql,data_filtro)

def WHERE(data_filtro):
    iter = True
    data = dict()
    sql = ''''''
    for llaves in data_filtro.keys():
        if iter:
            sql = sql + '''WHERE {} = :{}f '''.format(llaves,llaves.replace('.',''))
            llaves_nueva = llaves.replace('.','') + 'f'
            data[llaves_nueva] = data_filtro[llaves]
            iter = False
        else:
            sql = sql + '''AND {} = :{}f '''.format(llaves,llaves.replace('.',''))
            llaves_nueva = llaves.replace('.','') + 'f'
            data[llaves_nueva] = data_filtro[llaves]
    return sql,data

def SET(data_nueva):
    iter = True
    data = dict()
    sql = ''''''
    for llaves in data_nueva.keys():
        if iter:
            sql = sql + '''SET {} = :{}n '''.format(llaves, llaves)
            llaves_nueva = llaves + 'n'
            data[llaves_nueva] = data_nueva[llaves]
            iter = False
        else:
            sql = sql + ''', {} = :{}n '''.format(llaves,llaves)
            llaves_nueva = llaves + 'n'
            data[llaves_nueva] = data_nueva[llaves]
    return sql, data 


def crear_dato_codigos(data,connectionn):
    connection = connectionn()
    #data es un dic
    sql = ''' 
        INSERT INTO codigos(
            codigo,
            tipo,
            descripcion,
            color
        ) 
        VALUES(
            :codigo,
            :tipo,
            :descripcion,
            :color
            ) 
        '''
    try:
        cur = connection.cursor()
        cur.execute(sql,data)
        connection.commit()
        return True
    except Exception as e:
        print(e)
        return False

def crear_dato_inventario(data,connectionn):
    connection = connectionn()
    #data es un dic
    sql = ''' 
        INSERT INTO inventario(
            codigo,
            tipo,
            descripcion,
            color,
            costo,
            precio,
            cantidad,
            preciotienda,
            cantidadcasa,
            cantidadtienda
        ) 
        VALUES(
            :codigo,
            :tipo,
            :descripcion,
            :color,
            :costo,
            :precio,
            :cantidad,
            :preciotienda,
            :cantidadcasa,
            :cantidadtienda
            ) 
        '''
    try:
        cur = connection.cursor()
        cur.execute(sql,data)
        connection.commit()
        return True
    except Exception as e:
        print(e)
        return False

def crear_dato_ventas(data,connectionn):
    connection = connectionn()
    #data es un dic
    sql = ''' 
        INSERT INTO ventas(
            codigo,
            fecha,
            cantidad,
            lugar,
            precioventa,
            precioreal,
            descuento
        ) 
        VALUES(
            :codigo,
            :fecha,
            :cantidad,
            :lugar,
            :precioventa,
            :precioreal,
            :descuento
            ) 
        '''
    try:
        cur = connection.cursor()
        cur.execute(sql,data)
        connection.commit()
        return True
    except Exception as e:
        print(e)
        return False



def crear_dato_historial(data,connectionn):
    connection = connectionn()
    #data es un dic
    sql = ''' 
        INSERT INTO historial(
            codigo,
            tipo,
            fecha,
            descripcion
        ) 
        VALUES(
            :codigo,
            :tipo,
            :fecha,
            :descripcion
            ) 
        '''
    try:
        cur = connection.cursor()
        cur.execute(sql,data)
        connection.commit()
        return True
    except Exception as e:
        print(e)
        return False


