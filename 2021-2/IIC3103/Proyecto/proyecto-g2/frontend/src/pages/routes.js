import React from 'react';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import NavBar from '../components/navbar';
import Home from './home';
import FTPOCs from './ftp_ocs';
import FTPOCDetails from './ftp_oc_details';
import GroupOCs from './group_ocs';
import GroupOCDetails from './group_oc_details';


export default function Routes() {
    return (
        <Router >
            <NavBar />
            <Switch>
                <Route path='/' exact component={Home} />
                <Route path='/ftp_ocs' exact component={FTPOCs} />
                <Route path='/ftp_ocs/:id' exact component={FTPOCDetails}/> 
                <Route path='/group_ocs' exact component={GroupOCs} />
                <Route path='/group_ocs/:id' exact component={GroupOCDetails}/> 
            </Switch>
        </Router>
    );
};