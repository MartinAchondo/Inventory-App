import os
import json
import uuid
import ctypes
import shutil
import codecs
from datetime import date
import database_sqlite.crud as crd
import web.google_api as gapi
from database_sqlite.database import DB_Queries
import database_sqlite.database as db
from web.google_api import Fotos as Google_Fotos


def hideConsole():
    whnd = ctypes.windll.kernel32.GetConsoleWindow()
    if whnd != 0:
        ctypes.windll.user32.ShowWindow(whnd,0)

def verify_keys():
   filename = os.path.join(os.getcwd(), "keys.json")
   with open(filename,"r") as file_json:
      data = json.load(file_json)
      id_pc = str(str(uuid.getnode()).encode("utf-8").decode("utf-8"))
      keys = data["keys"]
      if id_pc in keys.values():
         return True
      elif "xxxx" in keys.values():
         for key in keys: 
           if keys[key]=="xxxx":
              keyx = key
              break
      else:
         return False
   os.remove(filename)
   with open(filename,"w") as file_json:
      data["keys"][keyx] = id_pc
      json.dump(data,file_json,indent=4)
      return True


def read_html(dir):
    file = codecs.open(dir, "r", "utf-8")
    html = file.read()
    file.close()
    return html


class Ingresar_Nueva(DB_Queries):

    def __init__(self):
        super().__init__()

    def ingresar_nuevo(self,data):
        data_filtro = {'tipo': data['tipo'],'color':data['color']}
        ans = self.get_algunos(data_filtro,'codigos')

        cod_tipo = self.get_algunos({'tipo': data['tipo']},'tipos')
        cod_color = self.get_algunos({'color': data['color']},'colores')
        if len(ans)==0:
            codd = str(cod_color[0][1])
            codigo = 'DOM-{}{}01'.format(cod_tipo[0][1],self.pasar_str(codd,2))
        else: 
            ans.sort()
            ans.reverse()
            anterior = int(ans[0][1][8:])
            actual = anterior + 1
            actual = str(actual)
            actual = self.pasar_str(actual,2)
            codd = str(cod_color[0][1])
            codigo = 'DOM-{}{}{}'.format(cod_tipo[0][1],self.pasar_str(codd,2),actual) 

        data_filtro['codigo'] = codigo
        data['codigo'] = codigo
        data_filtro['descripcion'] = data['descripcion']

        data2 = dict()
        data2['tipo'] = 'Ingresar Prenda'
        today = date.today()
        d1 = today.strftime("%Y/%m/%d")
        data2['fecha'] = d1
        data2['codigo'] = codigo
        data2['descripcion'] = 'Se ingresó {} del proovedor {}, cantidad: {}'.format(data['descripcion'],data['proovedor'],data['cantidad'])
        ans3 = self.crear_dato(data2,'historial')
        #borrar proovedor para inventario
        del data['proovedor']
        data['cantidadcasa'] = data['cantidad']
        data['cantidadtienda'] = 0
        
        ans = self.crear_dato(data_filtro,'codigos')
        ans2 = self.crear_dato(data,'inventario')
        #falta dato historial
        result = 'Se agregó prenda {}'.format(codigo)
        if ans and ans2:
            return result
        else:
            return False

    def pedir_tipo_color_nueva(self):
        L_colores = self.get_todos('colores')
        colores = list()
        for _,_,color in L_colores:
            colores.append(color)
        colores.sort()

        L_tipos = self.get_todos('tipos')
        tipos = list()
        for _,_,tipo in L_tipos:
            tipos.append(tipo)
        tipos.sort()
        return [colores,tipos]

    @staticmethod
    def pasar_str(data,n):
        while len(data)<n:
            data = '0' + data
        return data


