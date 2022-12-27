$(document).ready(async function () {
 
    let table = $('#inventario-datatable').DataTable({
        "scrollY": "50vh",
        "scrollCollapse": true,
        "pageLength": 100,
        "order": [[ 0, "asc" ]],
        "bInfo" : false,
        drawCallback: function () {
            $('#inventario-datatable_paginate ul.pagination').addClass("pagination-sm");   
        }
        });
        $('.dataTables_length').addClass('bs-select');
    mydata_table(table);

    table.on('dblclick','tr',function(){
        let codigo = table.row(this).data()[0];
        analisis_codigo_desde_tabla(codigo);
    });

    table.on('click','tr',function(){
        let row = table.row(this);
        if (row.child.isShown()){
            row.child.hide();
        }else{
            let codigo = row.data()[0];
            row.child(format_child(codigo)).show();
            let link_codigo = 'img-codigos/' + codigo + '.jpg';
            $(".inv-" + codigo).attr("src",link_codigo);
        };
    });

    function format_child(codigo){
        let error = "this.src='img-codigos/none.jpg';"
        return '<div class="foto-tablas">' +
                    '<p> Código: ' + codigo + '</p>' + 
                    '<img id="inv-img" class="inv-'+ codigo + '" src="#" onerror='+ error + ' alt="Sin Foto" height=100>'+ 
                '</div>';
    };

    let ans = await eel.pedir_tipo_color_ing_nueva()();
    let L_color = ans[0];
    let L_tipo = ans[1];

    const contenedor_color = document.querySelector("#search-color");
    let f_color = document.createDocumentFragment();
    for (color of L_color){
        const item = document.createElement('option');
        item.append(new Option(color, color));
        f_color.appendChild(item);
    };
    contenedor_color.appendChild(f_color);

    const contenedor_tipo = document.querySelector("#search-tipo");
    let f_tipo = document.createDocumentFragment();
    for (tipo of L_tipo){
        const item = document.createElement('option');
        item.append(new Option(tipo, tipo));
        f_tipo.appendChild(item);
    };
    contenedor_tipo.appendChild(f_tipo);

    $("#search-color").selectize({
        sortField: "text",
    });

    $("#search-lugar-inv").selectize({
        sortField: "text",
    });

    $('#search-tipo').change('keyup', function() {
        table.column(1).search($(this).val()).draw();
    });

    $('#search-color').change('keyup', function() {
        table.column(3).search($(this).val()).draw();
    });

    $('#search-descripcion').on('keyup', function() {
        table.column(2).search($(this).val()).draw();
    });

    $('#search-lugar-inv').change('keyup', function() {
        table.draw();
    });

});

async function mydata_table(tabla){
    data = await eel.pedir_inventario_tabla()();
    let lista = [];
    let lis;
    for (tupla of data){
        lis = [
            tupla[1],
            tupla[2],
            tupla[3],
            tupla[4],
            tupla[9],
            tupla[10],
            tupla[7],
            money_format_format(tupla[5]),
            money_format_format(tupla[6]),
            money_format_format(tupla[8])
        ];
        lista.push(lis);
    };
    tabla.rows.add(lista).draw(true);
};

$("#tabla-excel").click(async ()=>{
    let ans = await eel.crear_planilla_inventario()();
});

$("#tabla-excel-fotos").click(async ()=>{
    let ans = await eel.crear_planilla_fotos()();
});

$("#tabla-excel-drive").click(async ()=>{
    let ans = await eel.subir_planilla_drive()();
    mensaje(ans,'texto')
});

$.fn.DataTable.ext.classes.sFilterInput = "form-control form-control-sm";
$.fn.DataTable.ext.classes.pageLength = "form-control form-control-sm"; 

$.fn.dataTable.ext.search.push(
    function( settings, data, dataIndex ) {
        var lugar = $('#search-lugar-inv').val();
        var cant_casa = parseInt( data[4] ) || 0;
        var cant_tienda = parseInt( data[5] ) || 0;
        if (typeof lugar == "undefined"){
            return true
        }
        if (lugar=="Casa"){
            if (cant_casa != 0){
                return true;
            };
            return false;
        };
        if (lugar=="Tienda"){
            if (cant_tienda != 0){
                return true;
            };
            return false;
        };
        return true;
    }
);
