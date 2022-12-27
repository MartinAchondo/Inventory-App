
function alerta_estado(ans){
  let base = $("#estado-base");
  let base2 = $("#estado-base-log");
  if(ans == 'igual'){
      base.html('Base al Día');
      base2.css('background-color', '#25e30b');
  };
  if(ans=='menor' || ans=='descargar'){
      base.html('DESCARGAR');
      base2.css('background-color', 'red');
  };
  if(ans == 'mayor' || ans=='subir'){
      base.html('SUBIR');
      base2.css('background-color', 'red');
  };
  if(ans==false){
      base.html("Sin conexión");
      base2.css("background-color","yellow")
  }
};

function mensaje(texto,tipo){

  if (texto == true) {
    texto = 'true';
  }else if (texto==false){
    texto = 'false';
  };

  options = {
      type: 'none',
      buttons: ['Ok'],
      defaultId: 0,
      title: 'Mensaje',
      message: texto    
  };
  window.api.send("mensaje_toMain",options);
  // error, info, warning
};

function ask_path(){
  let options = {
      title: "Elegir Base",
      buttonLabel: "Seleccionar",
      filters: [{name: 'Data Base', extensions: ['db']}],
      properties: ['openFile']
    };
    window.api.send("ask_path_toMain",options);
};


window.api.receive("ans_ask_path", async (data) => {
  let ans = data['filePaths'][0];
  ans2 = await eel.copy_path(ans)();
  mensaje(ans,'sos');
});

function ask_path_foto(codigo){
  let titulo = "Elegir Foto Para " + codigo;
  let options = {
      title: titulo,
      buttonLabel: "Seleccionar",
      filters: [{name: 'Images', extensions: ['jpg', 'png', 'gif','jpeg']}],
      properties: ['openFile']
    };
    window.api.send("ask_path_foto_toMain",[options,codigo]);
};

window.api.receive("ans_ask_path_foto", async (data) => {
  let ans = data[0]['filePaths'][0];
  let codigo = data[1];
  ans2 = await eel.copy_path_foto([ans,codigo])();
  mensaje(ans,'sos');
  //mensaje(codigo,'sos');
});


function ask_save(){
  let options = {
    title: "Elegir Carpeta y Guardar",
    buttonLabel: "Guardar",
    filters: [{ name: 'All Files', extensions: ['*'] }],
      properties: ['openDirectory']
    };
    window.api.send("ask_save_toMain",options);
};

window.api.receive("ans_save_path", async (data) => {
  console.log(data);
});

function ask_confirmation(){
  let options = {
    title: 'Mensaje',
    buttons: ["Yes","No","Cancel"],
    message: "Quieres Continuar?"
  };
  window.api.send("ask_confirmation_toMain",options);
};

window.api.receive("ans_confirmation_fromMain", async (data) => {
  console.log(data);
  //response 0,1,2 etc
});



function money_format_format(num){
  var money_format = new Intl.NumberFormat('en-US', {
      style: 'currency',
      currency: 'USD',
      minimumFractionDigits: 0,
    });
    return money_format.format(num);
};


function crear_grafico_barras(L_data,L_labels){
    let chart = new Chart(document.getElementById("bar-chart"), {
        type: 'bar',
        data: {
          labels: L_labels,
          datasets: [
            {
              label: "Ventas",
              backgroundColor: ["#F7BA41"],
              data: L_data
            }
          ]
        },
        options: {
          legend: { display: false },
          title: {
            display: true,
            text: 'Ventas Mensuales'
          },
          scales: {
            xAxes: [{
                maxBarThickness: 8
            }]
          }
        }
    });
    return chart
};

function crear_grafico_circular(L_data,L_labels,idd){
    let chart = new Chart(document.getElementById(idd), {
        type: 'pie',
        data: {
          labels: L_labels,
          datasets: [
            {
              label: "Ventas",
              backgroundColor: ["#FF6384","#27BAC7","#f80dbf","#990dea","#b0b380","#473e81","#ab8ae0","#5bfead","#5acdee","#c7c821","#419a89","#297a23","#91b1f1","#f3192e","#4547bb","#f78264","#691e7b"],
              data: L_data
            }
          ]
        },
        options: {
          legend: { display: false },
          title: {
            display: true,
            text: 'Ventas Mensuales'
          }
        }
    });
    return chart
};


