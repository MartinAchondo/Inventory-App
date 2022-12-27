$("document").ready(()=>{
    cargar_inicio();
    ver_estado_base();
});

async function ver_estado_base(){
    let ans = await eel.comparar_bases()();
    alerta_estado(ans);
};


function borrar_null_tags(){
    $(".nulo").each(function() {
        this.parentNode.removeChild(this);
    });
};

document.getElementById('index-item-inicio').addEventListener('click', ()=>{
    cargar_inicio();
});

async function cargar_inicio(){
    let container = document.querySelector('.index-medium-container-main');
    container.innerHTML = await eel.pass_html("src/inicio.html")();
    borrar_null_tags();
    let script = document.createElement('script');
    script.src = 'inicio.js';
    script.classList.add('nulo');
    document.body.appendChild(script);
};


document.getElementById('index-item-ingresar-prenda-nueva').addEventListener('click', async ()=>{
    let container = document.querySelector('.index-medium-container-main');
    container.innerHTML = await eel.pass_html("src/ingresar-prenda/ingresar-prenda-nueva.html")();
    borrar_null_tags();
    let script = document.createElement('script');
    script.src = 'ingresar-prenda/ingresar-prenda2.js';
    script.classList.add('nulo');
    document.body.appendChild(script);
    var link = document.createElement('link');
    link.type = 'text/css';
    link.rel = 'stylesheet';
    link.href = 'ingresar-prenda/ingresar-prenda.css';
    link.classList.add('nulo');
    document.head.appendChild(link);
});

document.getElementById('index-item-ingresar-prenda-existente').addEventListener('click', async ()=>{
    let container = document.querySelector('.index-medium-container-main');
    container.innerHTML = await eel.pass_html("src/ingresar-prenda/ingresar-prenda-existente.html")();
    borrar_null_tags();
    let script = document.createElement('script');
    script.src = 'ingresar-prenda/ingresar-prenda3.js';
    script.classList.add('nulo');
    document.body.appendChild(script);
    var link = document.createElement('link');
    link.type = 'text/css';
    link.rel = 'stylesheet';
    link.href = 'ingresar-prenda/ingresar-prenda.css';
    link.classList.add('nulo');
    document.head.appendChild(link);
});

document.getElementById('index-item-inventario').addEventListener('click', async ()=>{
    let container = document.querySelector('.index-medium-container-main');
    container.innerHTML = await eel.pass_html("src/inventario/inventario.html")();
    borrar_null_tags();
    let script = document.createElement('script');
    script.src = 'inventario/inventario.js';
    script.classList.add('nulo');
    document.body.appendChild(script);
    var link = document.createElement('link');
    link.type = 'text/css';
    link.rel = 'stylesheet';
    link.href = 'inventario/inventario.css';
    link.classList.add('nulo');
    document.head.appendChild(link);
});

document.getElementById('index-item-editar').addEventListener('click', async ()=>{
    let container = document.querySelector('.index-medium-container-main');
    container.innerHTML = await eel.pass_html("src/editar-inventario/editar.html")();
    borrar_null_tags();
    let script = document.createElement('script');
    script.src = 'editar-inventario/editar.js';
    script.classList.add('nulo');
    document.body.appendChild(script);
});

document.getElementById('index-item-ingresar-venta').addEventListener('click', async ()=>{
    let container = document.querySelector('.index-medium-container-main');
    container.innerHTML = await eel.pass_html("src/ingresar-venta/ingresar-venta.html")();
    borrar_null_tags();
    let script = document.createElement('script');
    script.src = 'ingresar-venta/ingresar-venta.js';
    script.classList.add('nulo');
    document.body.appendChild(script);
    //var link = document.createElement('link');
    //link.type = 'text/css';
    //link.rel = 'stylesheet';
    //link.href = 'ingresar-venta/ingresar-venta.css';
    //document.head.appendChild(link);
});

document.getElementById('index-item-enviar-tienda').addEventListener('click', async ()=>{
    let container = document.querySelector('.index-medium-container-main');
    container.innerHTML = await eel.pass_html("src/enviar-tienda/enviar-tienda.html")();
    borrar_null_tags();
    let script = document.createElement('script');
    script.src = 'enviar-tienda/enviar-tienda.js';
    script.classList.add('nulo');
    document.body.appendChild(script);
    var link = document.createElement('link');
    link.type = 'text/css';
    link.rel = 'stylesheet';
    link.href = 'enviar-tienda/enviar-tienda.css';
    link.classList.add('nulo');
    document.head.appendChild(link);
});

