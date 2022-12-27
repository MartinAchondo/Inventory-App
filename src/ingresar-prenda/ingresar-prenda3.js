
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
      let elmt = $('#ingresar-codigo');
      let codigo = codigo_descr.slice(0,10);
      elmt.val(codigo);
      elmt.prop( "disabled", true );
      let link_codigo = 'img-codigos/' + codigo + '.jpg';
      $("#ingresar-img").attr("src",link_codigo);
      pedir_precio_costo();
   });
});

  $('#form-ingresar-existente').submit(async (e)=>{
    e.preventDefault();
    let codigo = $('#ingresar-codigo');
    let proovedor = $('#ingresar-proovedor');
    let costo = $('#ingresar-costo');
    let precio = $('#ingresar-precio');
    let preciotienda = $("#ingresar-precio-tienda");
    let cantidad = $('#ingresar-cantidad');
    if (codigo.val()=='' || preciotienda.val()=='' || proovedor.val()=='' || costo.val()=='' || precio.val()=='' || cantidad.val()==''){
        console.log('faltan datos');
        mensaje('faltan datos','error')
        //window.fun.mensaje('Faltan Datos');
    }else{
        let data = {'codigo': codigo.val(),
                    'proovedor': proovedor.val(),
                    'costo': parseInt(costo.val()),
                    'precio': parseInt(precio.val()),
                    'preciotienda': parseInt(preciotienda.val()),
                    'cantidad': parseInt(cantidad.val())
                };
        let resultado = await eel.ingresar_existente(data)();
        if (resultado == true){ 
            limpiar_existente();
            mensaje('Se agregó prenda','aviso');
            alerta_estado('subir');
        }else{
            mensaje(resultado);
        };
    };
});

async function pedir_precio_costo(){
  let codigo = $('#ingresar-codigo').val();
  let data = {'codigo': codigo};
  let ans = await eel.pedir_precio_costo(data)();

  let costo = ans[0];
  let precio = ans[1];
  let precio_tienda = ans[2];

  $('#ingresar-precio').val(precio);
  $('#ingresar-costo').val(costo);
  $('#ingresar-precio-tienda').val(precio_tienda);
};

function limpiar_existente(){
    $('#ingresar-proovedor').val("");
    $('#ingresar-costo').val("");
    $('#ingresar-precio').val("");
    $("#ingresar-precio-tienda").val("");
    $('#ingresar-cantidad').val("");
    $('#ingresar-codigo').val("");
    $("#ingresar-codigo").prop( "disabled", true );
    $("#ingresar-img").attr("src",'img-codigos/none.jpg');
    $("#existente-select")[0].selectize.clear();
};