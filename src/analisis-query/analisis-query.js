$("#query-mandar").click(async ()=>{
    let query = $("#query-input").val();
    if (query!=""){
        let ans = await eel.pedir_query_analisis(query)();
        let columns = ans[0];
        let data = ans[1];
        let columnas = [];
        if (data != false){
            for (columna of columns){
                columnas.push({title: columna});
            };
            try{
                $("#query-datatable").DataTable({
                    data: data,
                    columns: columnas,
                    "scrollY": "50vh",
                    "scrollCollapse": true,
                    "pageLength": 100,
                    "order": [[ 0, "asc" ]]
                });
            } catch(error){
                mensaje("Refresca página para hacer otra petición",'aviso');
            };
        }else{
            mensaje('Error en petición','error');
        };
    };
});