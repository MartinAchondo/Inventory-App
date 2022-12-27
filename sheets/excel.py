import os
import shutil
import xlsxwriter
import numpy as np
import pandas as pd
from datetime import date


class Inventario():

    def __init__(self):
        self.path_book = os.path.join(os.getcwd(),'exports','Inventario.xlsx')
        self.d1 = date.today().strftime("%Y/%m/%d")

    def crear_planilla_pd(self,data):
        df = pd.DataFrame(data)
        writer = pd.ExcelWriter(self.path_book, engine='xlsxwriter')
        df.to_excel(writer, sheet_name='Inventario')
        workbook  = writer.book
        workbook.filename = self.path_book.replace('.xlsx','') + '.xlsm'
        root = os.path.dirname(os.path.realpath(__file__))
        path_vba = os.path.join(root, 'bin_vbaprojects/vbaProject_inventario.bin')
        workbook.add_vba_project(path_vba)
        worksheet = workbook.add_worksheet()
        worksheet.write('A1', 'sos')
        worksheet.write("A2",self.d1)
        worksheet2 = workbook.add_worksheet("TablaTipos")
        worksheet3 = workbook.add_worksheet("Guardar")
        worksheet3.insert_button('B2', {'macro': 'guardar_como1',
                        'caption': 'Click Para Guardar',
                        'width': 200,
                        'height': 60})
        writer.save()
        path_run = self.path_book.replace('.xlsx','') + '.xlsm'
        os.startfile(path_run)
        return True

    def subir_planilla(self,data):
        df = pd.DataFrame(data)
        writer = pd.ExcelWriter(self.path_book, engine='xlsxwriter')
        df.to_excel(writer, sheet_name='Inventario')

        workbook  = writer.book
        workbook.filename = self.path_book.replace('.xlsx','') + '.xlsm'
        root = os.path.dirname(os.path.realpath(__file__))
        path_vba = os.path.join(root, 'bin_vbaprojects/vbaProject_inventario.bin')
        workbook.add_vba_project(path_vba)
        worksheet = workbook.add_worksheet()
        worksheet.write('A1', 'sos')
        worksheet.write("A2",self.d1)
        worksheet2 = workbook.add_worksheet("TablaTipos")
        worksheet3 = workbook.add_worksheet("Guardar")
        worksheet3.insert_button('B2', {'macro': 'guardar_como1',
                        'caption': 'Click Para Guardar',
                        'width': 200,
                        'height': 60})
        writer.save()
        path_run = self.path_book.replace('.xlsx','') + '.xlsm'
        os.system(path_run)
        return path_run

class Ventas():

    def __init__(self):
        self.path_book = os.path.join(os.getcwd(),'exports','Ventas.xlsx')
        self.d1 = date.today().strftime("%Y/%m/%d")

    def crear_planilla_pd(self,data):
        df = pd.DataFrame(data)
        df['precioventa'] = np.where(df.lugar == 'Tienda', df['precioventa']/0.9, df['precioventa'])
        df = df[['id','codigo','descripcion','color','fecha','cantidad','lugar','precioreal','precioventa','descuento']]
        writer = pd.ExcelWriter(self.path_book, engine='xlsxwriter')
        df.to_excel(writer, sheet_name='Ventas')
        workbook  = writer.book
        workbook.filename = self.path_book.replace('.xlsx','') + '.xlsm'
        root = os.path.dirname(os.path.realpath(__file__))
        path_vba = os.path.join(root, 'bin_vbaprojects/vbaProject_ventas.bin')
        workbook.add_vba_project(path_vba)
        worksheet = workbook.add_worksheet()
        worksheet.write('A1', 'sos')
        writer.save()
        os.startfile(self.path_book.replace('.xlsx','') + '.xlsm')
        return True

class Historial():

    def __init__(self):
        self.path_book = os.path.join(os.getcwd(),'exports','Historial.xlsx')
        self.d1 = date.today().strftime("%Y/%m/%d")

    def crear_planilla_pd(self,data):
        df = pd.DataFrame(data)
        writer = pd.ExcelWriter(self.path_book, engine='xlsxwriter')
        df.to_excel(writer, sheet_name='Historial')
        workbook  = writer.book
        workbook.filename = self.path_book.replace('.xlsx','') + '.xlsm'
        root = os.path.dirname(os.path.realpath(__file__))
        path_vba = os.path.join(root, 'bin_vbaprojects/vbaProject_historial.bin')
        workbook.add_vba_project(path_vba)
        worksheet = workbook.add_worksheet()
        worksheet.write('A1', 'sos')
        writer.save()
        os.startfile(self.path_book.replace('.xlsx','') + '.xlsm')
        return True

class Enviar_Tienda():

    def __init__(self):
        self.path_book = os.path.join(os.getcwd(),'exports','Tienda.xlsx')
        self.d1 = date.today().strftime("%Y/%m/%d")

    def pedir_path(self,ext):
        today = date.today()
        d1 = today.strftime("%Y/%m/%d")
        path = 'Tienda' + ext
        path = path.replace('/','_')
        path = os.path.join(os.getcwd(),'exports',path)
        return path

    def crear_planilla_pd(self,data):
        df = pd.DataFrame(data)
        writer = pd.ExcelWriter(self.path_book, engine='xlsxwriter')
        df.to_excel(writer, sheet_name='Envío')
        workbook  = writer.book
        workbook.filename = self.path_book.replace('.xlsx','') + '.xlsm'
        root = os.path.dirname(os.path.realpath(__file__))
        path_vba = os.path.join(root, 'bin_vbaprojects/vbaProject_tienda.bin')
        workbook.add_vba_project(path_vba)
        worksheet = workbook.add_worksheet()
        worksheet.write('A1', 'sos')
        writer.save()
        os.startfile(self.path_book.replace('.xlsx','') + '.xlsm')
        return True

class Fotos():

    def __init__(self):
        self.path_book = os.path.join(os.getcwd(),'exports','Codigos.xlsx')
        self.d1 = date.today().strftime("%Y/%m/%d")

    def crear_planilla_pd(self,data):
        df1 = pd.DataFrame(data)
        df = df1.iloc[:,[1,3]]
        writer = pd.ExcelWriter(self.path_book, engine='xlsxwriter')
        df.to_excel(writer, sheet_name='Códigos')
        workbook  = writer.book
        workbook.filename = self.path_book.replace('.xlsx','') + '.xlsm'
        root = os.path.dirname(os.path.realpath(__file__))
        path_vba = os.path.join(root, 'bin_vbaprojects/vbaProject_fotos.bin')
        workbook.add_vba_project(path_vba)
        worksheet = workbook.add_worksheet()
        worksheet.write('A1', 'sos')
        path2 = os.path.join(os.getcwd(),'src','img-codigos')
        worksheet.write('A2',path2)
        writer.save()
        os.startfile(self.path_book.replace('.xlsx','') + '.xlsm')
        return True