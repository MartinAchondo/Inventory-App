
$("document").ready(async ()=>{
    await cargar_codigos_foto();
    
    $("#existente-select").selectize({
        sortField: "text",
    });

    $("#foto-buscar").click(()=>{
        ask_path_foto($("#base-codigo").val());
        limpiar_foto();
    });
})

$(function(){
    $("#existente-select").change('keyup', function(){
        let codigo_descr = $(this).val();
        let elmt = $('#base-codigo')
        let codigo = codigo_descr.slice(0,10);
        elmt.val(codigo);
        elmt.prop( "disabled", true );
        $("#foto-buscar").prop("disabled",false); 
   });
});

async function cargar_codigos_foto(){
    L_codigos = await eel.pedir_codigos_existentes_fotos()();
    const contenedor_existente = document.querySelector("#existente-select");
    let f_exist = document.createDocumentFragment();
    for (codigo of L_codigos){
        const item = document.createElement('option');
        item.append(new Option(codigo,codigo));
        f_exist.appendChild(item);
    };
    contenedor_existente.appendChild(f_exist);
};

function limpiar_foto(){  
    $('#base-codigo').val("");
    $(".editar-gbtn").text("Buscar Código-Descripción");
    $("#foto-buscar").prop("disabled",true);
    $("#existente-select")[0].selectize.clear();
}

$("#fotos-subir").click(async ()=>{
    let ans = await eel.subir_fotos_drive()();
    mensaje(ans,'sos')
});

$("#fotos-descargar").click(async ()=>{
    let ans = await eel.descargar_fotos_drive()();
    mensaje(ans,'sos')
});