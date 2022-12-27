import os
import sqlite3
from functools import wraps


class DB_Queries():

    path_base = os.path.join(os.getcwd(),'base','base.db')
    connection = None
    status = False

    def __init__(self):
        if DB_Queries.connection is None:
            try:
                DB_Queries.connection = sqlite3.connect(self.path_base)
                DB_Queries.status = True
            except Exception as e:
                DB_Queries.status = False 
                print(e)
    
    def create_connection(query_function):
        @wraps(query_function)
        def wrapper(self,*kargs,**kwargs):
            if DB_Queries.status:
                ans = query_function(self,*kargs,**kwargs)
                DB_Queries.connection.close()
                DB_Queries.status = False
                return ans
            else:
                try:
                    DB_Queries.connection = sqlite3.connect(self.path_base)
                    DB_Queries.status = True
                    ans = query_function(self,*kargs,**kwargs)
                    DB_Queries.connection.close()
                    DB_Queries.status = False
                    return ans
                except Exception as e:
                    print(e)
                    return False
        return wrapper

    def make_dic(query_function):
        @wraps(query_function)
        def wrapper(self,*kargs,**kwargs):
            try:
                DB_Queries.connection = sqlite3.connect(self.path_base)
                DB_Queries.connection.row_factory = sqlite3.Row
                DB_Queries.status = True
                ans = query_function(self,*kargs,**kwargs)
                ans2 = [{k:item[k] for k in item.keys()} for item in ans]
                return ans2
            except Exception as e:
                print(e)
                return False
        return wrapper

    @create_connection
    def query(self,sql):
        try:
            cur = self.connection.cursor()
            cur.execute(sql)
            datos = cur.fetchall()
            self.connection.commit()
            return datos
        except Exception as e:
            print(e)
            return False

    @make_dic
    @create_connection
    def query_dic(self,sql):
        try:
            cur = self.connection.cursor()
            cur.execute(sql)
            datos = cur.fetchall()
            self.connection.commit()
            return datos
        except Exception as e:
            print(e)
            return False

    @create_connection
    def query_name(self,query_name):
        root = os.path.dirname(os.path.realpath(__file__))
        filename = os.path.join(root,'sql','querys.sql')
        with open(filename,'r') as fd:
            sqlfile = fd.read()
        sqlquerys = sqlfile.split('--')
        sqlquerys.pop(0)
        names = sqlquerys[::2]
        querys = sqlquerys[1::2]
        if query_name in names:
            index = names.index(query_name)
        else:
            return []
        try:
            cur = self.connection.cursor()
            cur.execute(querys[index])
            datos = cur.fetchall()
            self.connection.commit()
            return datos
        except Exception as e:
            print(e)
            return []
        
    @make_dic
    @create_connection
    def query_name_dic(self,query_name):
        root = os.path.dirname(os.path.realpath(__file__))
        filename = os.path.join(root,'sql','querys.sql')
        with open(filename,'r') as fd:
            sqlfile = fd.read()
        sqlquerys = sqlfile.split('--')
        sqlquerys.pop(0)
        names = sqlquerys[::2]
        querys = sqlquerys[1::2]
        if query_name in names:
            index = names.index(query_name)
        else:
            return []
        try:
            cur = self.connection.cursor()
            cur.execute(querys[index])
            datos = cur.fetchall()
            self.connection.commit()
            return datos
        except Exception as e:
            print(e)
            return []

    @create_connection
    def query_columnas(self,sql):
        DB_Queries.connection.row_factory = sqlite3.Row
        try:
            cur = self.connection.cursor()
            cur.execute(sql)
            datos = cur.fetchone()
            self.connection.commit()
            ans = datos.keys()
            return ans
        except Exception as e:
            print(e)
            return False 

    @create_connection
    def contar(self,tabla):
        sql = '''SELECT COUNT(*) FROM {}'''.format(tabla)
        try:
            cur = self.connection.cursor()
            cur.execute(sql)
            datos = cur.fetchone()
            self.connection.commit()
            return datos[0]
        except Exception as e:
            print(e)
            return False

    @create_connection
    def crear_dato(self,data,tabla):
        root = os.path.dirname(os.path.realpath(__file__))
        path_sql = os.path.join(root, 'tables_insert.sql')
        with open(path_sql,'r') as fd:
            sqlFile = fd.read()
        sqlcommands = sqlFile.split(';')
        sql = ''''''
        tabla = 'INSERT INTO ' + tabla
        for query in sqlcommands:
            if tabla in query:
                sql += query
                break 
        try:
            cur = self.connection.cursor()
            cur.execute(sql,data)
            self.connection.commit()
            return True
        except Exception as e:
            print(e)
            return False

    #Se actualiza por filtro (id o coidog o lo que sea)
    @create_connection
    def actualizar(self,data_nueva,data_filtro,tabla):
        sql = ''' 
            UPDATE {}
            '''.format(tabla)
        sql_where, data_filtro = self.WHERE(data_filtro)
        sql_set, data_nueva = self.SET(data_nueva)
        sql = sql + sql_set + sql_where
        data = dict()
        data.update(data_nueva)
        data.update(data_filtro)
        try:
            cur = self.connection.cursor()
            cur.execute(sql,data)
            self.connection.commit()
            return True
        except Exception as e:
            print(e)
            return False

    @create_connection
    def get_todos(self,tabla):
        sql = '''
            SELECT * FROM {}
            '''.format(tabla)
        try:
            cur = self.connection.cursor()
            cur.execute(sql)
            datos = cur.fetchall()
            self.connection.commit()
            return datos
        except Exception as e:
            print(e)
            return []   

    @make_dic
    @create_connection
    def get_todos_dic(self,tabla):
        sql = '''
            SELECT * FROM {}
            '''.format(tabla)
        try:
            cur = self.connection.cursor()
            cur.execute(sql)
            datos = cur.fetchall()
            self.connection.commit()
            return datos
        except Exception as e:
            print(e)
            return []  

    @create_connection
    def get_algunos(self,data_filtro,tabla):
        sql = '''
            SELECT * FROM {}
            '''.format(tabla)
        sql_where, data_filtro = self.WHERE(data_filtro)
        sql = sql + sql_where
        try:
            cur = self.connection.cursor()
            cur.execute(sql,data_filtro)
            datos = cur.fetchall()
            self.connection.commit()
            return datos
        except Exception as e:
            print(e)
            return []    

    @make_dic
    @create_connection
    def get_algunos_dic(self,data_filtro,tabla):
        sql = '''
            SELECT * FROM {}
            '''.format(tabla)
        sql_where, data_filtro = self.WHERE(data_filtro)
        sql = sql + sql_where
        try:
            cur = self.connection.cursor()
            cur.execute(sql,data_filtro)
            datos = cur.fetchall()
            self.connection.commit()
            return datos

        except Exception as e:
            print(e)
            return []    

    @create_connection
    def get_bycol(self,cols,data_filtro,tabla):
        sql = '''
            SELECT {} FROM {}
            '''.format(','.join(cols),tabla)
        sql_where, data_filtro = self.WHERE(data_filtro)
        sql = sql + sql_where
        try:
            cur = self.connection.cursor()
            cur.execute(sql,data_filtro)
            datos = cur.fetchall()
            self.connection.commit()
            return datos
        except Exception as e:
            print(e)
            return []    

    @make_dic
    @create_connection
    def get_bycol_dic(self,cols,data_filtro,tabla):
        sql = '''
            SELECT {} FROM {}
            '''.format(','.join(cols),tabla)
        sql_where, data_filtro = self.WHERE(data_filtro)
        sql = sql + sql_where
        try:
            cur = self.connection.cursor()
            cur.execute(sql,data_filtro)
            datos = cur.fetchall()
            self.connection.commit()
            return datos
        except Exception as e:
            print(e)
            return [] 


    #[[['fecha','lugar'],'ventas'],[['tipo','costo'],'inventario'],[['tipo'],'codigos']],'codigo',{'cantidad':1},db.create_connection
    @create_connection
    def get_n_tablas(self,data,union,filtro):
        sql,data_filtro = self.JOIN(data,union,filtro)
        try:
            cur = self.connection.cursor()
            cur.execute(sql,data_filtro)
            datos = cur.fetchall()
            self.connection.commit()
            return datos
        except Exception as e:
            print(e)
            return [] 

    @make_dic
    @create_connection
    def get_n_tablas_dic(self,data,union,filtro):
        sql,data_filtro = self.JOIN(data,union,filtro)
        try:
            cur = self.connection.cursor()
            cur.execute(sql,data_filtro)
            datos = cur.fetchall()
            self.connection.commit()
            return datos
        except Exception as e:
            print(e)
            return [] 

    @create_connection
    def borrar(self,data_filtro,tabla):
        sql = '''
            DELETE FROM {}
            '''.format(tabla)
        sql_where, data_filtro = self.WHERE(data_filtro)
        sql = sql + sql_where
        try:
            cur = self.connection.cursor()
            cur.execute(sql,data_filtro)
            self.connection.commit()
            return True
        except Exception as e:
            print(e)
            return False    

    @classmethod
    def JOIN(cls,data,union,filtro):
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
        sql_where,data_filtro = cls.WHERE(dic_filtro) 
        sql += ' ' + sql_where
        return (sql,data_filtro)

    @staticmethod
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

    @staticmethod
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

class DB2_Queries():

    def __init__(self):
        root = os.getcwd()
        self.path_base = os.path.join(root,'base','base_compare.db')
        try:
            self.con = sqlite3.connect(self.path_base)
        except Exception as e: 
            print(e)
    
    def create_connection(query_function):
        def connection(self,*kargs,**kwargs):
            try:
                ans = query_function(self,*kargs,**kwargs)
                self.con.close()
                return ans
            except:
                try:
                    self.con = sqlite3.connect(self.path_base)
                    ans = query_function(self,*kargs,**kwargs)
                    self.con.close()
                    return ans
                except Exception as e:
                    print(e)
        return connection

    @create_connection
    def query(self,sql):
        try:
            cur = self.con.cursor()
            cur.execute(sql)
            datos = cur.fetchall()
            self.con.commit()
            return datos
        except Exception as e:
            print(e)
            return False


if __name__=='__main__':
    db = DB_Queries()
    #db.connection.close()
    #print(DB_Queries.connection.cursor())
    db.crear_dato({'id_foto':'dwcw333','codigo':'BL-3434'},'id_fotos')
    #db.get_all_dic()
    #db.con.close()