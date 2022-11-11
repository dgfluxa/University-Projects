import React from "react";
import Table from "@material-ui/core/Table";
import TableBody from "@material-ui/core/TableBody";
import TableCell from "@material-ui/core/TableCell";
import TableHead from "@material-ui/core/TableHead";
import TableRow from "@material-ui/core/TableRow";
import Paper from "@material-ui/core/Paper";
import { Typography } from '@material-ui/core';


export default function GeneralTable({ data }) {


  return (
    <div style={{width: '80%', margin: 'auto', marginTop: '2%'}}>
        <Typography variant="h3"> Almacenes Totales </Typography>

        <Typography variant="h6"> Espacio Utilizado Sin Pulmón: </Typography>
        {
        data.usedSpaceWP/data.spaceWP >= 0.5 ? 
            (data.usedSpaceWP/data.spaceWP === 1 ? 
                <Typography variant="h6" style={{color: "red"}}> ({data.usedSpaceWP}/{data.spaceWP}) </Typography>
            : 
                <Typography variant="h6" style={{color: "orange"}}> ({data.usedSpaceWP}/{data.spaceWP}) </Typography>
            )
        : 
            <Typography variant="h6" style={{color: "green"}}> ({data.usedSpaceWP}/{data.spaceWP}) </Typography>
        }
        
        <Typography variant="h6"> Espacio Utilizado Con Pulmón: </Typography>
        {
        data.totalUsedSpace/data.totalSpace >= 0.5 ? 
            (data.totalUsedSpace/data.totalSpace === 1 ? 
                <Typography variant="h6" style={{color: "red"}}> ({data.totalUsedSpace}/{data.totalSpace}) </Typography>
            : 
                <Typography variant="h6" style={{color: "orange"}}> ({data.totalUsedSpace}/{data.totalSpace}) </Typography>
            )
        : 
            <Typography variant="h6" style={{color: "green"}}> ({data.totalUsedSpace}/{data.totalSpace}) </Typography>
        }
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
            {data.skus.map((row) => (
                <TableRow key={row.sku}>
                <TableCell>{row.sku}</TableCell>
                <TableCell>{row.name}</TableCell>
                <TableCell>{row.stock}</TableCell>
                </TableRow>
            ))}
            </TableBody>
        </Table>
        </Paper>
    </div>
  );
}