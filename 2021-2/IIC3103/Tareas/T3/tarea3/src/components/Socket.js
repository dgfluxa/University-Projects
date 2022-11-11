import { io } from "socket.io-client";

export const socket = io("wss://tarea-3-websocket.2021-2.tallerdeintegracion.cl", {
    path: "/trucks/"
  });

/*socket.on("connect", () => {
    console.log(socket.id); // x8WIv7-mJelg7on_ALbx
});*/
