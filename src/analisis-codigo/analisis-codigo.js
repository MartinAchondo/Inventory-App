$('document').ready(async function(){
    await cargar_codigos();

    $("#existente-select").selectize({
        sortField: "text",
    });
});

async function cargar_codigos(){
    L_codigos = await eel.pedir_codigos_existentes()();
    const contenedor_existente = document.querySelector("#existente-select");
    let f_exist = document.createDocumentFragment();
    for (codigo of L_codigos){
        const item = document.createElement('option');
        item.append(new Option(codigo,codigo));
        f_exist.appendChild(item);
    };
    contenedor_existente.appendChild(f_exist);
};


$(function(){
    $("#existente-select").change('keyup', function(){
        let codigo_descr = $(this).val();
        let codigo = codigo_descr.slice(0,10);
        pedir_todo_analisis_codigo({'codigo': codigo});
   });
});

async function pedir_todo_analisis_codigo(data){
    let ans = await eel.pedir_todo_analisis_codigo(data)();

    $("#analisis-codigo").html(ans['codigo']);
    $("#analisis-tipo").html(ans['tipo']);
    $("#analisis-color").html(ans['color']);
    $("#analisis-descripcion").html(ans['descripcion']);
    $("#analisis-costo").html(money_format_format(ans['costo']));
    $("#analisis-preciocasa").html(money_format_format(ans['precio']));
    $("#analisis-preciotienda").html(money_format_format(ans['preciotienda']));
    $("#analisis-cantidadcasa").html(ans['cantidadcasa']);
    $("#analisis-cantidadtienda").html(ans['cantidadtienda']);
    let link_codigo = 'img-codigos/' + ans['codigo'] + '.jpg';
    $("#analisis-img").attr("src",link_codigo);

    let ans2 = await eel.pedir_todo_analisis_ventas(data)();
    $("#analisis-tbody").html("")
    let f_tabla = document.createDocumentFragment();
    for (venta of ans2){
        var tr = document.createElement("tr");
        var th1 = document.createElement("th");
        th1.innerHTML = venta['id'];
        tr.appendChild(th1);
        var th2 = document.createElement("th");
        th2.innerHTML = venta['fecha'];
        tr.appendChild(th2);
        var th3 = document.createElement("th");
        th3.innerHTML = venta['lugar'];
        tr.appendChild(th3);
        var th4 = document.createElement("th");
        th4.innerHTML = venta['cantidad'];
        tr.appendChild(th4);
        let precio = venta['precioventa'];
        if (venta['lugar']=='Tienda'){
            precio = parseInt(precio)/0.9;
        };
        var th5 = document.createElement("th");
        th5.innerHTML = money_format_format(precio);
        tr.appendChild(th5);
        var th6 = document.createElement("th");
        th6.innerHTML = venta['descuento'];
        tr.appendChild(th6);
        f_tabla.appendChild(tr)
    };
    document.querySelector("#analisis-tbody").appendChild(f_tabla); 
    if (ans2.length==0){
        $("#analisis-nada").html('No hay ventas')
    }else{
        $("#analisis-nada").html('')
    };
};