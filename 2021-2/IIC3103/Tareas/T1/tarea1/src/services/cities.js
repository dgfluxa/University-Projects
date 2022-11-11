import axios from 'axios';

const canvas_id = '48378';
const API_URL = 'https://us-central1-taller-integracion-310700.cloudfunctions.net/tarea-1-2021-2/' + canvas_id;

async function getCities() {
    var pages = 1;
    var cities = [];
    for (var page = 1; page <= pages; page++) {  
        var url = API_URL + '/cities?_page=' + page;
        var response = await axios.get(url);
        if (pages === 1) {
            var num = parseInt(response.headers['x-total-count']);
            if (num%10 === 0) {
                pages = num/10;
            } else {
                pages = num/10 + 1;
            }
        }
        cities = cities.concat(response.data);
    }
    return cities;
} 

async function getCity(id) {
    const city_id = id;
    var url = API_URL + '/cities/' + city_id;
    var response = await axios.get(url);
    return response.data;
} 

async function searchCities(string) {
    var pages = 1;
    var cities = [];
    const text = string;
    for (var page = 1; page <= pages; page++) {  
        var url = API_URL + '/cities?q=' + text + '&_page=' + page;
        var response = await axios.get(url);
        if (pages === 1) {
            var num = parseInt(response.headers['x-total-count']);
            if (num%10 === 0) {
                pages = num/10;
            } else {
                pages = num/10 + 1;
            }
        }
        cities = cities.concat(response.data);
    }
    return cities;
} 

export default { getCities, getCity, searchCities };