document.getElementById('index-item-enviar-casa').addEventListener('click', async ()=>{
    let container = document.querySelector('.index-medium-container-main');
    container.innerHTML = await eel.pass_html("src/enviar-casa/enviar-casa.html")();
    borrar_null_tags();
    let script = document.createElement('script');
    script.src = 'enviar-casa/enviar-casa.js';
    script.classList.add('nulo');
    document.body.appendChild(script);
    //var link = document.createElement('link');
    //link.type = 'text/css';
    //link.rel = 'stylesheet';
    //link.href = 'enviar-casa/enviar-casa.css';
    //document.head.appendChild(link);
});

document.getElementById('index-item-historial').addEventListener('click', async ()=>{
    let container = document.querySelector('.index-medium-container-main');
    container.innerHTML = await eel.pass_html("src/historial/historial.html")();
    borrar_null_tags();
    let script = document.createElement('script');
    script.src = 'historial/historial.js';
    script.classList.add('nulo');
    document.body.appendChild(script);
    var link = document.createElement('link');
    link.type = 'text/css';
    link.rel = 'stylesheet';
    link.href = 'historial/historial.css';
    link.classList.add('nulo');
    document.head.appendChild(link);
});

document.getElementById('index-item-devolucion').addEventListener('click', async ()=>{
    let container = document.querySelector('.index-medium-container-main');
    container.innerHTML = await eel.pass_html("src/editar-venta/devolucion.html")();
    borrar_null_tags();
    let script = document.createElement('script');
    script.src = 'editar-venta/devolucion.js';
    script.classList.add('nulo');
    document.body.appendChild(script);
    //var link = document.createElement('link');
    //link.type = 'text/css';
    //link.rel = 'stylesheet';
    //link.href = 'devolucion/devolucion.css';
    //document.head.appendChild(link);
});

document.getElementById('index-item-anular').addEventListener('click', async ()=>{
    let container = document.querySelector('.index-medium-container-main');
    container.innerHTML = await eel.pass_html("src/editar-venta/anular.html")();
    borrar_null_tags();
    let script = document.createElement('script');
    script.src = 'editar-venta/anular.js';
    script.classList.add('nulo');
    document.body.appendChild(script);
    //var link = document.createElement('link');
    //link.type = 'text/css';
    //link.rel = 'stylesheet';
    //link.href = 'devolucion/devolucion.css';
    //document.head.appendChild(link);
});

document.getElementById('index-item-ventas').addEventListener('click', async ()=>{
    let container = document.querySelector('.index-medium-container-main');
    container.innerHTML = await eel.pass_html("src/ventas/ventas.html")();
    borrar_null_tags();
    let script = document.createElement('script');
    script.src = 'ventas/ventas.js';
    script.classList.add('nulo');
    document.body.appendChild(script);
    var link = document.createElement('link');
    link.type = 'text/css';
    link.rel = 'stylesheet';
    link.href = 'ventas/ventas.css';
    link.classList.add('nulo');
    document.head.appendChild(link);
});


document.getElementById('index-item-cargar-base').addEventListener('click', async ()=>{
    let container = document.querySelector('.index-medium-container-main');
    container.innerHTML = await eel.pass_html("src/cargar-base/cargar-base.html")();
    borrar_null_tags();
    let script = document.createElement('script');
    script.src = 'cargar-base/cargar-base.js';
    script.classList.add('nulo');
    document.body.appendChild(script);
    //var link = document.createElement('link');
    //link.type = 'text/css';
    //link.rel = 'stylesheet';
    //link.href = 'cargar-base/cargar-base.css';
    //document.head.appendChild(link);
});

document.getElementById('index-item-cargar-foto').addEventListener('click', async ()=>{
    let container = document.querySelector('.index-medium-container-main');
    container.innerHTML = await eel.pass_html("src/cargar-foto/cargar-foto.html")();
    borrar_null_tags();
    let script = document.createElement('script');
    script.src = 'cargar-foto/cargar-foto.js';
    script.classList.add('nulo');
    document.body.appendChild(script);
    //var link = document.createElement('link');
    //link.type = 'text/css';
    //link.rel = 'stylesheet';
    //link.href = 'cargar-base/cargar-base.css';
    //document.head.appendChild(link);
});

document.getElementById('index-item-analisis-inventario').addEventListener('click', async ()=>{
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
});

document.getElementById('index-item-analisis-ventas').addEventListener('click', async ()=>{
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
});

document.getElementById('index-item-analisis-codigo').addEventListener('click', async ()=>{
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
});

document.getElementById('index-item-analisis-query').addEventListener('click', async ()=>{
    let container = document.querySelector('.index-medium-container-main');
    container.innerHTML = await eel.pass_html("src/analisis-query/analisis-query.html")();
    borrar_null_tags();
    let script = document.createElement('script');
    script.src = 'analisis-query/analisis-query.js';
    script.classList.add('nulo');
    document.body.appendChild(script);
    var link = document.createElement('link');
    link.type = 'text/css';
    link.rel = 'stylesheet';
    link.href = 'analisis-query/analisis-query.css';
    link.classList.add('nulo');
    document.head.appendChild(link);
});

