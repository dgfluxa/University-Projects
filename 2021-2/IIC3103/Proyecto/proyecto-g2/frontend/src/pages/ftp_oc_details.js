import React, { useEffect, useState } from 'react';
import { BrowserRouter as Router, Switch, RouteLink, Link, useParams } from 'react-router-dom';
import { Typography } from '@material-ui/core';
import Loader from "react-loader-spinner";
import Table from "@material-ui/core/Table";
import TableBody from "@material-ui/core/TableBody";
import TableCell from "@material-ui/core/TableCell";
import TableRow from "@material-ui/core/TableRow";
import Paper from "@material-ui/core/Paper";
import OCsService from '../services/ocs';

function FTPOC() {

	let { id } = useParams();
	const [oc, setOC] = useState([])
	const [loaded, setLoaded] = useState(false)

	useEffect(() => {
		OCsService.getOC(id).then((data) => {
			setOC(data);
			setLoaded(true);
            
		});
	}, []);
  
    if (!loaded){
        return (
            <div >
                <div style={{marginTop: '2%'}}>
                <Typography variant="h3" style={{marginBottom: '2%'}}>
                    Cargado Orden de Compra FTP
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
        const date = new Date(oc.fechaEntrega);
        return (
            <div >
                <div style={{marginTop: '2%', marginBottom: '5%'}}>
                    <Typography variant="h3">
                        Orden de Compra: {oc._id}
                    </Typography>
                    <div style={{marginLeft: '5%', marginRight: '5%', marginTop: '2%'}}>
                        <div style={{display: 'flex', marginTop: '2%', justifyContent: 'center'}}>
                            <Paper style={{width: 'auto', minWidth: 400}}>
                                <Table size='small'>
                                    <TableBody>
                                        <TableRow>
                                            <TableCell>ID:</TableCell>
                                            <TableCell >{oc._id}</TableCell>
                                        </TableRow>
                                        <TableRow>
                                            <TableCell>Cliente:</TableCell>
                                            <TableCell >{oc.cliente}</TableCell>
                                        </TableRow>
                                        <TableRow>
                                            <TableCell>Proveedor:</TableCell>
                                            <TableCell >{oc.proveedor}</TableCell>
                                        </TableRow>
                                        <TableRow>
                                            <TableCell>SKU:</TableCell>
                                            <TableCell >{oc.sku}</TableCell>
                                        </TableRow>
                                        <TableRow>
                                            <TableCell>Fecha de Entrega:</TableCell>
                                            <TableCell >{date.toLocaleString()}</TableCell>
                                        </TableRow>
                                        <TableRow>
                                            <TableCell>Cantidad:</TableCell>
                                            <TableCell >{oc.cantidad}</TableCell>
                                        </TableRow>
                                        <TableRow>
                                            <TableCell>Cantidad Despachada:</TableCell>
                                            <TableCell >{oc.cantidadDespachada}</TableCell>
                                        </TableRow>
                                        <TableRow>
                                            <TableCell>Precio Unitario:</TableCell>
                                            <TableCell >{oc.precioUnitario}</TableCell>
                                        </TableRow>
                                        <TableRow>
                                            <TableCell>Canal:</TableCell>
                                            <TableCell >{oc.canal}</TableCell>
                                        </TableRow>
                                        <TableRow>
                                            <TableCell>Estado:</TableCell>
                                            <TableCell >{oc.estado}</TableCell>
                                        </TableRow>
                                        <TableRow>
                                            <TableCell>Notas:</TableCell>
                                            <TableCell >{oc.notas? oc.notas : '---'}</TableCell>
                                        </TableRow>
										{oc.estado.toLowerCase() === 'rechazada'? 
										<TableRow>
											<TableCell>Motivo Rechazo:</TableCell>
											<TableCell >{oc.rechazo? oc.rechazo : '---'}</TableCell>
										</TableRow>
                                        :
                                        null
										}
                                        {oc.estado.toLowerCase() === 'anulada'? 
										<TableRow>
											<TableCell>Motivo Anulación:</TableCell>
											<TableCell >{oc.anulacion? oc.anulacion : '---'}</TableCell>
										</TableRow>
                                        :
                                        null
										}
                                        <TableRow>
                                            <TableCell>URL Notificación:</TableCell>
                                            <TableCell >{oc.urlNotificacion? oc.urlNotificacion : '---'}</TableCell>
                                        </TableRow>
                                    </TableBody>
                                </Table>
                            </Paper>
                        </div>
                    </div>
                </div>
            </div>
        );
	}
}
export default FTPOC;