class Ingresar_Existente(DB_Queries):

    def __init__(self):
        super().__init__()

    def get_cod_descr(self):
        L = self.get_todos('inventario')
        if len(L)==0:
            return L
        L_ans = list()

        for _,codigo,_,descripcion,_,_,_,_,_,_,_ in L:
            text = '{} - {}'.format(codigo,descripcion)
            L_ans.append(text)
        return L_ans

    def pedir_precio_costo(self,data):
        data_base = self.get_algunos(data,'inventario')
        if len(data_base)==0:
            return data_base

        L_ans = [data_base[0][5],data_base[0][6],data_base[0][8]]
        return L_ans

    def ingresar_existente(self,data):
        filtro = dict()
        filtro['codigo'] = data['codigo'].replace(" ","")
        ans2 = self.get_algunos(filtro,'inventario')
        
        cant_old = ans2[0][7]
        cost_old = ans2[0][5]
        cant_nueva = int(cant_old) + int(data['cantidad'])
        cost_nueva = (int(cost_old)*int(cant_old) + int(data['cantidad'])*int(data['costo']))//cant_nueva

        data['costo'] = cost_nueva
        cant_casa_old = ans2[0][9]
        cant_casa_nueva = int(cant_casa_old) + int(data['cantidad'])

        cant_ingresar = data['cantidad']
        data['cantidad'] = cant_nueva
        data['cantidadcasa'] = cant_casa_nueva
        data2 = dict()
        data2['tipo'] = 'Ingresar Prenda'
        today = date.today()
        d1 = today.strftime("%Y/%m/%d")
        data2['fecha'] = d1
        data2['codigo'] = data['codigo'].replace(" ","")
        data2['descripcion'] = 'Se ingresó {} del proovedor {}, cantidad: {}'.format(ans2[0][3],data['proovedor'],cant_ingresar)
        ans3 = self.crear_dato(data2,'historial')
        del data['proovedor']

        ans = self.actualizar(data,filtro,'inventario')
        return ans


class Editar(DB_Queries):

    def __init__(self):
        super().__init__()

    def pedir_todo(self,data):
        ans = self.get_algunos_dic(data,'inventario')
        if len(ans)==0:
            return []
        return ans[0]

    def editar(self,data):
        filtro = {'codigo': data['codigo']}
        del data['codigo']
        ans = self.actualizar(data,filtro,'inventario')

        today = date.today()
        d1 = today.strftime("%Y/%m/%d")
        data2 = dict()
        data2['tipo'] = 'Editar'
        data2['fecha'] = d1
        data2['codigo'] = filtro['codigo']
        data2['descripcion'] = 'Se editó prenda con:  cant_t: {}, cant_c: {}, p_t: {}, p_c: {},cost: {}, descr: {}'.format(data['cantidadtienda'],data['cantidadcasa'],data['preciotienda'],data['precio'],data['costo'],data['descripcion'])
        ans3 = self.crear_dato(data2,'historial')
        return ans

    def borrar(self,data):
        ans = self.borrar(data,'inventario')
        ans2 = self.borrar(data,'codigos')
        today = date.today()
        d1 = today.strftime("%Y/%m/%d")
        data2 = dict()
        data2['tipo'] = 'Borrar'
        data2['fecha'] = d1
        data2['codigo'] = data['codigo']
        data2['descripcion'] = 'Se eliminó código'
        ans3 = self.crear_dato(data2,'historial')
        return ans


