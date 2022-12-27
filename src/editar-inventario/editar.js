
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
        let elmt = $('#ingresar-codigo')
        let codigo = codigo_descr.slice(0,10);
        elmt.val(codigo);
        let link_codigo = 'img-codigos/' + codigo + '.jpg';
        $("#ingresar-img").attr("src",link_codigo);
        elmt.prop( "disabled", true );
        pedir_todo();
     });
  });

  $('#form-ingresar-editar').submit(async (e)=>{
    e.preventDefault();
    let codigo = $('#ingresar-codigo');
    let costo = $('#ingresar-costo');
    let precio = $('#ingresar-precio');
    let preciotienda = $("#ingresar-precio-tienda");
    let cantidad1 = $('#ingresar-cantidad');
    let descripcion = $('#ingresar-descripcion');
    let cantidad2 = $('#ingresar-cantidad2');
    cantidad_t = parseInt(cantidad1.val()) + parseInt(cantidad2.val());
    let data = {'codigo': codigo.val(),
                'descripcion': descripcion.val(),
                'costo': parseInt(costo.val()),
                'precio': parseInt(precio.val()),
                'preciotienda': parseInt(preciotienda.val()),
                'cantidadcasa': parseInt(cantidad1.val()),
                'cantidadtienda': parseInt(cantidad2.val()),
                'cantidad': cantidad_t
            };
    let resultado = await eel.editar_existente(data)();
    limpiar_editar();
    if (resultado == true){
        mensaje('Se editó prenda','aviso');
        alerta_estado('subir');
    }else{
        mensaje(resultado);
    };
});

$("#ingresar-borrar").click(async ()=>{
    let codigo = $('#ingresar-codigo');
    let data = {'codigo': codigo.val()};
    if (codigo.val() != ""){
        let ans = eel.borrar_existente(data)();
        limpiar_editar();
        mensaje("Se borró código","aviso");
        alerta_estado('subir'); 
    }else{
        mensaje("No se seleccionó código","aviso");
    };

});

async function pedir_todo(){
  let codigo = $('#ingresar-codigo').val();
  let data = {'codigo': codigo};

  let ans = await eel.pedir_todo_editar(data)();

  let costo = ans['costo'];
  let precio = ans['precio'];
  let precio_tienda = ans['preciotienda'];
  let descripcion = ans['descripcion'];
  let cantidad_casa = ans['cantidadcasa'];
  let cantidad_tienda = ans['cantidadtienda'];

  $('#ingresar-precio').val(precio);
  $('#ingresar-costo').val(costo);
  $('#ingresar-precio-tienda').val(precio_tienda);
  $('#ingresar-descripcion').val(descripcion);
  $('#ingresar-cantidad').val(cantidad_casa);
  $('#ingresar-cantidad2').val(cantidad_tienda);  
};
function limpiar_editar(){
    $('#ingresar-precio').val("");
    $('#ingresar-costo').val("");
    $('#ingresar-precio-tienda').val("");
    $('#ingresar-descripcion').val("");
    $('#ingresar-cantidad').val("");
    $('#ingresar-cantidad2').val("");  
    $('#ingresar-codigo').val("");
    $("#ingresar-img").attr("src",'img-codigos/none.jpg');
    $("#existente-select")[0].selectize.clear();
}
