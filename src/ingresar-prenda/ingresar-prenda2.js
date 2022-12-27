$('document').ready(async function(){
    let ans = await eel.pedir_tipo_color_ing_nueva()();
    let L_color = ans[0];
    let L_tipo = ans[1];

    const contenedor_color = document.querySelector("#ingresar-color");
    let f_color = document.createDocumentFragment();
    for (color of L_color){
        const item = document.createElement('option');
        item.append(new Option(color, color));
        f_color.appendChild(item);
    };
    contenedor_color.appendChild(f_color);

    const contenedor_tipo = document.querySelector("#ingresar-tipo");
    let f_tipo = document.createDocumentFragment();
    for (tipo of L_tipo){
        const item = document.createElement('option');
        item.append(new Option(tipo, tipo));
        f_tipo.appendChild(item);
    };
    contenedor_tipo.appendChild(f_tipo);

    $("#form-ingresar-nueva").submit(async (e)=>{
        e.preventDefault();
        let tipo = $('#ingresar-tipo');
        let descripcion = $('#ingresar-descripcion');
        let color = $('#ingresar-color');
        let proovedor = $('#ingresar-proovedor');
        let costo = $('#ingresar-costo');
        let precio = $('#ingresar-precio');
        let preciotienda = $("#ingresar-precio-tienda");
        let cantidad = $('#ingresar-cantidad');
        if (tipo.val()=='' || preciotienda.val()=='' || descripcion.val()==''  || proovedor.val()=='' || costo.val()=='' || precio.val()=='' || cantidad.val()==''){
            mensaje('faltan datos','aviso')
            //window.fun.mensaje('Faltan Datos');
        }else{
            let data = {'tipo': tipo.val(),
                        'descripcion': descripcion.val(),
                        'color': color.val(),
                        'proovedor': proovedor.val(),
                        'costo': parseInt(costo.val()),
                        'precio': parseInt(precio.val()),
                        'cantidad': parseInt(cantidad.val()),
                        'preciotienda': parseInt(preciotienda.val())
                    };
            let resultado = await eel.ingresar_nuevo(data)();
            limpiar_nueva();
            mensaje(resultado,'aviso'); 
            alerta_estado('subir');   
        };
    });
});

function limpiar_nueva(){
    $('#ingresar-tipo').val("");
    $('#ingresar-descripcion').val("");
    $('#ingresar-color').val("");
    $('#ingresar-proovedor').val("");
    $('#ingresar-costo').val("");
    $('#ingresar-precio').val("");
    $("#ingresar-precio-tienda").val("");
    $('#ingresar-cantidad').val("");
};




