import React, {Component} from 'react';
import {Grid, Col} from 'react-bootstrap';
import Axios from 'axios';

import {LastAdvertisement, AdvertisementByRegion, AdvertisementByCategories} from './home-components'

export default class Home extends Component{

    constructor(props){
        super(props);
        this.state = {
            regiones: [],
            ultimosAvisos: [],
        }
    }

    getRegiones(){
        return Axios.get('api/regiones');
    }

    getUltimosAvisos(){
        return Axios.get('api/avisos?limit=5');
    }

    componentDidMount(){
        Axios.all([this.getRegiones(), this.getUltimosAvisos()])
            .then(Axios.spread((regiones, ultimosAvisos)=>{
                this.setState({
                    regiones: regiones.data.results,
                    ultimosAvisos: ultimosAvisos.data.results
                });
            }));
    }

    render(){
        const {regiones, ultimosAvisos} = this.state;
        return (
            <Grid>
                <Col md={12}>
                    <LastAdvertisement lastAdvertisements={ultimosAvisos}/>
                </Col>

                <Col md={12}>
                    <AdvertisementByCategories/>
                </Col>

                <Col md={12}>
                    <AdvertisementByRegion regiones={regiones}/>
                </Col>
            </Grid>
        );
    }
}
