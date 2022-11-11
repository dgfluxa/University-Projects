import { socket } from './Socket';
import React from 'react';
import { useState, useEffect } from 'react';
import { Typography, Button } from '@material-ui/core';
import '../style/Trucks.css';

function Trucks() {

    const [trucks, setTrucks] = useState({});
    const [loaded, setLoaded] = useState(false);

    socket.emit("TRUCKS");
    socket.on("TRUCKS", (data) => {
        var trucks_data = {}
        data.map((truck)=>{
            trucks_data[truck.code] = truck;
            trucks_data[truck.code].failure = false;
            return null;
        });
        setTrucks(trucks_data);
        setLoaded(true);
        return 
    });

    if (loaded){
        socket.off("TRUCKS");
    }
    
    useEffect(() => {
        const addFailure = (fail) => {
            
            if (loaded) {
                if (!trucks[fail.code].failure){   
                    let trucks_data = {...trucks};
                    trucks_data[fail.code].failure = "Falla en " + fail.source;
                    setTrucks(trucks_data);
                }
            }
        };
        socket.on("FAILURE", addFailure);
        return () => socket.off("FAILURE", addFailure);
    });

    useEffect(() => {
        const addFix = (fix) => {
            var trucks_data = {...trucks};
            trucks_data[fix.code].failure = false;
            setTrucks(trucks_data);
        };
        socket.on("FIX", addFix);
        return () => socket.off("FIX", addFix);
    });


    function renderTrucks(data) {
        var index = 0;
        return Object.keys(data).map((code) => {
            index += 1;
            return (
                <div key={index}>
                    <div id={!data[code].failure ? 'good' : 'bad'} className="truck">
                        <Typography variant="h5">
                            Camión {code}
                        </Typography>
                        <Typography variant="subtitle1">
                            Modelo: {data[code].truck}
                        </Typography>
                        <Typography variant="subtitle1">
                            Estado: {data[code].failure ? data[code].failure : "Ok"}
                        </Typography>
                        <Typography variant="body2">
                            Origen: {data[code].origin[0]}, {data[code].origin[1]}
                        </Typography>
                        <Typography variant="body2">
                            Destino: {data[code].destination[0]}, {data[code].destination[1]}
                        </Typography>
                        <Typography variant="body2">
                            Motor: {data[code].engine}
                        </Typography>
                        <Typography variant="body2">
                            Capacidad: {data[code].capacity}
                        </Typography>
                        <Typography variant="body2">
                            Staff: 
                        </Typography>
                            {
                                (data[code].staff.map((employee) => {
                                return <Typography key={employee.name} variant="body2"> {employee.name} ({employee.age})</Typography> 
                                }))
                            }
                        {data[code].failure ?
                        <Button style={{margin: 5}} variant="contained" onClick={(event) => {
                            socket.emit("FIX", {code: code});
                        }}>
                            Arreglar
                        </Button>
                        :
                        ""
                        }
                        
                    </div>
                </div>
            );
        });
    }

    return (
        <div style={{padding: 20}} id="Trucks">
            <Typography variant="h4">
                Información Camiones
            </Typography>
            <div className="trucks-container" >
                {renderTrucks(trucks)}
            </div>
            
        </div>
    );
}

export default Trucks;