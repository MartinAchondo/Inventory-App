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
        $("#ingresar-idventa").prop("disabled",false);
     });
  });

$('#form-ingresar-anular-venta').submit(async (e)=>{
    e.preventDefault();
    let codigo = $('#ingresar-codigo');
    let id = $('#ingresar-idventa');
    if (codigo.val()=='' ||  id.val()==''){
        console.log('faltan datos');
        mensaje('faltan datos','error');
        //window.fun.mensaje('Faltan Datos');
    }
    else{
    let data = {'codigo': codigo.val(),
                'id': id.val()
            };
    let resultado = await eel.anular_venta(data)();
    if (resultado == true){
        limpiar_devolucion();
        mensaje('Se Anuló venta','aviso');
        alerta_estado('subir');
    }else{
        mensaje(resultado);
    };
    };
});

function limpiar_devolucion(){
    $('#ingresar-codigo').val("");
    $('#ingresar-idventa').val("");
    $("#existente-select")[0].selectize.clear();
};


