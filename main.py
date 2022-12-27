import eel 
import functions as fn
import pdfs.plots as pdf
import sheets.excel as xls
import database_sqlite.base as db
import web.google_service as gle


@eel.expose 
def pass_html(dirr):
    return fn.read_html(dirr)

#ingresar_nueva
#--------------------------------------
@eel.expose
def ingresar_nuevo(data):
    ans = cls['Ingresar_Nueva'].ingresar_nuevo(data)
    return ans

@eel.expose
def pedir_tipo_color_ing_nueva():
    ans = cls['Ingresar_Nueva'].pedir_tipo_color_nueva()
    return ans

#ingresar existente
#--------------------------------------
@eel.expose
def pedir_codigos_existentes():
    ans = cls['Ingresar_Existente'].get_cod_descr()
    return ans

@eel.expose
def ingresar_existente(data):
    ans = cls['Ingresar_Existente'].ingresar_existente(data)
    return ans

@eel.expose
def pedir_precio_costo(data):
    ans = cls['Ingresar_Existente'].pedir_precio_costo(data)
    return ans

#Editar
#--------------------------------------
@eel.expose
def pedir_todo_editar(data):
    ans = cls['Editar'].pedir_todo(data)
    return ans

@eel.expose
def editar_existente(data):
    ans = cls['Editar'].editar(data)
    return ans

@eel.expose
def borrar_existente(data):
    ans = cls['Editar'].borrar(data)
    return ans

#Ingresar Venta
#--------------------------------------
@eel.expose
def ingresar_venta(data):
    ans = cls['Ingresar_Venta'].ingresar_venta(data)
    return ans

@eel.expose
def pedir_cantidades_ventas(data):
    ans = cls['Ingresar_Venta'].pedir_cantidades(data)
    return ans

#Ingresar Devolución y Anular
#--------------------------------------
@eel.expose
def ingresar_devolucion(data):
    ans = cls['Ingresar_Devolucion'].ingresar_devolucion(data)
    return ans

@eel.expose
def anular_venta(data):
    ans = cls['Ingresar_Devolucion'].anular_venta(data)
    return ans

#inventario
#--------------------------------------
@eel.expose
def pedir_inventario_tabla():
    ans = cls['Inventario'].pedir_todo()
    return ans

@eel.expose
def crear_planilla_inventario():
    ans = cls['Inventario'].crear_planilla()
    ans = cls['Xls_Inventario'].crear_planilla_pd(ans)
    return ans

@eel.expose
def crear_planilla_fotos():
    ans = cls['Inventario'].crear_planilla()
    ans = cls['Xls_Fotos'].crear_planilla_pd(ans)
    return ans

@eel.expose
def subir_planilla_drive():
    ans = cls['Inventario'].crear_planilla()
    ans = cls['Xls_Inventario'].subir_planilla(ans)
    ans = cls['Base'].upload_sheet(ans,gle.Create_Service)
    return ans

#Ventas
#--------------------------------------
@eel.expose
def pedir_ventas_tabla():
    ans = cls['Ventas'].pedir_todo()
    return ans

@eel.expose
def crear_planilla_ventas():
    ans = cls['Ventas'].crear_planilla()
    ans = cls['Ventas'].crear_planilla_pd(ans)
    return ans


#Enviar Tienda
#--------------------------------------
@eel.expose
def pedir_codigos_enviar():
    ans = cls['Enviar_Tienda'].pedir_codigos()
    return ans

@eel.expose
def pedir_cantidad_max(data):
    ans = cls['Enviar_Tienda'].pedir_cantidad_max(data)
    return ans

@eel.expose
def mandar_tienda(data):
    ans = cls['Enviar_Tienda'].ingresar_tienda(data)
    ans2 = cls['Xls_Tienda'].crear_planilla_pd(data)
    return ans2 


#Enviar Casa
#--------------------------------------
@eel.expose
def pedir_codigos_enviar2():
    ans = cls['Enviar_Casa'].pedir_codigos()
    return ans

@eel.expose
def pedir_cantidad_max_casa(data):
    ans = cls['Enviar_Casa'].pedir_cantidad_max_casa(data)
    return ans

@eel.expose
def mandar_casa(data):
    ans = cls['Enviar_Casa'].ingresar_casa(data)
    return ans 

#historial
#--------------------------------------
@eel.expose
def pedir_historial_tabla():
    ans = cls['Historial'].pedir_todo()
    return ans

@eel.expose
def crear_planilla_historial():
    ans = cls['Historial'].crear_planilla()
    ans = cls['Xls_Historial'].crear_planilla_pd(ans)
    return ans

