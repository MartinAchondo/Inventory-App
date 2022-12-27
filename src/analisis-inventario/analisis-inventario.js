$("document").ready(()=>{
    cargar_inv_todo();
});

async function cargar_inv_todo(){
    let data = await eel.pedir_cantidades_inicio()();
    let total_casa = data[0];
    let total_tienda = data[1];
    let total = total_casa + total_tienda;

    let data4 = await eel.pedir_utilidades_costos_inicio()();
    let cst_inv = data4[1];
    let ut_inv = data4[3];
    let vent_inv = cst_inv + ut_inv;

    $("#analisis-venta-inv").html(money_format_format(vent_inv));
    $("#analisis-costo-inv").html(money_format_format(cst_inv));
    $("#analisis-utilidad-inv").html(money_format_format(ut_inv));
    $("#analisis-cantidad-inv").html(total);
    $("#analisis-cantidadcasa-inv").html(total_casa);
    $("#analisis-cantidadtienda-inv").html(total_tienda);

    cargar_grafico_inv("todo");

    async function cargar_grafico_inv(data){
        let data2 = await eel.pedir_tipos_analisis_total(data)();
        let L_tipos = data2[0];
        let L_cantidad = data2[1];
        let chart_inv = crear_grafico_circular(L_cantidad,L_tipos,'grafico-analisis-inv');
    };
    
    $("#analisis-todo-inv-btn").click(()=>{
        crear_nuevo_analisis_chart();
        cargar_grafico_inv("todo");
    });
    
    $("#analisis-casa-inv-btn").click(()=>{
        crear_nuevo_analisis_chart();
        cargar_grafico_inv("casa");
    });
    
    $("#analisis-tienda-inv-btn").click(()=>{
        crear_nuevo_analisis_chart();
        cargar_grafico_inv("tienda");
    });

    function crear_nuevo_analisis_chart(){
        $(".grafico-analisis-inv").each(function() {
            this.parentNode.removeChild(this);
        });
        let container = document.querySelector(".grafico-inv");
        let canva = document.createElement('canvas');
        canva.classList.add("grafico-analisis-inv");
        canva.id = "grafico-analisis-inv";
        container.appendChild(canva);
    };
};

