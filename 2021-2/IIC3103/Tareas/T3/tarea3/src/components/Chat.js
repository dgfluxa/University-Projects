import { socket } from './Socket';
import React from 'react';
import { useState, useEffect } from 'react';
import { Button, Typography, Divider, TextField } from '@material-ui/core';
import '../style/Chat.css';

function Chat() {

    const [messages, setMessages] = useState([]);
    const [newMsg, setNewMsg] = useState("");
    const [username, setUsername] = useState("Anónimo")
    const [newUsername, setNewUsername] = useState("")

    useEffect(() => {
        const addMsg = (msg) => {
            setMessages([...messages, msg]);
        };
        socket.on("CHAT", addMsg);
        return () => socket.off("CHAT", addMsg);
    });

    function renderRows(data) {
        var index = 0;
        return data.map((message) => {
            index += 1;
            return (
                <div key={index}>
                    <div className="message">
                        <Typography variant="h6">
                            {message.name}
                        </Typography>
                        <Typography variant="body1">
                            {message.message}
                        </Typography>
                        <Typography variant="caption">
                            {toDate(message.date)}
                        </Typography>
                    </div>
                    <Divider />
                </div>
            );
        });
    }

    function toDate(number) {
        var myDate = new Date(number);
        var mytime = myDate.toLocaleString();

        return mytime;
    }

    function sendMsg(event) {
        event.preventDefault();
        socket.emit("CHAT", {message: newMsg, name: username});
        setNewMsg("");
    }

    function updateUsername(event) {
        event.preventDefault();
        if (newUsername === ""){
            setUsername("Anónimo");
        } else {
            setUsername(newUsername);
            setNewUsername("");
        }
    }

    return (
        <div style={{padding: 20}} id="Chat">
            <Typography variant="h4">
                Centro de Control
            </Typography>
            <Typography variant="caption" color="secondary">
                {username === "Anónimo" ?  'Estás conectado como Anónimo' : ''}
            </Typography>
            <div style={{width: '70%', margin: 'auto', marginTop: 20, paddingBottom: 10}}>
                <form onSubmit={updateUsername} noValidate autoComplete="off">
                    
                    <Typography style={{marginLeft: 0, marginRight: 5}} variant="caption">
                        Nombre: {username}
                    </Typography>
                    <TextField style={{height: 35, width: '30%', marginRight: 5}} id="outlined-basic" 
                    label="Ingresa un nombre" 
                    variant="outlined" 
                    size="small"
                    inputProps={{ 'aria-label': 'updateName' }}
                    value={newUsername}
                    onChange={(event) => {
                        setNewUsername(event.target.value);
                    }}/>
                    <Button style={{height: 40, width: 'auto', marginRight: 0}} type="submit" aria-label="updateName" variant="contained" color="primary" >Cambiar</Button>
                </form>
            </div>
            <div className="chatbox">
                {renderRows(messages)}
            </div>
            <div style={{paddingTop: 10}}>
                <form onSubmit={sendMsg} noValidate autoComplete="off">
                    <TextField style={{height: 50, width: '60%', marginRight: 5}} id="outlined-basic" 
                    label="Escribe un mensaje..." 
                    variant="outlined" 
                    inputProps={{ 'aria-label': 'send' }}
                    value={newMsg}
                    onChange={(event) => {
                        setNewMsg(event.target.value);
                    }}/>
                    <Button style={{height: 55, width: '10%'}} type="submit" aria-label="send" variant="contained" color="primary" >Enviar</Button>
                </form>
            </div>
        </div>
    );
}

export default Chat;