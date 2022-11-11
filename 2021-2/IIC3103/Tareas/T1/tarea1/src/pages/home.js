import React from 'react';
import { Button, Typography } from '@material-ui/core';
import { useHistory } from 'react-router-dom';

function Home() {

  const history = useHistory();

  const users = () => {
      history.push("/users")
  }

  const cities = () => {
    history.push("/cities")
  }

  return (
    <div>
      <div style={{marginTop: '2%'}}>
        <Typography variant="h3">
          Bienvenido
        </Typography>
        <Typography style={{marginTop: '3%', marginLeft: '10%', marginRight: '10%'}} variant="subtitle1">
          Mediante los botones que se encuentran debajo de este texto o utilizando la barra de navegación 
          podrás ingresar a los listados de usuarios y ciudades. Además, con la barra de búsqueda ubicada en la 
          barra de navegación superior podrás buscar usuarios y ciudades al ingresar un texto y presionando enter o el
          icono de lupa.
        </Typography>
        <div >
            <Button style={{margin: '5%', width: 150 }} variant="contained" color="secondary" size='large' onClick={users}>Usuarios</Button>
            <Button style={{margin: '5%', width: 150 }} variant="contained" color="secondary" size='large' onClick={cities}>Ciudades</Button>
        </div>
      </div>
    </div>
  );
}

export default Home;