import React, { useEffect, useState } from 'react';
import { Typography } from '@material-ui/core';
import GeneralTable from '../components/general_table';
import SpecificTable from '../components/specific_table';
import stocksService from '../services/stocks';
import Loader from "react-loader-spinner";


function Home() {

  const [stocks, setStocks] = useState([]);
  const [generalStocks, setGeneralStocks] = useState([]);
  const [loaded1, setLoaded1] = useState(false);
  const [loaded2, setLoaded2] = useState(false);

  useEffect(() => {
    stocksService.getStocks().then((data) => {
      setStocks(data);
      setLoaded1(true);
    });

    stocksService.getGeneralStocks().then((data) => {
      setGeneralStocks(data);
      setLoaded2(true);
    });

  }, []);

  return (
    <div>
      <div style={{marginTop: '2%', marginBottom: "2%"}}>
        { loaded2 ? 
          <GeneralTable data={generalStocks} />
        :
          <div>
            <Typography variant="h3" style={{marginBottom: "2%"}}>
              Almacenes Totales
            </Typography>
            <Loader
              type="TailSpin"
              color="#3f50b5"
              height={100}
              width={100}
            />
            <Typography variant="h6">
              Cargando... 
            </Typography>
          </div>
        }
        <Typography variant="h3" style={{marginTop: "5%", marginBottom: "2%"}}>
            Almacenes Específicos:
        </Typography>
        { loaded1 ? 
          stocks.map((almacen) => (<SpecificTable data={almacen} key={almacen._id}/>)) 
          
          
        :
          <div>
            <Loader
              type="TailSpin"
              color="#3f50b5"
              height={100}
              width={100}
            />
            <Typography variant="h6">
              Cargando... 
            </Typography>
          </div>
        }
      </div>
    </div>
  );
}

export default Home;