import ReactDOM from 'react-dom';
import React from 'react';
import {Switch, Router} from 'react-router';
import createBrowserHistory from 'history/createBrowserHistory'

import App from './app';

const customHistory = createBrowserHistory();

ReactDOM.render(
        <Router history={customHistory}>
            <Switch>
                <App/>
            </Switch>
        </Router>
    , document.getElementById('app')
);

if (module.hot){
    module.hot.accept(App, ()=>{

    });
}