class Ingresar_Venta(DB_Queries):

    def __init__(self):
        super().__init__()

    def ingresar_venta(self,data):
        today = date.today()
        d1 = today.strftime("%Y/%m/%d")
        filtro = {'codigo':data['codigo']}
        ans = self.get_algunos(filtro,'inventario')

        if data['lugar']=='Tienda':
            d1 = self.fecha_anterior(d1)
            precio_venta = int(int(data['precioventa'])*0.9)
            precio_real = ans[0][8]
            descuento = 100-int(data['precioventa'])*100//int(precio_real)
            data['descuento'] = str(descuento)+"%"
            data['precioreal'] = precio_real
            data['precioventa'] = precio_venta

        elif data['lugar'] == 'Casa':
            precio_real = ans[0][6]
            precio_venta = int(data['precioventa'])
            descuento = 100-precio_venta*100//int(precio_real)
            data['descuento'] = str(descuento)+"%"
            data['precioreal'] = precio_real

        data['fecha'] = d1
        ans3 = self.crear_dato(data,'ventas')

        data_inventario = dict()
        cantidad_old = ans[0][7]
        cantidad_new = int(cantidad_old)-int(data['cantidad'])
        data_inventario['cantidad'] = cantidad_new

        if data['lugar']=='Casa':
            cantidad_casa_old = ans[0][9]
            cantidad_casa_new = int(cantidad_casa_old)-int(data['cantidad'])
            data_inventario['cantidadcasa'] = cantidad_casa_new

        elif data['lugar']=='Tienda':
            cantidad_tienda_old = ans[0][10]
            cantidad_tienda_new = int(cantidad_tienda_old)-int(data['cantidad'])
            data_inventario['cantidadtienda'] = cantidad_tienda_new

        ans2 = self.actualizar(data_inventario,filtro,'inventario')
        data2 = dict()
        data2['tipo'] = 'Venta'
        data2['fecha'] = d1
        data2['codigo'] = data['codigo']
        data2['descripcion'] = 'Se ingresó venta de {} en {}, cantidad: {}'.format(ans[0][3],data['lugar'],data['cantidad'])
        ans3 = self.crear_dato(data2,'historial')
        return ans2

    def pedir_cantidades(self,data):
        dic = self.get_algunos_dic(data,'inventario')
        if len(dic)==0:
            return dic
        L = [dic[0]['cantidadcasa'],dic[0]['cantidadtienda']]
        return L 

    @staticmethod
    def fecha_anterior(d1):
        ano = d1[0:4]
        mes = d1[5:7]
        mes_1 = str(int(mes)-1)
        if len(mes_1)==1:
            mes_1 = '0'+ mes_1
            if mes_1=='00':
                mes_1 = '12'
                ano = str(int(ano)-1)
        d1 = '{}/{}/{}'.format(ano,mes_1,'28')
        return d1


