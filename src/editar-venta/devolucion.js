$('document').ready(async function(){
    await cargar_codigos();

    $("#existente-select").selectize({
        sortField: "text",
    });
});

async function cargar_codigos(){
    let L_codigos = await eel.pedir_codigos_existentes()();
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
        let elmt = $('#ingresar-codigo');
        let codigo = codigo_descr.slice(0,10);
        elmt.val(codigo);
        elmt.prop( "disabled", true );
        $("#ingresar-lugar").prop( "disabled", false );
     });
  });

$("#search-devolucion").on("keyup", function() {
    var value = $(this).val().toLowerCase();
    $(".dropdown-menu button").filter(function() {
      $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1);
    });
  });

$('#form-ingresar-devolucion').submit(async (e)=>{
    e.preventDefault();
    let codigo = $('#ingresar-codigo');
    let lugar = $('#ingresar-lugar');
    let precio = $('#ingresar-precio');
    let cantidad = $('#ingresar-cantidad');
    if (codigo.val()=='' ||  lugar.val()=='' || precio.val()=='' || cantidad.val()==''){
        console.log('faltan datos');
        mensaje('faltan datos','error');
        //window.fun.mensaje('Faltan Datos');
    }
    else{
    let data = {'codigo': codigo.val(),
                'lugar': lugar.val(),
                'precioventa': parseInt(precio.val()),
                'cantidad': parseInt(cantidad.val())
            };
        let resultado = await eel.ingresar_devolucion(data)();
        if (resultado == true){
            limpiar_devolucion();
            mensaje('Se Agregó Devolución','aviso');
            alerta_estado('subir');
        }else{
            mensaje(resultado);
        };
    };
});

function limpiar_devolucion(){
    $('#ingresar-codigo').val("");
    $('#ingresar-lugar').val("");
    $('#ingresar-precio').val("");
    $('#ingresar-cantidad').val("");
    $("#ingresar-lugar").prop( "disabled", true );
    $("#existente-select")[0].selectize.clear();
};

$( "#ingresar-lugar" ).change(async function() {
    let lugar = $("#ingresar-lugar").val();
    let codigo = $("#ingresar-codigo").val();
    let data = {'codigo': codigo};
    let ans = await eel.pedir_precio_costo(data)();
    let precio = ans[1];
    let precio_tienda = ans[2];
    if (lugar=="Casa"){
        $('#ingresar-precio').val(precio);
    }else if (lugar=="Tienda"){
        $('#ingresar-precio').val(precio_tienda);
    };
  });
