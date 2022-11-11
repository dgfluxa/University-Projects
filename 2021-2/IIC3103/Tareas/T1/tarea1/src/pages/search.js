import React, { useEffect, useState } from 'react';
import { BrowserRouter as Router, Switch, RouteLink, Link, useParams } from 'react-router-dom';
import { Typography } from '@material-ui/core';
import userService from '../services/users';
import cityService from '../services/cities';
import Loader from "react-loader-spinner";
import UserTable from '../components/userTable'
import CityTable from '../components/cityTable'

function Search() {

  const [cities, setCities] = useState(undefined);
  const [users, setUsers] = useState(undefined);
  let { text } = useParams();

  useEffect(() => {
        cityService.searchCities(text).then((data) => {
            setCities(data)
        });

        userService.searchUsers(text).then((data) => {
            setUsers(data)
        });
  }, []);
  
    if (cities === undefined || users === undefined) {
        return (
            <div >
                <div style={{marginTop: '2%'}}>
                <Typography variant="h3" style={{marginBottom: '2%'}}>
                    Resultados Búsqueda "{text}"
                </Typography>
                <Loader
                    type="TailSpin"
                    color="#3f50b5"
                    height={100}
                    width={100}
                />
                <Typography style={{marginTop: '3%', marginLeft: '10%', marginRight: '10%'}} variant="subtitle1">
                    Cargando
                </Typography>
                </div>
            </div>
        );
    } else {
        return (
            <div >
                <div style={{marginTop: '2%', marginBottom: '5%'}}>
                    <Typography variant="h3" style={{marginBottom: '2%'}}>
                        Resultados Búsqueda "{text}"
                    </Typography>
                    <div style={{marginLeft: '5%', marginRight: '5%', marginTop: '2%'}}>
                        <Typography variant="h5">
                            Usuarios
                        </Typography>
                        <div style={{display: 'flex', marginTop: '2%', justifyContent: 'center'}}>
							{users.length === 0 ? 
								<Typography variant="subtitle1">No se encontraron usuarios para la búsqueda "{text}"</Typography> 
								:
								<UserTable rows={users} /> 
							}
                        </div>
                    </div>
                    <div style={{marginLeft: '5%', marginRight: '5%', marginTop: '3%'}}>
                        <Typography variant="h5">
                            Ciudades
                        </Typography>
                        <div style={{display: 'flex', marginTop: '2%', justifyContent: 'center'}}>
							{cities.length === 0 ? 
								<Typography variant="subtitle1">No se encontraron ciudades para la búsqueda "{text}"</Typography> 
								:
								<CityTable rows={cities} /> 
							}
                        </div>
                    </div>
                </div>
            </div>
        );
    } 
}
export default Search;