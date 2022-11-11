import React, { useEffect, useState } from 'react';
import { BrowserRouter as Router, Switch, RouteLink, Link, useParams } from 'react-router-dom';
import { Typography } from '@material-ui/core';
import userService from '../services/users';
import Loader from "react-loader-spinner";
import Avatar from '@material-ui/core/Avatar';
import Table from "@material-ui/core/Table";
import TableBody from "@material-ui/core/TableBody";
import TableCell from "@material-ui/core/TableCell";
import TableHead from "@material-ui/core/TableHead";
import TableRow from "@material-ui/core/TableRow";
import Paper from "@material-ui/core/Paper";

function User() {

  const [user, setUser] = useState(undefined);
  const [cards, setCards] = useState(undefined);
  const [addresses, setAddresses] = useState(undefined);
  let { id } = useParams();

  useEffect(() => {
    userService.getUser(id).then((data) => {
        setUser(data);
    });
    userService.getUserCards(id).then((data) => {
        setCards(data);
    });
    userService.getUserAddresses(id).then((data) => {
        setAddresses(data);
    });
  }, []);
  
    if (user === undefined || cards === undefined || addresses === undefined){
        return (
            <div >
                <div style={{marginTop: '2%'}}>
                <Typography variant="h3" style={{marginBottom: '2%'}}>
                    Cargado Usuario
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
                    <Typography variant="h3">
                        Usuario: {user.name} {user.lastName}
                    </Typography>
                    <div style={{marginLeft: '5%', marginRight: '5%', marginTop: '2%'}}>
                        <div style={{justifyContent: "center", display: "flex"}}>
                            <Avatar  style={{height: '15%', width: '15%'}} src={user.avatar} />
                        </div>
                        <div style={{display: 'flex', marginTop: '2%', justifyContent: 'center'}}>
                            <Paper style={{width: '30%', minWidth: 400}}>
                                <Table >
                                    <TableBody>
                                        <TableRow>
                                            <TableCell>ID:</TableCell>
                                            <TableCell >{user.id}</TableCell>
                                        </TableRow>
                                        <TableRow>
                                            <TableCell>Nombre:</TableCell>
                                            <TableCell >{user.name}</TableCell>
                                        </TableRow>
                                        <TableRow>
                                            <TableCell>Apellido:</TableCell>
                                            <TableCell >{user.lastName}</TableCell>
                                        </TableRow>
                                        <TableRow>
                                            <TableCell>Email:</TableCell>
                                            <TableCell >{user.email}</TableCell>
                                        </TableRow>
                                        <TableRow>
                                            <TableCell>Cumpleaños:</TableCell>
                                            <TableCell >{user.birthdate}</TableCell>
                                        </TableRow>
                                    </TableBody>
                                </Table>
                            </Paper>
                        </div>
                    </div>
                    <div style={{marginLeft: '5%', marginRight: '5%', marginTop: '2%'}}>
                        <Typography variant="h5">
                            Tarjetas de Crédito
                        </Typography>
                        <div style={{display: 'flex', marginTop: '2%', justifyContent: 'center'}}>
							{cards.length === 0 ? 
								<Typography variant="subtitle1">No tiene tarjetas de crédito ingresadas</Typography> 
								:
								<Paper style={{width: '50%', minWidth: 500}}>
									<Table >
										<TableHead>
											<TableRow>
												<TableCell>Id</TableCell>
												<TableCell>Número de Tarjeta</TableCell>
												<TableCell>CVV</TableCell>
											</TableRow>
										</TableHead>
										<TableBody>
											{cards.map((row) => (
												<TableRow>
													<TableCell >{row.id}</TableCell>
													<TableCell >{row.creditCard}</TableCell>
													<TableCell >{row.CVV}</TableCell>
												</TableRow>
											))}
										</TableBody>
									</Table>
								</Paper>
							}
                        </div>
                    </div>
                    <div style={{marginLeft: '5%', marginRight: '5%', marginTop: '2%'}}>
                        <Typography variant="h5">
                            Direcciones
                        </Typography>
                        <div style={{display: 'flex', marginTop: '2%', justifyContent: 'center'}}>
							{addresses.length === 0 ? 
								<Typography variant="subtitle1">No tiene direcciones ingresadas</Typography> 
								:
								<Paper style={{width: '70%', minWidth: 500}}>
									<Table >
										<TableHead>
											<TableRow>
												<TableCell>Id</TableCell>
												<TableCell>Dirección</TableCell>
												<TableCell>Ciudad</TableCell>
												<TableCell>País</TableCell>
												<TableCell>Zip</TableCell>
											</TableRow>
										</TableHead>
										<TableBody>
											{addresses.map((row) => (
												<TableRow>
													<TableCell >{row.id}</TableCell>
													<TableCell >{row.address}</TableCell>
													<TableCell ><Link to={"/cities/" + row.city.id}>{row.city.name}</Link></TableCell>
													<TableCell >{row.city.country}</TableCell>
													<TableCell >{row.zip}</TableCell>
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
export default User;