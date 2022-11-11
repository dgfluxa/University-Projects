import React from "react";
import Table from "@material-ui/core/Table";
import TableBody from "@material-ui/core/TableBody";
import TableCell from "@material-ui/core/TableCell";
import TableHead from "@material-ui/core/TableHead";
import TableRow from "@material-ui/core/TableRow";
import Paper from "@material-ui/core/Paper";
import { Typography } from '@material-ui/core';
import { Button } from '@material-ui/core';
import { useHistory } from 'react-router-dom';


export default function GroupOCTable({ data }) {

    const history = useHistory();

  return (
    <div style={{display: 'flex', marginTop: '4%', justifyContent: 'center'}}>
        
        {data.length > 0 ? 
            <Paper style={{width: '70%', minWidth: 700}}>
                <Table size="small">
                    <TableHead>
                    <TableRow>
                        <TableCell>ID OC</TableCell>
                        <TableCell>SKU</TableCell>
                        <TableCell>Cantidad</TableCell>
                        <TableCell>Estado</TableCell>
                        <TableCell></TableCell>
                    </TableRow>
                    </TableHead>
                    <TableBody>
                        {data.map((row) => {
                            if (row.estado.toLowerCase()==='aceptada'){
                                var color = 'green';
                            } else if (row.estado.toLowerCase()==='recibida'){
                                var color = 'orange';
                            } else if (row.estado.toLowerCase()==='rechazada'){
                                var color = 'red';
                            } else {
                                var color = 'black';
                            }
                            return (
                            <TableRow key={row.oc_id}>
                                <TableCell>{row.oc_id}</TableCell>
                                <TableCell>{row.sku}</TableCell>
                                <TableCell>{row.cantidad}</TableCell>
                                <TableCell style={{color: color}}>{row.estado}</TableCell>
                                <TableCell> <Button style={{height: 25}} variant="contained" color="secondary" onClick={() => history.push('group_ocs/'+row.oc_id)}> Detalles </Button></TableCell>
                            </TableRow>
                        )})}
                    </TableBody>
                </Table>
            </Paper>
        :
            <Typography variant="h6" style={{color: "red"}}> No existen ordenes de compra </Typography>
        }
    </div>
  );
}