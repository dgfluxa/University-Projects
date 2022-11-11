import React from 'react';
import Chat from '../components/Chat';
import Trucks from '../components/Trucks';
import Map from '../components/Map';
import 'leaflet/dist/leaflet.css'

function Home() {

  return (
    <div>
      <div style={{marginTop: '2%'}}>
        <Map />
        <Trucks />
        <Chat />
      </div>
    </div>
  );
}

export default Home;