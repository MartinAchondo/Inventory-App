import os
import numpy as np
import pandas as pd
from fpdf import FPDF
import matplotlib.pyplot as plt

def create_plot(name_plot,labels,values):
    fig, ax = plt.subplots()
    fig.set_size_inches(3, 3)
    wedges, autotexts = ax.pie(values, startangle=90)
    plt.legend(wedges, labels, loc='lower right')
    path_plot = os.path.join(os.getcwd(),'pdfs','plots',name_plot)
    plt.savefig(path_plot)


def create_pdf(data):
    L_ventas,L_circ_tipos,L_circ_ventas,ut_total,fecha = data
    df = pd.DataFrame(L_ventas)
    df['precioventa'] = np.where(df.lugar == 'Tienda', df['precioventa']/0.9, df['precioventa'])
    df = df[['id','codigo','descripcion','color','fecha','cantidad','lugar','precioventa','descuento']]
    create_plot('p1.png',L_circ_tipos[0],L_circ_tipos[1])
    create_plot('p2.png',L_circ_ventas[0],L_circ_ventas[1])
    save_pdf(df,fecha,L_circ_ventas,ut_total,L_circ_tipos)
    

def save_pdf(df,fecha,ventas,utilidad,tipos):
    pdf=FPDF(format='letter')
    pdf.add_page() 
    pdf.set_font('arial', 'B', 14)
    pdf.cell(60)
    pdf.cell(75, 10, 'Análisis de Ventas de {}'.format(fecha), 0, 2, 'C')
    pdf.cell(90, 15, '', 0, 2, 'C')

    pdf.set_font('arial','B',11)
    pdf.ln(10)
    pdf.cell(30)
    pdf.cell(35,10,'Ventas Totales:',ln=0,align='C')
    pdf.cell(35,10,'$' + str(ventas[1][0]+ventas[1][1]),align='C')
    pdf.ln(15)
    pdf.cell(30)
    pdf.cell(35,10,'Utilidad Total:',ln=0,align='C')
    pdf.cell(35,10,'$' + str(utilidad),align='C')
    pdf.ln(30)

    path_x = os.path.join(os.getcwd(),'pdfs','plots')
    pdf.ln(0.5)
    pdf.cell(60)
    pdf.cell(35,10,'Ventas Por Lugar',align='C')
    pdf.ln(8)
    pdf.cell(20)
    pdf.image(os.path.join(path_x,'p2.png'), x = None, y = None, w=0, h=0, type='', link='')
    pdf.ln(10)
    pdf.set_font('arial','B', 11)
    pdf.cell(45)
    pdf.cell(35, 10, 'Lugar', border=1, ln=0, align='C')
    pdf.cell(35, 10, 'Cantidad', border=1, ln=0, align='C')
    pdf.set_font('arial','', 11)
    for j in range(len(ventas[0])):
        pdf.ln(10)
        pdf.cell(45)
        pdf.cell(35, 10, ventas[0][j], border=1, ln=0, align='C')
        pdf.cell(35, 10, '$' + str(ventas[1][j]), border=1, ln=0, align='C')

    pdf.ln(40)
    pdf.add_page()
    pdf.set_font('arial','B', 11)
    pdf.cell(60)
    pdf.cell(35,10,'Tipos de Prendas Vendidos',align='C')
    pdf.ln(8)
    pdf.cell(20)
    pdf.image(os.path.join(path_x,'p1.png'), x = None, y = None, w=0, h=0, type='', link='')
    pdf.ln(10)
    pdf.set_font('arial','B', 11)
    pdf.cell(45)
    pdf.cell(35, 10, 'Tipos', border=1, ln=0, align='C')
    pdf.cell(35, 10, 'Cantidad', border=1, ln=0, align='C')
    pdf.set_font('arial','', 11)
    for j in range(len(tipos[0])):
        pdf.ln(10)
        pdf.cell(45)
        pdf.cell(35, 10, tipos[0][j], border=1, ln=0, align='C')
        pdf.cell(35, 10, str(tipos[1][j]), border=1, ln=0, align='C') 

    epw = pdf.w - 2*pdf.l_margin
    col_width = epw/8

    pdf.ln(40)
    pdf.add_page()
    pdf.set_font('arial','B', 11)
    pdf.cell(60)
    pdf.cell(35,10,'Ventas',align='C')
    pdf.ln(15)
    pdf.set_font('arial','B', 9)

    pdf.cell(col_width/5+2, 10, 'Id', border=1, ln=0, align='C')
    pdf.cell(col_width+3, 10, 'Código', border=1, ln=0, align='C')
    pdf.cell(col_width*3-3, 10, 'Descripción', border=1, ln=0)
    pdf.cell(col_width-2, 10, 'Color', border=1, ln=0, align='C')
    pdf.cell(col_width-2, 10, 'Fecha', border=1, ln=0, align='C')
    pdf.cell(col_width/4+3, 10, 'Cant', border=1, ln=0, align='C')
    pdf.cell(col_width/2, 10, 'Lugar', border=1, ln=0, align='C')
    pdf.cell(col_width/2, 10, 'Precio', border=1, ln=0, align='C')
    pdf.cell(col_width/3+2, 10, 'Dscto', border=1, ln=0, align='C')
    pdf.set_font('arial', '', 8)
    pdf.ln(10)
    for i in range(0, len(df)):
        pdf.cell(col_width/5+2, 10, str(df['id'][i]), border=1, ln=0, align='C')
        pdf.cell(col_width+3, 10, df['codigo'][i], border=1, ln=0, align='C')
        pdf.cell(col_width*3-3, 10, df['descripcion'][i], border=1, ln=0)
        pdf.cell(col_width-2, 10, df['color'][i], border=1, ln=0, align='C')
        pdf.cell(col_width-2, 10, df['fecha'][i], border=1, ln=0, align='C')
        pdf.cell(col_width/4+3, 10, str(df['cantidad'][i]), border=1, ln=0, align='C')
        pdf.cell(col_width/2, 10, df['lugar'][i], border=1, ln=0, align='C')
        pdf.cell(col_width/2, 10, '$' + str(int(df['precioventa'][i])), border=1, ln=0, align='C')
        pdf.cell(col_width/3+2, 10, str(df['descuento'][i]), border=1, ln=0, align='C')
        pdf.ln(10)
    pdf.cell(90, 10, '', 0, 2, 'C')
    pdf.cell(55, 10, '', 0, 0, 'C')

    path_pdf = os.path.join(os.getcwd(),'exports','Ventas.pdf')
    pdf.output(path_pdf, 'F')
    os.startfile(path_pdf)
    