class Ingresar_Devolucion(DB_Queries):

    def __init__(self):
        super().__init__()

    def ingresar_devolucion(self,data):
        today = date.today()
        d1 = today.strftime("%Y/%m/%d")
        data['fecha'] = d1
        filtro = {'codigo':data['codigo']}
        ans = self.get_algunos(filtro,'inventario')

        precio_real = ans[0][6]
        #descuento = 100-int(data['precioventa'])*100//int(precio_real)
        data['descuento'] = "Null"
        data['precioreal'] = (-1)*int(precio_real)

        data['precioventa'] = (-1)*int(data['precioventa'])
        if data['lugar']=='Tienda':
            data['precioventa'] = data['precioventa']*0.9

        ans3 = self.crear_dato(data,'ventas')

        data_inventario = dict()
        cantidad_old = ans[0][7]
        cantidad_new = int(cantidad_old)+int(data['cantidad'])
        data_inventario['cantidad'] = cantidad_new

        if data['lugar']=='Casa':
            cantidad_casa_old = ans[0][9]
            cantidad_casa_new = int(cantidad_casa_old)+int(data['cantidad'])
            data_inventario['cantidadcasa'] = cantidad_casa_new
            precio_real = ans[0][6]
            #descuento = 100-int(data['precioventa'])*100//int(precio_real)
            data['descuento'] = "Null"
            data['precioreal'] = precio_real

        elif data['lugar']=='Tienda':
            cantidad_tienda_old = ans[0][10]
            cantidad_tienda_new = int(cantidad_tienda_old)+int(data['cantidad'])
            data_inventario['cantidadtienda'] = cantidad_tienda_new
            precio_real = ans[0][8]
            #descuento = 100-int(data['precioventa'])*100//int(precio_real)
            data['descuento'] = "Null"
            data['precioreal'] = precio_real

        ans2 = self.actualizar(data_inventario,filtro,'inventario')

        data2 = dict()
        data2['tipo'] = 'Devolución'
        data2['fecha'] = d1
        data2['codigo'] = data['codigo']
        data2['descripcion'] = 'Se ingresó devolución de {} en {}, cantidad: {}'.format(ans[0][3],data['lugar'],data['cantidad'])
        ans3 = self.crear_dato(data2,'historial')
        return ans2

    def anular_venta(self,data):
        today = date.today()
        d1 = today.strftime("%Y/%m/%d")
        data['fecha'] = d1
        filtro = {'codigo':data['codigo']}
        ans = self.get_algunos(filtro,'inventario')

        filtro2 = {'id': data['id']}
        idd = data['id']
        ansx = self.get_algunos_dic(filtro2,'ventas')

        precio_real = ans[0][6]
        #descuento = 100-int(data['precioventa'])*100//int(precio_real)
        data['descuento'] = "Null"
        data['precioreal'] = (-1)*int(precio_real)
        data['precioventa'] = (-1)*int(ansx[0]['precioventa'])
        data['lugar'] = ansx[0]['lugar']
        data['cantidad'] = ansx[0]['cantidad']
        del data['id']
        ans3 = self.crear_dato(data,'ventas')

        data_inventario = dict()
        cantidad_old = ans[0][7]
        cantidad_new = int(cantidad_old)+int(data['cantidad'])
        data_inventario['cantidad'] = cantidad_new

        if data['lugar']=='Casa':
            cantidad_casa_old = ans[0][9]
            cantidad_casa_new = int(cantidad_casa_old)+int(data['cantidad'])
            data_inventario['cantidadcasa'] = cantidad_casa_new
            precio_real = ans[0][6]
            #descuento = 100-int(data['precioventa'])*100//int(precio_real)
            data['descuento'] = "Null"
            data['precioreal'] = precio_real

            ans2 = self.actualizar(data_inventario,filtro,'inventario')

        elif data['lugar']=='Tienda':
            cantidad_tienda_old = ans[0][10]
            cantidad_tienda_new = int(cantidad_tienda_old)+int(data['cantidad'])
            data_inventario['cantidadtienda'] = cantidad_tienda_new
            precio_real = ans[0][8]
            #descuento = 100-int(data['precioventa'])*100//int(precio_real)
            data['descuento'] = "Null"
            data['precioreal'] = precio_real

            ans2 = self.actualizar(data_inventario,filtro,'inventario')

        data2 = dict()
        data2['tipo'] = 'Anular Venta'
        data2['fecha'] = d1
        data2['codigo'] = data['codigo']
        data2['descripcion'] = 'Se anuló venta de {} con id: {}'.format(ans[0][3],idd)
        ans3 = self.crear_dato(data2,'historial')
        return ans2

class Inventario(DB_Queries):

    def __init__(self):
        super().__init__()

    def pedir_todo(self):
        ans = self.get_todos('inventario')
        return ans

    def crear_planilla(self):
        ans = self.get_todos('inventario')
        return ans

    def pedir_analisis(self):
        ans = self.query("SELECT tipo FROM codigos")
        ans2 = self.get_todos_dic('inventario')
        data = 'todo'
        set_tipos = set()
        for tipo in ans:
            tipo = tipo[0]
            set_tipos.add(tipo)
        
        L_tipos = list()
        L_cantidades = list()
        for tipo in set_tipos:
            L_tipos.append(tipo)
            L_cantidades.append(0)
            for dic in ans2:
                if dic['tipo'] == tipo:
                    if data == 'todo':
                        L_cantidades[len(L_tipos)-1] += dic['cantidad']    
                    elif data == 'casa':
                         L_cantidades[len(L_tipos)-1] += dic['cantidadcasa']
                    elif data == 'tienda':
                        L_cantidades[len(L_tipos)-1] += dic['cantidadtienda']  
        return [L_tipos,L_cantidades]


