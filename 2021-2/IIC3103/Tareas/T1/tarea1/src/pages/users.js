import React, { useEffect, useState } from 'react';
import { Typography } from '@material-ui/core';
import userService from '../services/users';
import UserTable from '../components/userTable'
import Loader from "react-loader-spinner";

function Users() {

  const [users, setUsers] = useState(0)

  useEffect(() => {
    userService.getUsers().then((data) => {
      setUsers(data);
    });
  }, []);
  
  if (users === 0){
    return (
      <div >
        <div style={{marginTop: '2%'}}>
          <Typography variant="h3" style={{marginBottom: '2%'}}>
            Usuarios
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
            Usuarios
          </Typography>
          <div style={{marginLeft: '5%', marginRight: '5%', marginTop: '2%'}}>
            <UserTable rows={users} />
          </div>
        </div>
      </div>
    );
  }
}
export default Users;
  