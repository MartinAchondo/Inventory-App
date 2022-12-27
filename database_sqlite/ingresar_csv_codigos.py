import csv
import base as db
import crud as crd

def subir_tipo(file_name):
    path = 'database/codigos_csv/' + file_name
    with open(path,'r') as file:
        csv_reader = csv.reader(file,delimiter=';')
        line_1 = ''
        for line in csv_reader:
            codigo,valor = line
            dic = dict()
            dic['sigla'] = codigo
            dic['tipo'] = valor
            ans = preguntar_si_existe(dic,'tipos',db.create_connection)
            if len(ans)==0:
                ingresar_tipo(dic,db.create_connection)


def ingresar_tipo(dic,con):
    if len(crd.get_algunos(dic,'tipos',con))==0:
        sql = ''' 
            INSERT INTO tipos(
                sigla,
                tipo
            ) 
            VALUES(
                :sigla,
                :tipo
            ) 
            '''

        connection = con()
        try:
            cur = connection.cursor()
            cur.execute(sql,dic)
            connection.commit()
            return True
        except Exception as e:
            print(e)
            return False

def subir_color(file_name):
    path = 'database/codigos_csv/' + file_name
    with open(path,'r') as file:
        csv_reader = csv.reader(file,delimiter=';')
        line_1 = ''
        for line in csv_reader:
            codigo,valor = line
            dic = dict()
            dic['numero'] = codigo
            dic['color'] = valor
            
            ans = preguntar_si_existe(dic,'colores',db.create_connection)
            if len(ans)==0:
                ingresar_color(dic,db.create_connection)


def ingresar_color(dic,con):
    if len(crd.get_algunos(dic,'colores',con))==0:
        sql = ''' 
            INSERT INTO colores(
                numero,
                color
            ) 
            VALUES(
                :numero,
                :color
            ) 
            '''

        connection = con()
        try:
            cur = connection.cursor()
            cur.execute(sql,dic)
            connection.commit()
            return True
        except Exception as e:
            print(e)
            return False

def preguntar_si_existe(data,tabla,connectionn):
    ans = crd.get_algunos(data,tabla,connectionn)
    return ans

if __name__=='__main__':
    pass
    subir_tipo('tipos.csv')
    subir_color('colores.csv')