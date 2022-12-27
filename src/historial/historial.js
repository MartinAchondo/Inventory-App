$(document).ready(function () {
 
    let table = $('#historial-datatable').DataTable({
        "scrollY": "50vh",
        "scrollCollapse": true,
        "pageLength": 100,
        "order": [[ 0, "desc" ]],
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

});

async function mydata_table(tabla){
    let data = await eel.pedir_historial_tabla()();
    let lista = [];
    let lis;
    for (tupla of data){
        lis = [
            tupla[0],
            tupla[1],
            tupla[3],
            tupla[2],
            tupla[4],
        ];
        lista.push(lis);
    };
    tabla.rows.add(lista).draw(true);
}

$("#tabla-excel5").click(async ()=>{
    await eel.crear_planilla_historial()();
});