import axios from 'axios';
import { API_URL } from './variables'


async function getOC(id) {
    var response = await axios.get(API_URL+'/oc_detail/'+id);
    return response.data;
};

async function getGeneralOCs() {
    var response = await axios.get(API_URL+'/ocs/');
    return response.data;
};

async function getGroupOC(id) {
    var response = await axios.get(API_URL+'/ordenes-compra/'+id);
    return response.data;
};

async function getGeneralGroupOCs() {
    var response = await axios.get(API_URL+'/ordenes-compra/');
    return response.data;
};


export default { getOC, getGeneralOCs, getGroupOC, getGeneralGroupOCs };