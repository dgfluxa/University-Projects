import React, { useEffect, useState } from 'react';
import { BrowserRouter as Router, Switch, RouteLink, Link, useParams } from 'react-router-dom';
import { Typography } from '@material-ui/core';
import userService from '../services/users';
import cityService from '../services/cities';
import Loader from "react-loader-spinner";
import Table from "@material-ui/core/Table";
import TableBody from "@material-ui/core/TableBody";
import TableCell from "@material-ui/core/TableCell";
import TableHead from "@material-ui/core/TableHead";
import TableRow from "@material-ui/core/TableRow";
import Paper from "@material-ui/core/Paper";

function City() {

  const [city, setCity] = useState(undefined);
  const [users, setUsers] = useState(undefined);
  let { id } = useParams();

  useEffect(() => {
    cityService.getCity(id).then((data) => {
        setCity(data);
        userService.getSomeUsers(data.users).then((data) => setUsers(data));
    });
  }, []);
  
    if (city === undefined || users === undefined) {
        return (
            <div >
                <div style={{marginTop: '2%'}}>
                <Typography variant="h3" style={{marginBottom: '2%'}}>
                    Cargando Ciudad
                </Typography>
                <Loader
                    type="TailSpin"
                    color="#3f50b5"
                    height={100}
                    width={100}
                />
                </div>
            </div>
        );
    } else {
        return (
            <div >
                <div style={{marginTop: '2%', marginBottom: '5%'}}>
                <Typography variant="h3" style={{marginBottom: '2%'}}>
                    Ciudad: {city.name}
                </Typography>
                    <div style={{marginLeft: '5%', marginRight: '5%', marginTop: '2%'}}>
                        <div style={{display: 'flex', marginTop: '2%', justifyContent: 'center'}}>
                            <Paper style={{width: '30%', minWidth: 400}}>
                                <Table >
                                    <TableBody>
                                        <TableRow>
                                            <TableCell>ID:</TableCell>
                                            <TableCell >{city.id}</TableCell>
                                        </TableRow>
                                        <TableRow>
                                            <TableCell>Nombre:</TableCell>
                                            <TableCell >{city.name}</TableCell>
                                        </TableRow>
                                        <TableRow>
                                            <TableCell>Pais:</TableCell>
                                            <TableCell >{city.country}</TableCell>
                                        </TableRow>
                                    </TableBody>
                                </Table>
                            </Paper>
                        </div>
                    </div>
                    <div style={{marginLeft: '5%', marginRight: '5%', marginTop: '2%'}}>
                        <Typography variant="h5">
                            Usuarios
                        </Typography>
                        <div style={{display: 'flex', marginTop: '2%', justifyContent: 'center'}}>
							{users.length === 0 ? 
								<Typography variant="subtitle1">No hay usuarios con direcciones en esta ciudad</Typography> 
								:
								<Paper style={{width: '70%', minWidth: 500}}>
									<Table >
										<TableHead>
											<TableRow>
												<TableCell>Id</TableCell>
												<TableCell>Nombre</TableCell>
												<TableCell>Apellido</TableCell>
												<TableCell>email</TableCell>
											</TableRow>
										</TableHead>
										<TableBody>
											{users.map((row) => (
												<TableRow>
													<TableCell >{row.id}</TableCell>
													<TableCell ><Link to={"/users/" + row.id}>{row.name}</Link></TableCell>
													<TableCell >{row.lastName}</TableCell>
													<TableCell >{row.email}</TableCell>
												</TableRow>
											))}
										</TableBody>
									</Table>
								</Paper>
							}
                        </div>
                    </div>
                </div>
            </div>
        );
    }
}
export default City;