class Ventas(DB_Queries):

    def __init__(self):
        super().__init__()

    def pedir_todo(self):
        #ans = self.crd.get_todos('ventas')
        ans = self.get_n_tablas([[['id','codigo','fecha','cantidad','lugar','precioventa','precioreal','descuento'],'ventas'],[['descripcion','color'],'inventario']],'codigo',[])
        return ans

    def crear_planilla(self):
        ans = self.get_n_tablas_dic([[['id','codigo','fecha','cantidad','lugar','precioventa','precioreal','descuento'],'ventas'],[['descripcion','color'],'inventario']],'codigo',[])
        return ans


class Enviar_Tienda(DB_Queries):

    def __init__(self):
        super().__init__()

    def ingresar_tienda(self,data):
        for ingr in data:
            filtro = {'codigo':ingr['codigo']}
            nuevo = dict()

            ans2 = self.get_algunos(filtro,'inventario')
            cant_casa_old = ans2[0][9]
            cant_casa_nueva = int(cant_casa_old) - int(ingr['cantidad'])
            cant_tienda_old = ans2[0][10]
            cant_tienda_nueva = int(cant_tienda_old) + int(ingr['cantidad'])
            cantidad = ingr['cantidad']

            precio = int(ingr['precio'].replace('$',"").replace(',',''))
            nuevo['cantidadcasa'] = cant_casa_nueva
            nuevo['cantidadtienda'] = cant_tienda_nueva
            nuevo['preciotienda'] = precio

            ans = self.actualizar(nuevo,filtro,'inventario')

            today = date.today()
            d1 = today.strftime("%Y/%m/%d")
            data2 = dict()
            data2['tipo'] = 'Enviar a Tienda'
            data2['fecha'] = d1
            data2['codigo'] = ingr['codigo']
            data2['descripcion'] = 'Se envió a tienda {}, cantidad: {}'.format(ans2[0][3],cantidad)
            ans3 = self.crear_dato(data2,'historial')
        return ans

    def pedir_codigos(self):

        L = self.get_todos('inventario')
        if len(L)==0:
            return L
        L_ans = list()

        for _,codigo,_,descripcion,_,_,_,_,_,cant,_ in L:
            if int(cant)>0:
                text = '{} - {}'.format(codigo,descripcion)
                L_ans.append(text)
        return L_ans

    def pedir_cantidad_max(self,data):
        dic = self.get_algunos_dic(data,'inventario')
        if len(dic)==0:
            return dic
        return dic[0]['cantidadcasa']


class Enviar_Casa(DB_Queries):

    def __init__(self):
        super().__init__()

    def ingresar_casa(self,data):
        
        for ingr in data:
            filtro = {'codigo':ingr['codigo']}

            ans2 = self.get_algunos(filtro,'inventario')
    
            cant_casa_old = ans2[0][9]
            cant_casa_nueva = int(cant_casa_old) + int(ingr['cantidad'])

            cant_tienda_old = ans2[0][10]
            cant_tienda_nueva = int(cant_tienda_old) - int(ingr['cantidad'])

            cantidad = ingr['cantidad']

            nuevo = dict()
            nuevo['cantidadcasa'] = cant_casa_nueva
            nuevo['cantidadtienda'] = cant_tienda_nueva

            ans = self.actualizar(nuevo,filtro,'inventario')

            today = date.today()
            d1 = today.strftime("%Y/%m/%d")
            data2 = dict()
            data2['tipo'] = 'Enviar a Casa'
            data2['fecha'] = d1
            data2['codigo'] = ingr['codigo']
            data2['descripcion'] = 'Se envió a casa {}, cantidad: {}'.format(ans2[0][3],cantidad)
            ans3 = self.crear_dato(data2,'historial')
        return ans

    def pedir_codigos(self):

        L = self.get_todos('inventario')
        if len(L)==0:
            return L
            
        L_ans = list()

        for _,codigo,_,descripcion,_,_,_,_,_,_,cant in L:
            if int(cant)>0:
                text = '{} - {}'.format(codigo,descripcion)
                L_ans.append(text)
        return L_ans

    def pedir_cantidad_max_casa(self,data):
        dic = self.get_algunos_dic(data,'inventario')
        return dic[0]['cantidadtienda']



