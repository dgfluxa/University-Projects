import React, { useEffect, useState } from 'react';
import { Typography } from '@material-ui/core';
import cityService from '../services/cities';
import CityTable from '../components/cityTable'
import Loader from "react-loader-spinner";

function Cities() {
  const [cities, setCities] = useState(0);

  useEffect(() => {
    cityService.getCities().then((data) => {
      setCities(data);
    });
  }, []);
  
  if (cities === 0){
    return (
      <div >
        <div style={{marginTop: '2%'}}>
          <Typography variant="h3" style={{marginBottom: '2%'}}>
            Ciudades
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
        <div style={{marginTop: '2%'}}>
          <Typography variant="h3">
            Ciudades
          </Typography>
          <div style={{marginLeft: '5%', marginRight: '5%', marginTop: '2%'}}>
            <CityTable rows={cities} />
          </div>
        </div>
      </div>
    );
  }
}
  
export default Cities;