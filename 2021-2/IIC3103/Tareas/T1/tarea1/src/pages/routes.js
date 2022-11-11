import React from 'react';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import NavBar from '../components/navbar';
import Home from './home';
import Users from './users';
import Cities from './cities';
import Search from './search';
import UserDetails from './user_details';
import CityDetails from './city_details';


export default function Routes() {
    return (
        <Router>
            <NavBar />
            <Switch>
                <Route path='/' exact component={Home} />
                <Route path='/users' exact component={Users} />
                <Route path='/cities' exact component={Cities} />
                <Route path='/search/:text' exact component={Search} />
                <Route path='/users/:id' exact component={UserDetails}/>     
                <Route path='/cities/:id' exact component={CityDetails}/>
            </Switch>
        </Router>
    );
};