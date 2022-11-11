import React, { useEffect, useState } from 'react';
import { Typography } from '@material-ui/core';
import GroupOCTable from '../components/group_oc_table';
import OCsService from '../services/ocs';
import Loader from "react-loader-spinner";
import Table from "@material-ui/core/Table";
import TableBody from "@material-ui/core/TableBody";
import TableCell from "@material-ui/core/TableCell";
import TableRow from "@material-ui/core/TableRow";
import Paper from "@material-ui/core/Paper";


function GroupOCs() {

	const [ocs, setOCs] = useState([]);
	const [loaded, setLoaded] = useState(false)

	useEffect(() => {
		OCsService.getGeneralGroupOCs().then((data) => {
			setOCs(data);
			setLoaded(true);
		});
	}, []);

	return (
		<div>
			<div style={{marginTop: '2%', marginBottom: "2%"}}>   
						<Typography variant="h3" style={{marginBottom: "2%"}}>
							Ordenes de Compra entre Grupos
						</Typography>
						{loaded? 
								<div style={{marginLeft: '5%', marginRight: '5%', marginTop: '2%'}}>
									<div style={{display: 'flex', marginTop: '2%', justifyContent: 'center'}}>
										<Paper style={{width: '20%', minWidth: 300}}>
											<Table size='small'>
												<TableBody>
													<TableRow>
														<TableCell style={{color: 'orange'}}>Recibidas:</TableCell>
														<TableCell >{ocs.estadisticas.recibidas}</TableCell>
													</TableRow>
													<TableRow>
														<TableCell style={{color: 'green'}}>Aceptadas:</TableCell>
														<TableCell >{ocs.estadisticas.aceptadas}</TableCell>
													</TableRow>
													<TableRow>
														<TableCell style={{color: 'red'}}>Rechazadas:</TableCell>
														<TableCell >{ocs.estadisticas.rechazadas}</TableCell>
													</TableRow>
													<TableRow>
														<TableCell >Finalizadas:</TableCell>
														<TableCell >{ocs.estadisticas.finalizadas}</TableCell>
													</TableRow>
												</TableBody>
											</Table>
										</Paper>
									</div>
									
									<GroupOCTable data={ocs.ordenes} />
								</div>
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

export default GroupOCs;