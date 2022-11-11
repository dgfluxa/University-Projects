import React from 'react';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import NavBar from '../components/navbar';
import Home from './home';
import Info from './info';


export default function Routes() {
    return (
        <Router >
            <NavBar />
            <Switch>
                <Route path='/tarea-3-dgfluxa/' exact component={Home} />
                <Route path='/tarea-3-dgfluxa/Info' exact component={Info} />
            </Switch>
        </Router>
    );
};