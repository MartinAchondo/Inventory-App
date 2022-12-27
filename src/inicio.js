
$("document").ready(()=>{
    cargar_inicio_2();
});

async function cargar_inicio_2(){
    let data = await eel.pedir_ventas_mensuales()();
    let L_meses = data[0];
    let L_labels = data[1];
    grafico_linea = crear_grafico_barras(L_meses,L_labels);
    let data2 = await eel.pedir_ventas_circular()();
    let L_total = data2[0];
    let L_actual = data2[1];
    crear_grafico_circular(L_total,["Casa", "Tienda"],'grafico-circular1');
    crear_grafico_circular(L_actual,["Casa", "Tienda"],'grafico-circular2');

    let data3 = await eel.pedir_cantidades_inicio()();
    let total_casa = data3[0];
    let total_tienda = data3[1];
    let total = L_total[0]+L_total[1]; 
    
    let data4 = await eel.pedir_utilidades_costos_inicio()();
    let ut_total = data4[0];
    let cst_inv = data4[1];
    let ut_mes = data4[2];
    let ut_inv = data4[3];

    $("#index-total").html(money_format_format(total));
    $("#index-inventario").html(total_casa+total_tienda);
    $("#index-casa").html(total_casa);
    $("#index-tienda").html(total_tienda);
    $("#index-utilidad").html(money_format_format(ut_total));
    $("#index-cst-inv").html(money_format_format(cst_inv));
    $("#index-utilidadmes").html(money_format_format(ut_mes));
    $("#index-ut-inv").html(money_format_format(ut_inv));
};

document.getElementById('bar-chart').addEventListener('click',(evt)=>{
    const points = grafico_linea.getElementsAtEventForMode(evt, 'nearest', { intersect: true }, true);
    if (points.length) {
        const firstPoint = points[0];
        var label = grafico_linea.data.labels[firstPoint.index];
        var value = grafico_linea.data.datasets[firstPoint.datasetIndex].data[firstPoint.index];
        let fecha = label;
        analisis_venta_desde_inicio(fecha);
    };
}); 

$("#box-inventario").dblclick(()=>{
    analisis_inventario_desde_inicio();
});