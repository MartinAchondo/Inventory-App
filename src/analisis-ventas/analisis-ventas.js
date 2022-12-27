$("document").ready(function(){

    let L_ano = ["2021","2022","2023"];
    const contenedor_ano = document.querySelector("#ingresar-ano");
    let f_ano = document.createDocumentFragment();
    for (ano of L_ano){
        const item = document.createElement('option');
        item.append(new Option(ano, ano));
        f_ano.appendChild(item);
    };
    contenedor_ano.appendChild(f_ano);

    let L_mes = ['Enero','Febrero','Marzo',"Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"];
    const contenedor_mes = document.querySelector("#ingresar-mes");
    let f_mes = document.createDocumentFragment();
    for (mes of L_mes){
        const item = document.createElement('option');
        item.append(new Option(mes, mes));
        f_mes.appendChild(item);
    };
    contenedor_mes.appendChild(f_mes);

    if ($(".ano")[0]){
        $("#ingresar-ano").val($(".check-analisis-ano").attr("id"));
        $("#ingresar-mes").val($(".check-analisis-mes").attr("id"));
    };
        
    $("#form-analisis-ventas").submit(async (e)=>{
        e.preventDefault();
        let dic = {
            "Enero": "01",
            "Febrero": "02",
            "Marzo": "03",
            "Abril": "04",
            "Mayo": "05",
            "Junio": "06",
            "Julio": "07",
            "Agosto": "08",
            "Septiembre": "09",
            "Octubre": "10",
            "Noviembre": "11",
            "Diciembre": "12"
        };
        let ano = $('#ingresar-ano').val();
        let mes = $('#ingresar-mes').val();
        let fecha = "";
        if (mes != ""){
            fecha = ano + "/" + dic[mes];
        }else{
            fecha = ano;
        };
        let ans = await eel.pedir_tipos_analisis_ventas(fecha)();
        if (ans.length != 0){
            crear_analisis_ventas_todo(ans);
        }else{
            crear_nuevo_analisis_chart();
            limpiar_analisis_ventas();
        };

    });

});

function crear_analisis_ventas_todo(data){
    crear_nuevo_analisis_chart();

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

function crear_nuevo_analisis_chart(){
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

$("#crear-pdf").click(async ()=>{
    let ano = $('#ingresar-ano').val();
    if (ano != ""){
        let mes = $('#ingresar-mes').val();
        let fecha = "";
        let dic = {
            "Enero": "01",
            "Febrero": "02",
            "Marzo": "03",
            "Abril": "04",
            "Mayo": "05",
            "Junio": "06",
            "Julio": "07",
            "Agosto": "08",
            "Septiembre": "09",
            "Octubre": "10",
            "Noviembre": "11",
            "Diciembre": "12"
        };
        if (mes != ""){
            fecha = ano + "/" + dic[mes];
        }else{
            fecha = ano;
        };
        let ans = await eel.create_pdf_ventas(fecha)();
    };
});


function limpiar_analisis_ventas(){
    $("#analisis-venta").html(money_format_format(0));
    $("#analisis-costo").html(money_format_format(0));
    $("#analisis-utilidad").html(money_format_format(0));
    $("#analisis-ventacasa").html(money_format_format(0));
    $("#analisis-ventatienda").html(money_format_format(0));
    $("#analisis-cantidad").html(0);
};

