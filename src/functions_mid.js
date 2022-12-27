
async function analisis_codigo_desde_tabla(codigo){
    await cargar_html_codigo();
    pedir_todo_analisis_codigo_inv({'codigo': codigo});
};

async function cargar_html_codigo(){
    let container = document.querySelector('.index-medium-container-main');
    container.innerHTML = await eel.pass_html("src/analisis-codigo/analisis-codigo.html")();
    borrar_null_tags();
    let script = document.createElement('script');
    script.src = 'analisis-codigo/analisis-codigo.js';
    script.classList.add('nulo');
    document.body.appendChild(script);
    var link = document.createElement('link');
    link.type = 'text/css';
    link.rel = 'stylesheet';
    link.href = 'analisis-codigo/analisis-codigo.css';
    link.classList.add('nulo');
    document.head.appendChild(link);
}

async function pedir_todo_analisis_codigo_inv(data){
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
    console.log(link_codigo)
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

//--------------------------------------------------------------------------------

async function analisis_venta_desde_inicio(fecha){
    await cargar_html_ventas();
    let fecha_c = fecha.slice(3) + '/' + fecha.slice(0,2);
    let ans = await eel.pedir_tipos_analisis_ventas(fecha_c)();
    if (ans.length != 0){
        crear_analisis_ventas_todo2(ans);
    }else{
        crear_nuevo_analisis_chart2();
        limpiar_analisis_ventas2();
    };
    $("#ingresar-ano").addClass("ano");
    $("#ingresar-mes").addClass("mes");
    let dic = {
        "01": "Enero",
        "02": "Febrero",
        "03": "Marzo",
        "04": "Abril",
        "05": "Mayo",
        "06": "Junio",
        "07": "Julio",
        "08": "Agosto",
        "09": "Septiembre",
        "10": "Octubre",
        "11": "Noviembre",
        "12": "Diciembre"
    };
    $(".check-analisis-ano").attr("id",fecha.slice(3));
    $(".check-analisis-mes").attr("id",dic[fecha.slice(0,2)]);
};

async function cargar_html_ventas(){
    let container = document.querySelector('.index-medium-container-main');
    container.innerHTML = await eel.pass_html("src/analisis-ventas/analisis-ventas.html")();
    borrar_null_tags();
    let script = document.createElement('script');
    script.src = 'analisis-ventas/analisis-ventas.js';
    script.classList.add('nulo');
    document.body.appendChild(script);
    var link = document.createElement('link');
    link.type = 'text/css';
    link.rel = 'stylesheet';
    link.href = 'analisis-ventas/analisis-ventas.css';
    link.classList.add('nulo');
    document.head.appendChild(link);
};


function crear_analisis_ventas_todo2(data){
    crear_nuevo_analisis_chart2();

    let L_tipos = data[0][0];
    let L_tipos_c = data[0][1];
    let L_circ_mes = data[1][0];
    let L_circ_mes_c = data[1][1];
    let cst_total = data[2];

    crear_grafico_circular(L_tipos_c,L_tipos,"grafico-circular-tipos-analisis");
    crear_grafico_circular(L_circ_mes_c,L_circ_mes,"grafico-circular-lugar-analisis");

    let venta = L_circ_mes_c[0]+L_circ_mes_c[1];
    $("#analisis-venta").html(money_format_format(venta));
    $("#analisis-costo").html(money_format_format(cst_total));
    $("#analisis-utilidad").html(money_format_format(venta-cst_total));
    $("#analisis-ventacasa").html(money_format_format(L_circ_mes_c[0]));
    $("#analisis-ventatienda").html(money_format_format(L_circ_mes_c[1]));

    let cantidad = 0;
    for (cant of L_tipos_c){
        cantidad += cant;
    }
    $("#analisis-cantidad").html(cantidad);

};

function crear_nuevo_analisis_chart2(){
    $("#grafico-circular-tipos-analisis").each(function() {
        this.parentNode.removeChild(this);
    });
    let container = document.querySelector(".graf-tipos");
    let canva = document.createElement('canvas');
    canva.id = "grafico-circular-tipos-analisis";
    container.appendChild(canva);

    $("#grafico-circular-lugar-analisis").each(function() {
        this.parentNode.removeChild(this);
    });
    let container2 = document.querySelector(".graf-lugar");
    let canva2 = document.createElement('canvas');
    canva2.id = "grafico-circular-lugar-analisis";
    container2.appendChild(canva2);
};


function limpiar_analisis_ventas2(){
    $("#analisis-venta").html(money_format_format(0));
    $("#analisis-costo").html(money_format_format(0));
    $("#analisis-utilidad").html(money_format_format(0));
    $("#analisis-ventacasa").html(money_format_format(0));
    $("#analisis-ventatienda").html(money_format_format(0));
    $("#analisis-cantidad").html(0);
};

//--------------------------------------------------------------------------


async function analisis_inventario_desde_inicio(){
    await cargar_html_inventario();
};

async function cargar_html_inventario(){
    let container = document.querySelector('.index-medium-container-main');
    container.innerHTML = await eel.pass_html("src/analisis-inventario/analisis-inventario.html")();
    borrar_null_tags();
    let script = document.createElement('script');
    script.src = 'analisis-inventario/analisis-inventario.js';
    script.classList.add('nulo');
    document.body.appendChild(script);
    var link = document.createElement('link');
    link.type = 'text/css';
    link.rel = 'stylesheet';
    link.href = 'analisis-inventario/analisis-inventario.css';
    link.classList.add('nulo');
    document.head.appendChild(link);
};

