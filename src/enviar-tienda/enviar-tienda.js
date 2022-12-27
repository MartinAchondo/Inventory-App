$('document').ready(async function(){
    await cargar_codigos();

    $("#existente-select").selectize({
      sortField: "text",
    });
 
    var table = $('#enviar-datatable').DataTable({
        "scrollY": "20vh",
        "scrollCollapse": true,
        "pageLength": 100,
        "order": [[ 0, "desc" ]],
        searching: false,
        paging: false,
        info: false
        });
        $('.dataTables_length').addClass('bs-select');


      $('#form-enviar-tienda').submit(async (e)=>{
        e.preventDefault();
        let codigo_descr = $("#existente-select").val();    
        let codigo = codigo_descr.slice(0,10);
        let cantidad = $("#enviar-cantidad");
        let precio = $("#enviar-precio");
        let descripcion = codigo_descr.slice(13);
        let lista = [codigo,descripcion,cantidad.val(),money_format_format(precio.val())];
        table.row.add(lista).draw(true);
        $("#existente-select")[0].selectize.clear();
        let $select = $('#existente-select').selectize(); 
        let selectSizeControl = $select[0].selectize; 
        let selectedValue = selectSizeControl.getValue()
        selectSizeControl.removeOption( selectedValue )
        cantidad.val('');
        precio.val('');
        $("#existente-select")[0].selectize.clear();
        $("#ingresar-img").attr("src",'img-codigos/none.jpg');
      });


    $("#enviar-tienda").click(()=>{
      let lista = [];
      var data = table.rows().data();
      data.each(function (value, index) {
          let dic = {'codigo':value[0],'descripcion':value[1], 'cantidad':value[2],'precio':value[3]};
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
    let L_codigos = await eel.pedir_codigos_enviar()();
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
    let link_codigo = 'img-codigos/' + codigo + '.jpg';
    $("#ingresar-img").attr("src",link_codigo);
    if (codigo != ""){
      pedir_precio_costo(codigo);
      pedir_cantidad_max(codigo);
    };
 });
});

  async function pedir_precio_costo(codigo){
    let data = {'codigo': codigo};
    let ans = await eel.pedir_precio_costo(data)();
    let costo = ans[0];
    let precio = ans[1];
    let precio_tienda = ans[2]
    $('#enviar-precio').val(precio_tienda);  
  };

async function pedir_cantidad_max(codigo){
  let data = {'codigo': codigo};
  let ans = await eel.pedir_cantidad_max(data)();
  let cant = ans;
  $("#enviar-cantidad").attr({"max":cant});
};

async function mandar_tienda(dic){
  let ans = await eel.mandar_tienda(dic)();
  alerta_estado('subir');
  $("#index-item-enviar-tienda").click();
};