class Historial(DB_Queries):

    def __init__(self):
        super().__init__()

    def pedir_todo(self):
        ans = self.get_todos('historial')
        return ans

    def crear_planilla(self):
        ans = self.get_todos('historial')
        return ans


class Base(DB_Queries):

    def __init__(self):
        super().__init__()

    @staticmethod
    def copy_path(data):
        newpath = os.getcwd()
        newpath = os.path.join(newpath,'base','base.db')
        if data == None:
            return True
        ext = data[-3:]
        if ext == '.db':
            try:
                shutil.copy(data,newpath)
                return True
            except Exception as e:
                print(e)
                return False

    @staticmethod
    def copy_path_foto(data):
        path = data[0]
        codigo = data[1] + ".jpg"
        newpath = os.getcwd()
        newpath = os.path.join(newpath,'src','img-codigos',codigo)
        if path == None:
            return True
        ext = path[-4:]
        if ext == '.jpg' or ext == 'jpeg' or ext == '.png':
            try:
                shutil.move(path,newpath)
                return True
            except Exception as e:
                print(e)
                return False

    def get_cod_descr(self):
        L = self.get_todos('inventario')
        if len(L)==0:
            return L
        L_ans = list()

        for _,codigo,_,descripcion,_,_,_,_,_,_,_ in L:
            path_foto = os.path.join(os.getcwd(),'src','img-codigos',codigo+'.jpg')
            if not os.path.isfile(path_foto):
                text = '{} - {}'.format(codigo,descripcion)
                L_ans.append(text)
        return L_ans

    @staticmethod
    def upload_base(service):
        try:
            base = gapi.Base()
            base.update_file(service)
            return True
        except Exception as e:
            print(e)
            return False

    @staticmethod
    def download_base(service):
        root = os.getcwd()
        newpath = os.path.join(root,'saves','base_save.db')
        oldpath = os.path.join(root,'base','base.db')
        shutil.copy(oldpath,newpath)
        try:
            base = gapi.Base()
            base.download_file(service)
            return True
        except Exception as e:
            print(e)
            return False

    @staticmethod
    def upload_sheet(name,service):
        try:
            sh = gapi.Sheets()
            sh.update_file(name,service)
            return True
        except Exception as e:
            print(e)
            return False



