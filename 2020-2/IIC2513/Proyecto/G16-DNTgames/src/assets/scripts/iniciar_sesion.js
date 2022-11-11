
//----------------------------------------


var API_session = document.getElementById("API");

var mensajes = document.getElementById("mensaje");
API_session.addEventListener("click", enviaInfo);


function enviaInfo(){
  var user = document.getElementById("username").value;
  var contrasena = document.getElementById("p1").value;
  var datos = {
    username: user,
    password: contrasena
  };
  enviaValores(datos);
}

const enviaValores = datos =>{
  fetch("https://cors-anywhere.herokuapp.com/https://dntgames.herokuapp.com/session/log_in",
       { method:"POST", body:JSON.stringify(datos), headers:{"Content-type":"application/json"} })
      .then(responde =>{ return responde.json() })
      .then(dataRespuesta=>{
           if(dataRespuesta.error != undefined){
              mensajes.innerText = dataRespuesta.error;
           }
          else{
              mensajes.innerText = dataRespuesta.msg;
              //dejamos en local storage el usuario.
              const user = {
                'username':dataRespuesta.user.username,
                'token': dataRespuesta.user.token,
                'part_g': dataRespuesta.user.part_g,
                'part_p': dataRespuesta.user.part_p,
                'partida': dataRespuesta.user.partida
              }
              localStorage.setItem('user_sesion', JSON.stringify(user));
              $(location).attr('href', "../../../index.html");
          }
      })
}