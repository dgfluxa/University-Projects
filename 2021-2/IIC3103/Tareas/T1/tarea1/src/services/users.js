import axios from 'axios';

const canvas_id = '48378';
const API_URL = 'https://us-central1-taller-integracion-310700.cloudfunctions.net/tarea-1-2021-2/' + canvas_id;

async function getUsers() {
    var pages = 1;
    var users = [];
    for (var page = 1; page <= pages; page++) {  
        var url = API_URL + '/users?_page=' + page;
        var response = await axios.get(url);
        if (pages === 1) {
            var num = parseInt(response.headers['x-total-count']);
            if (num%10 === 0) {
                pages = num/10;
            } else {
                pages = num/10 + 1;
            }
        }
        users = users.concat(response.data);
    }
    return users;
} 

async function getUser(id) {
    const user_id = id;
    var url = API_URL + '/users/' + user_id;
    var response = await axios.get(url);
    return response.data;
} 

async function getUserCards(id) {
    const user_id = id;
    var url = API_URL + '/users/' + user_id + '/credit-cards';
    var response = await axios.get(url);
    return response.data;
} 

async function getUserAddresses(id) {
    const user_id = id;
    var url = API_URL + '/users/' + user_id + '/addresses';
    var response = await axios.get(url);
    return response.data;
} 

async function getSomeUsers(list) {
    const id_list = list;
    const users = [];
    for (var i = 0; i < id_list.length; i++) {
        var user = await getUser(id_list[i]);
        users.push(user);
    }
    return users;
}

async function searchUsers(string) {
    var pages = 1;
    var users = [];
    const text = string;
    for (var page = 1; page <= pages; page++) {  
        var url = API_URL + '/users?q=' + text + '&_page=' + page;
        var response = await axios.get(url);
        if (pages === 1) {
            var num = parseInt(response.headers['x-total-count']);
            if (num%10 === 0) {
                pages = num/10;
            } else {
                pages = num/10 + 1;
            }
        }
        users = users.concat(response.data);
    }
    return users;
} 

export default { getUsers, getUser, getUserCards, getUserAddresses, getSomeUsers, searchUsers };