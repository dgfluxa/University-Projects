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

function GroupOC() {

	let { id } = useParams();
	const [oc, setOC] = useState([])
	const [loaded, setLoaded] = useState(false)

	useEffect(() => {
		OCsService.getGroupOC(id).then((data) => {
			setOC(data);
			setLoaded(true);
            console.log(data);
            
		});
	}, []);
  
    if (!loaded){
        return (
            <div >
                <div style={{marginTop: '2%'}}>
                <Typography variant="h3" style={{marginBottom: '2%'}}>
                    Cargado Orden de Compra entre Grupos
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
                                            <TableCell>{oc.id}</TableCell>
                                        </TableRow>
                                        <TableRow>
                                            <TableCell>Cliente:</TableCell>
                                            <TableCell>{oc.cliente}</TableCell>
                                        </TableRow>
                                        <TableRow>
                                            <TableCell>SKU:</TableCell>
                                            <TableCell>{oc.sku}</TableCell>
                                        </TableRow>
                                        <TableRow>
                                            <TableCell>Fecha de Entrega:</TableCell>
                                            <TableCell>{date.toLocaleString()}</TableCell>
                                        </TableRow>
                                        <TableRow>
                                            <TableCell>Cantidad:</TableCell>
                                            <TableCell>{oc.cantidad}</TableCell>
                                        </TableRow>
                                        <TableRow>
                                            <TableCell>Estado:</TableCell>
                                            <TableCell>{oc.estado}</TableCell>
                                        </TableRow>
                                        <TableRow>
                                            <TableCell>URL Notificación:</TableCell>
                                            <TableCell>{oc.urlNotificacion}</TableCell>
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
export default GroupOC;