class Inicio(DB_Queries):

    def __init__(self):
        super().__init__()
        self.crd2 = db.DB2_Queries()

    def get_meses(self):
        ans = self.get_todos('ventas')
        if len(ans)==0:
            return ans
            
        dic_meses = dict()
        L_montos = list()
        L_labels = list()

        for _,_,fecha,cantidad,_,precio,_,_ in ans:
            fecha = fecha[0:7]
            fecha = fecha[5:] +'/'+ fecha[0:4]
            if fecha not in dic_meses:
                dic_meses[fecha] = precio*cantidad
                L_labels.append(fecha)
            else:
                dic_meses[fecha] += precio*cantidad
 
        for fecha in L_labels:
            L_montos.append(dic_meses[fecha])    
    
        return [L_montos,L_labels]

    def get_circular(self):
        ans = self.get_todos('ventas')
        if len(ans)==0:
            return ans

        L_total_casa = 0
        L_total_tienda = 0
        L_mes_casa = 0
        L_mes_tienda = 0
        today = date.today()
        d1 = today.strftime("%Y/%m/%d")
        hoy = d1[0:8]
        
        for _,_,fecha,cantidad,lugar,precio,_,_ in ans:
            fecha = fecha[0:8]
            if lugar=='Casa':
                L_total_casa += precio*cantidad
                if hoy == fecha:
                    L_mes_casa += precio*cantidad
            elif lugar=='Tienda':
                L_total_tienda += precio*cantidad
                if hoy == fecha:
                    L_mes_tienda += precio*cantidad
            
        L = [[L_total_casa,L_total_tienda],[L_mes_casa,L_mes_tienda]]
        return L
            
    def get_cantidades(self):
        ans = self.get_todos_dic('inventario')
        if len(ans)==0:
            return ans
            
        total_casa = 0
        total_tienda = 0
        for dic in ans: 
            total_casa += dic['cantidadcasa']
            total_tienda += dic['cantidadtienda']
        return [total_casa,total_tienda]

    def get_utilidad_costos(self):
        ans = self.get_todos('ventas')
        if len(ans)==0:
            return ans
        ut_total = 0
        ut_mes = 0
        cst_total = 0
        ut_inv = 0
        today = date.today()
        d1 = today.strftime("%Y/%m/%d")
        hoy = d1[0:8]
        
        for _,codigo,fecha,cantidad,lugar,precio,_,_ in ans:
            fecha = fecha[0:8]
            data = self.get_algunos_dic({'codigo':codigo},'inventario')
            cst = data[0]['costo']*cantidad
            ut = precio*cantidad - cst
            if hoy == fecha:
                ut_mes += ut
            ut_total += ut

        data = self.get_todos_dic('inventario')
        for valor in data:
            cst_total += valor['costo']*valor['cantidad']
            ut_inv += valor['precio']*valor['cantidad']-valor['costo']*valor['cantidad']
        L = [ut_total,cst_total,ut_mes,ut_inv]
        return L      

    def comparar_bases(self,service):
        try:
            base = gapi.Base()
            base.download_file_compare(service)
            local = self.query('SELECT COUNT(*) from historial')
            online = self.crd2.query('SELECT COUNT(*) from historial')
            local = local[0][0]
            online = online[0][0]
            if local == online:
                return 'igual'
            if local < online:
                return 'menor'
            if local > online:
                return 'mayor'
        except Exception as e:
            print(e)
            return False


class Analisis(DB_Queries):

    def __init__(self):
        super().__init__()

    def pedir_tipos_total(self,data):
        ans = self.query("SELECT tipo FROM codigos")
        ans2 = self.get_todos_dic('inventario')

        set_tipos = set()
        for tipo in ans:
            tipo = tipo[0]
            set_tipos.add(tipo)
        
        L_tipos = list()
        L_cantidades = list()
        for tipo in set_tipos:
            L_tipos.append(tipo)
            L_cantidades.append(0)
            for dic in ans2:
                if dic['tipo'] == tipo:
                    if data == 'todo':
                        L_cantidades[len(L_tipos)-1] += dic['cantidad']    
                    elif data == 'casa':
                         L_cantidades[len(L_tipos)-1] += dic['cantidadcasa']
                    elif data == 'tienda':
                        L_cantidades[len(L_tipos)-1] += dic['cantidadtienda']  
        return [L_tipos,L_cantidades]

    def pedir_tipos_ventas(self,data):
        fecha = data
        sql = """
            SELECT codigos.tipo, ventas.cantidad, ventas.precioventa, inventario.costo, ventas.lugar
            FROM ventas
            INNER JOIN codigos
            ON ventas.codigo = codigos.codigo
            INNER JOIN inventario
            ON ventas.codigo = inventario.codigo
            WHERE ventas.fecha LIKE '{}%'
                """.format(fecha)
        ans = self.query(sql)
        
        dic_tipos = dict()
        L_tipos = list()
        L_tipos_c = list()

        vent_casa = 0
        vent_tienda = 0
        cst_total = 0
        if not ans or len(ans)==0:
            return []
        for tipo,cantidad,precio,costo,lugar in ans:
            if tipo not in dic_tipos:
                dic_tipos[tipo] = cantidad
            else:
                dic_tipos[tipo] += cantidad

            if lugar=='Casa':
                vent_casa += precio*cantidad
            elif lugar=='Tienda':
                vent_tienda += precio*cantidad

            cst_total += costo*cantidad

        L_circ_vent = [['Casa','Tienda'],[vent_casa,vent_tienda]]
        for tipos in dic_tipos:
            L_tipos.append(tipos)
            L_tipos_c.append(dic_tipos[tipos])
        
        return [[L_tipos,L_tipos_c],L_circ_vent,cst_total]
    
    def pedir_codigo_analisis(self,data):

        ans = self.get_algunos_dic(data,'inventario')
        return ans[0]

    def pedir_ventas_codigo_analisis(self,data):

        ans = self.get_algunos_dic(data,'ventas')
        return ans

    def pedir_query_analisis(self,data):
        if "SELECT" not in data:
            return [False,False]
        columns = self.query_columnas(data)
        body = self.query(data)
        return [columns,body]

