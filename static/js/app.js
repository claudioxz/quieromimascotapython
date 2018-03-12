import React, {Component} from 'react';
import {Route} from 'react-router';

import NavbarComponent from './navbar/navbar';
import Home from './home/home'

const Publicar = ()=>(
    <div>
        <h1>Publicar</h1>
    </div>
);

const PageNotfound = ()=>(
  <div>
      <h1>Opps! Page not found</h1>
  </div>
);

export default class App extends Component {

    render() {
        return (
            <div>
                <NavbarComponent/>
                <Route exact path='/' component={Home}/>
                <Route path='/publicar' component={Publicar}/>
            </div>
        );
    }
}