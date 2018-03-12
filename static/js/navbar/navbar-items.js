import {Nav, NavItem, Button, Glyphicon, FormControl, FormGroup, Navbar} from 'react-bootstrap';
import React, {Component} from 'react';
import {Link} from 'react-router-dom';

export const NavbarSearch = () => (
    <Navbar.Form pullLeft>
        <FormGroup>
            <FormControl type="text" placeholder="Buscar..."/>
            <Button>
                <Glyphicon glyph="search"/>
            </Button>
        </FormGroup>
    </Navbar.Form>
);


export const NavbarLinks = ()=> (
    <ul className="nav navbar-nav">
        <li role="presentation">
            <Link to="/">Inicio</Link>
        </li>

        <li role="presentation">
            <Link to="/publicar">Publicar</Link>
        </li>

    </ul>
);

const marginLeft = {
    marginRight: '4px'
};

export const NavbarLogin = () => (
    <ul className="nav navbar-nav navbar-right">
        <li role="presentation">
            <Link to="/registro" role="button">
                <Glyphicon glyph="info-sign" style={marginLeft}/>
                <span>
                    Registro
                </span>
            </Link>
        </li>

        <li role="presentation">
            <Link to="/ingresar" role="button">
                <Glyphicon glyph="log-in" style={marginLeft}/>
                <span>
                    Ingresar
                </span>
            </Link>
        </li>
    </ul>
);