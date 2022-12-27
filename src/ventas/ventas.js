$(document).ready(function () {
 
    let table = $('#ventas-datatable').DataTable({
        "scrollY": "50vh",
        "scrollCollapse": true,
        "pageLength": 100,
        "order": [[ 0, "desc" ]],
        "bInfo" : false,
        drawCallback: function () {
            $('#ventas-datatable_paginate ul.pagination').addClass("pagination-sm");   
        }
        });
        $('.dataTables_length').addClass('bs-select');
    mydata_table(table);

    table.on('dblclick','tr',function(){
        let codigo = table.row(this).data()[1];
        analisis_codigo_desde_tabla(codigo);
    });

    table.on('click','tr',function(){
        let row = table.row(this);
        if (row.child.isShown()){
            row.child.hide();
        }else{
            let codigo = row.data()[1];
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

    $('#search-color').on('keyup', function() {
        table.column(3).search($(this).val()).draw();
    });

    $('#search-descripcion').on('keyup', function() {
        table.column(2).search($(this).val()).draw();
    });

    $('#search-lugar-venta').change('keyup', function() {
        table.column(6).search($(this).val()).draw();
    });

    $('#search-fecha-min').change('keyup', function() {
        table.draw();
    });

    $('#search-fecha-max').change('keyup', function() {
        table.draw();
    });
});

async function mydata_table(tabla){
    data = await eel.pedir_ventas_tabla()();
    let lista = [];
    let lis;
    for (tupla of data){
        let real = tupla[5];
        if (tupla[4] == 'Tienda'){
            real = parseInt(real/0.9);
        };
        lis = [
            tupla[0],
            tupla[1],
            tupla[8],
            tupla[9],
            tupla[2],
            tupla[3],
            tupla[4],
            money_format_format(tupla[6]),
            money_format_format(real),
            tupla[7]
        ];
        lista.push(lis);
    };
    tabla.rows.add(lista).draw(true);
};

$("#tabla-excel2").click(async ()=>{
    let ans = await eel.crear_planilla_ventas()();
});

$.fn.DataTable.ext.classes.sFilterInput = "form-control form-control-sm";
$.fn.DataTable.ext.classes.pageLength = "form-control form-control-sm"; 


$.fn.dataTable.ext.search.push(
    function( settings, data, dataIndex ) {
        var fecha_min = $('#search-fecha-min').val();
        var fecha_max = $('#search-fecha-max').val();
        if (typeof fecha_min == "undefined"){
            return true;
        }
        var fecha = data[4];
        fecha = date_to_string_vent(fecha,true);
        fecha_max = date_to_string_vent(fecha_max,true);
        fecha_min = date_to_string_vent(fecha_min,true);
        if ( ( isNaN( fecha_min ) && isNaN( fecha_max ) ) ||
        ( isNaN( fecha_min )  && fecha <= fecha_max ) ||
        ( fecha_min <= fecha   && isNaN( fecha_max ) ) ||
        ( fecha_min <= fecha   && fecha <= fecha_max ) )
        {
            return true;
        }
            return false;
        }
);


function date_to_string_vent(date,bool){
    if (bool){
        let ano = date.slice(0,4);
        let mes = date.slice(5,7);
        let dia = date.slice(8);
        let ans = 400*parseInt(ano) + 32*parseInt(mes) + parseInt(dia);
        return ans
    }else {
        let ano = date.slice(6);
        let mes = date.slice(3,5);
        let dia = date.slice(0,2);
        let ans = 400*parseInt(ano) + 32*parseInt(mes) + parseInt(dia);
        return ans
    }

}