import React from "react";
import Table from "@material-ui/core/Table";
import TableBody from "@material-ui/core/TableBody";
import TableCell from "@material-ui/core/TableCell";
import TableHead from "@material-ui/core/TableHead";
import TableRow from "@material-ui/core/TableRow";
import Paper from "@material-ui/core/Paper";
import { Typography } from '@material-ui/core';


export default function SpecificTable({ data }) {


  return (
    <div style={{width: '80%', margin: 'auto', marginTop: '2%'}}>
        <Typography variant="h4"> Almacen {data.almacen_name} </Typography>
        
        <Typography variant="h6"> Espacio Utilizado: </Typography>
        {
        data.usedSpace/data.totalSpace >= 0.5 ? 
            (data.usedSpace/data.totalSpace === 1 ? 
                <Typography variant="h6" style={{color: "red"}}> ({data.usedSpace}/{data.totalSpace}) </Typography>
            : 
                <Typography variant="h6" style={{color: "orange"}}> ({data.usedSpace}/{data.totalSpace}) </Typography>
            )
        : 
            <Typography variant="h6" style={{color: "green"}}> ({data.usedSpace}/{data.totalSpace}) </Typography>
        }
        
        {data.stock.length > 0 ? 
            <Paper style={{minWidth: 700}}>
                <Table size="small">
                    <TableHead>
                    <TableRow>
                        <TableCell>SKU</TableCell>
                        <TableCell>Nombre</TableCell>
                        <TableCell>Stock</TableCell>
                    </TableRow>
                    </TableHead>
                    <TableBody>
                        {data.stock.map((row) => (
                            <TableRow key={row._id}>
                                <TableCell>{row._id}</TableCell>
                                <TableCell>{row.name}</TableCell>
                                <TableCell>{row.total}</TableCell>
                            </TableRow>
                        ))}
                    </TableBody>
                </Table>
            </Paper>
        :
            <Typography variant="h6" style={{color: "red"}}> Este almacén no posee inventario </Typography>
        }
    </div>
  );
}