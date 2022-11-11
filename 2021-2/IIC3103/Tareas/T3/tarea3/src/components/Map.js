import { socket } from './Socket';
import React from 'react';
import { useState, useEffect } from 'react';
import { Typography } from '@material-ui/core';
import { MapContainer, TileLayer, Marker, Polyline, Tooltip } from 'react-leaflet';
import 'leaflet/dist/leaflet.css';
import truckIcon from '../assets/truckIcon.png';
import L from 'leaflet';
import Loader from "react-loader-spinner";

const icon = new L.Icon({
    iconUrl: truckIcon,
    iconSize: new L.Point(40, 50),
});

function Map() {

    const [trucks, setTrucks] = useState({});
    const [loaded, setLoaded] = useState(false);
    const [position, setPosition] = useState(false);
    

    socket.emit("TRUCKS");
    socket.on("TRUCKS", (data) => {
        var trucks_data = {}
        data.map((truck)=>{
            trucks_data[truck.code] = truck;
            trucks_data[truck.code].failure = false;
            trucks_data[truck.code].start_pos = "";
            trucks_data[truck.code].pos = truck.origin;
            if (!position) {
                setPosition(truck.origin);
            }
            return null;
        });
        setTrucks(trucks_data);
        setLoaded(true);
        return
    });

    useEffect(() => {
        const updatePosition = (pos) => {
            if (loaded) {
                let trucks_data = {...trucks};
                if (trucks_data[pos.code].start_pos === ""){        
                    trucks_data[pos.code].start_pos = pos.position;   
                }
                trucks_data[pos.code].pos = pos.position;
                setTrucks(trucks_data);
                return
            }
        };
        socket.on("POSITION", updatePosition);
        return () => socket.off("POSITION", updatePosition);
    });

    function renderTrucks(data) {
        var index = 0;
        return Object.keys(data).map((code) => {
            index += 1;
            return (
                <Marker key={index} position={data[code].pos} icon={icon} >
                    <Tooltip>
                        Camión {code} <br /> {data[code].pos[0]}, {data[code].pos[1]}
                    </Tooltip>
                </Marker>
            );
        });
    };

    function renderLines(data) {
        var index = 0;
        return Object.keys(data).map((code) => {
            index += 1;
            return (
                <Polyline key={index} pathOptions={{color: 'red'}} positions={[data[code].origin, data[code].destination]}>
                    <Tooltip>
                        Camino Camión {code} <br /> Origen: {data[code].origin[0]}, {data[code].origin[1]} <br /> Destino: {data[code].destination[0]}, {data[code].destination[1]}
                    </Tooltip>
                </Polyline>
            );
        });
        
    };

    function renderPathLines(data) {
        var index = 0;
        return Object.keys(data).map((code) => {
            index += 1;
            if (data[code].start_pos !== ""){
                return (
                    <Polyline key={index} pathOptions={{color: 'green'}} positions={[data[code].start_pos, data[code].pos]} >
                        <Tooltip>
                            Camino Recorrido Camión {code} <br /> Posición Inicial: {data[code].start_pos[0]}, {data[code].start_pos[1]} <br /> Posición Actual: {data[code].pos[0]}, {data[code].pos[1]}
                        </Tooltip>
                    </Polyline>
                );
            } else {
                return null;
            }
        });
        
    };

    if (loaded){
        socket.off("TRUCKS");
    }

    return (
        <div style={{padding: 20}} id="Map">
            <Typography variant="h4">
                Mapa en vivo flota de camiones
            </Typography>
            <div style={{padding: "10px"}}>
                { position ? 
                    <MapContainer style={{ width: "80%", height: "400px", margin: "auto"}} center={position} zoom={10} scrollWheelZoom={true}>
                        <TileLayer
                            attribution='&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
                            url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
                        />
                        {renderTrucks(trucks)}
                        {renderLines(trucks)}
                        {renderPathLines(trucks)}
                    </MapContainer>
                    : 
                    <Loader
                        type="TailSpin"
                        color="#3f50b5"
                        height={100}
                        width={100}
                    />
                }
            </div>
        </div>
    );
}

export default Map;