#actualizar base
#--------------------------------------
@eel.expose
def copy_path(data):
    ans = cls['Base'].copy_path(data)
    return ans

@eel.expose
def copy_path_foto(data):
    ans = cls['Base'].copy_path_foto(data)
    return ans

@eel.expose
def upload_base_web():
    ans = cls['Base'].upload_base(gle.Create_Service)
    return ans

@eel.expose
def download_base_web():
    ans = cls['Base'].download_base(gle.Create_Service)
    return ans

@eel.expose
def pedir_codigos_existentes_fotos():
    ans = cls['Base'].get_cod_descr()
    return ans


#Inicio 
#--------------------------------------
@eel.expose
def pedir_ventas_mensuales():
    ans = cls['Inicio'].get_meses()
    return ans

@eel.expose
def pedir_ventas_circular():
    ans = cls['Inicio'].get_circular()
    return ans

@eel.expose
def pedir_cantidades_inicio():
    ans = cls['Inicio'].get_cantidades()
    return ans

@eel.expose
def pedir_utilidades_costos_inicio():
    ans = cls['Inicio'].get_utilidad_costos()
    return ans 

@eel.expose
def comparar_bases():
    ans = cls['Inicio'].comparar_bases(gle.Create_Service)
    return ans

#analisis-inv
#--------------------------------------
@eel.expose
def pedir_tipos_analisis_total(data):
    ans = cls['Analisis'].pedir_tipos_total(data)
    return ans

#analisis-ventas
#--------------------------------------
@eel.expose
def pedir_tipos_analisis_ventas(data):
    ans = cls['Analisis'].pedir_tipos_ventas(data)
    return ans

#analisis-codigo
@eel.expose
def pedir_todo_analisis_codigo(data):
    ans = cls['Analisis'].pedir_codigo_analisis(data)
    return ans 

@eel.expose
def pedir_todo_analisis_ventas(data):
    ans = cls['Analisis'].pedir_ventas_codigo_analisis(data)
    return ans

@eel.expose
def pedir_query_analisis(data):
    ans = cls['Analisis'].pedir_query_analisis(data)
    return ans

#--------------------------------------

@eel.expose
def create_pdf_ventas(data):
    ans = cls['Pdf'].pedir_to_pdf(data)
    ppdf = pdf.create_pdf(ans)
    return True

#--------------------------------------

@eel.expose
def subir_fotos_drive():
    ans = cls['Drive_Fotos'].upload_if_not_exists(gle.Create_Service)
    return True

@eel.expose
def descargar_fotos_drive():
    ans = cls['Drive_Fotos'].download_if_not_exists(gle.Create_Service)
    return True

#--------------------------------------

def start_classes():
    cls = {'Ingresar_Nueva': fn.Ingresar_Nueva(),
            'Ingresar_Existente': fn.Ingresar_Existente(),
            'Editar': fn.Editar(),
            'Ingresar_Venta': fn.Ingresar_Venta(),
            'Ingresar_Devolucion': fn.Ingresar_Devolucion(),
            'Inventario': fn.Inventario(),
            'Ventas': fn.Ventas(),
            'Enviar_Tienda': fn.Enviar_Tienda(),
            'Enviar_Casa': fn.Enviar_Casa(),
            'Historial': fn.Historial(),
            'Base': fn.Base(),
            'Inicio': fn.Inicio(),
            'Analisis': fn.Analisis(),
            'Pdf': fn.Pdf(),
            'Xls_Inventario': xls.Inventario(),
            'Xls_Ventas': xls.Ventas(),
            'Xls_Fotos': xls.Fotos(),
            'Xls_Tienda': xls.Enviar_Tienda(),
            'Xls_Historial': xls.Historial(),
            'Drive_Fotos': fn.Fotos_Drive()}
    return cls

if __name__=='__main__':
    if fn.verify_keys():
        dev = True
        db.start()
        cls = start_classes()
        eel.init('src',allowed_extensions=['.js', '.html'])
        if dev:
            #eel.start('index.html',size=(1080,670))
            #eel.start('index.html', mode='custom', cmdline_args=['app/window/gestor-dominga.exe', '.'])
            eel.start('index.html', mode='custom', cmdline_args=['node_modules/electron/dist/electron.exe', '.'])
        else:
            fn.hideConsole()
            eel.start('index.html', mode='custom', cmdline_args=['window/gestor-dominga.exe', '.'])
    else:
        print("No permitido en este equipo")
        input("")
    
    