class Pdf(DB_Queries):

    def __init__(self):
        super().__init__()
        
    def pedir_to_pdf(self,data):
        fecha = data

        sql = """
            SELECT ventas.id, codigos.codigo, codigos.tipo, codigos.descripcion, codigos.color, ventas.fecha, ventas.cantidad, ventas.precioventa, inventario.costo, ventas.lugar, ventas.descuento,ventas.precioreal
            FROM ventas
            INNER JOIN codigos
            ON ventas.codigo = codigos.codigo
            INNER JOIN inventario
            ON ventas.codigo = inventario.codigo
            WHERE ventas.fecha LIKE '{}%'
                """.format(fecha)
        ans = self.query_dic(sql)
        
        dic_tipos = dict()
        L_tipos = list()
        L_tipos_c = list()

        vent_casa = 0
        vent_tienda = 0
        cst_total = 0
        if not ans or len(ans)==0:
            return []
        for dic in ans:
            tipo = dic['tipo']
            cantidad = dic['cantidad']
            precio = dic['precioventa']
            costo = dic['costo']
            lugar = dic['lugar']
            if tipo not in dic_tipos:
                dic_tipos[tipo] = cantidad
            else:
                dic_tipos[tipo] += cantidad

            if lugar=='Casa':
                vent_casa += precio*cantidad
            elif lugar=='Tienda':
                vent_tienda += precio*cantidad

            cst_total += costo*cantidad

        ut_total = vent_casa + vent_tienda - cst_total
        L_circ_vent = [['Casa','Tienda'],[vent_casa,vent_tienda]]
        for tipos in dic_tipos:
            L_tipos.append(tipos)
            L_tipos_c.append(dic_tipos[tipos])
        
        return [ans,[L_tipos,L_tipos_c],L_circ_vent,ut_total,fecha]

class Fotos_Drive(Google_Fotos,DB_Queries):
    
    def __init__(self):
        super().__init__()

    def upload_if_not_exists(self,Create_Service):
        ans = self.get_bycol(['codigo'],{},'id_fotos')
        files = os.listdir(os.path.join(os.getcwd(),'src','img-codigos'))
        files = list(map(lambda x: x.replace('.jpg',''),files))
        subir = list()
        for codigo in files:
            if (codigo,) not in ans:
                subir.append(codigo)
        for cod in subir:
            codd,id_cod = self.create_file(cod,Create_Service)
            if id_cod != '':
                ans = self.crear_dato({'id_foto':id_cod,'codigo':cod},'id_fotos')
        
    def download_if_not_exists(self,Create_Service):
        ans = self.get_bycol(['codigo','id_foto'],{},'id_fotos')
        files = os.listdir(os.path.join(os.getcwd(),'src','img-codigos'))
        files = list(map(lambda x: x.replace('.jpg',''),files))
        descargar = list()
        for codigo,id_f in ans:
            if codigo not in files:
                descargar.append((codigo,id_f))
        for cod,id_foto in descargar:
            print(cod)
            self.download_foto(cod,id_foto,Create_Service)
