import axios from 'axios';
import { API_URL } from './variables'


async function getStocks() {
    var response = await axios.get(API_URL+'/almacenes/');
    return response.data;
};

async function getGeneralStocks() {
    var response = await axios.get(API_URL+'/generalStocks/');
    return response.data;
};


export default { getStocks, getGeneralStocks };