$('document').ready(async function(){
    await cargar_codigos();
 
    $("#existente-select").selectize({
      sortField: "text",
    });

    var table = $('#casa-datatable').DataTable({
        "scrollY": "20vh",
        "scrollCollapse": true,
        "pageLength": 100,
        "order": [[ 0, "desc" ]],
        });
        $('.dataTables_length').addClass('bs-select');


      $('#form-enviar-casa').submit(async (e)=>{
        e.preventDefault();
        let codigo_descr = $("#existente-select").val();    
        let codigo = codigo_descr.slice(0,10);
        let descripcion = codigo_descr.slice(13);
        let cantidad = $("#casa-cantidad");
        let lista = [codigo,descripcion,cantidad.val()];
        table.row.add(lista).draw(true);
        $("#existente-select")[0].selectize.clear();
        let $select = $('#existente-select').selectize(); 
        let selectSizeControl = $select[0].selectize; 
        let selectedValue = selectSizeControl.getValue()
        selectSizeControl.removeOption( selectedValue )
        cantidad.val('');
        $("#existente-select")[0].selectize.clear();
      });


    $("#casa-tienda").click(()=>{
      let lista = [];
      var data = table.rows().data();
      data.each(function (value, index) {
          let dic = {'codigo':value[0],'cantidad':value[2]};
          lista.push(dic);
      });
      if (lista.length>0){
        mandar_tienda(lista);
        table.clear();
        table.draw();
      };
    });
});

async function cargar_codigos(){
    let L_codigos = await eel.pedir_codigos_enviar2()();
    const contenedor_existente = document.querySelector("#existente-select");
    let f_exist = document.createDocumentFragment();
    for (codigo of L_codigos){
        const item = document.createElement('option');
        item.append(new Option(codigo,codigo));
        item.classList.add(codigo.slice(0,10));
        f_exist.appendChild(item);
    };
    contenedor_existente.appendChild(f_exist);
};

$(function(){
  $("#existente-select").change('keyup', function(){
    let codigo_descr = $(this).val();
    let codigo = codigo_descr.slice(0,10);
    console.log(codigo)
    if (codigo != ""){
      pedir_cantidad_max_casa(codigo);
    };
 });
});


async function pedir_cantidad_max_casa(codigo){
  let data = {'codigo': codigo};
  let ans = await eel.pedir_cantidad_max_casa(data)();
  let cant = ans;
  $("#casa-cantidad").attr({"max":cant});
}

async function mandar_tienda(dic){
  let ans = await eel.mandar_casa(dic)();
  mensaje(ans,'aviso');
  alerta_estado('subir');
  $("#index-item-enviar-casa").click();
};

