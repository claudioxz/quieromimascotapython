import React, {Component} from 'react';
import {Navbar} from 'react-bootstrap'

import {NavbarLogin, NavbarLinks, NavbarSearch} from './navbar-items';


export default class NavbarComponent extends Component {
    render(){
        return (
            <Navbar inverse collapseOnSelect>
                <Navbar.Header>
                    <Navbar.Brand>
                        <a href="#">Quiero mi mascota</a>
                    </Navbar.Brand>
                    <Navbar.Toggle />
                </Navbar.Header>
                <Navbar.Collapse>

                    <NavbarSearch/>

                    <NavbarLinks/>

                    <NavbarLogin/>

                </Navbar.Collapse>
            </Navbar>
        )
    }
}