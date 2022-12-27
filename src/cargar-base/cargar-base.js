$("document").ready(()=>{

    $("#base-buscar").click(()=>{
        ask_path();
    });    

    $("#base-subir").click(async ()=>{
        mensaje('subiendo','texto');
        let ans = await eel.upload_base_web()();
        mensaje(ans,'texto');
        if (ans){
            alerta_estado('igual');
        };
    });

    $("#base-descargar").click(async ()=>{
        mensaje('descargando','texto');
        let ans = await eel.download_base_web()();
        mensaje(ans,'texto');
        if (ans){
            alerta_estado('igual');
        };
    });

});

