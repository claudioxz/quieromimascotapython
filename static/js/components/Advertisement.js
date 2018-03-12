import React, {Component} from 'react'
import PropTypes  from 'prop-types';
import {Col, Well, Label} from 'react-bootstrap';

export default class Advertisement extends Component{

    get

    render(){
        let {advertisement} = this.props;
        return (
            <Col md={3}>
                <div className="aviso">
                    <div className="aviso-container-title">
                        <div className="aviso-title">
                            {advertisement.titulo}
                        </div>
                    </div>
                    <div>
                        <div className="aviso-cotainer-date">
                            <Label bsStyle="success">{advertisement.fecha_publicacion}</Label>
                        </div>
                        <div className="aviso-container-imagen">
                            <img className="aviso-imagen" width="200" height="200" src={advertisement.imagenes[0].archivo} />
                        </div>
                        <Well bsSize="sm" className="aviso-tipo">
                            {advertisement.tipo_aviso.value}
                        </Well>
                        <div className="caption aviso-container-region">
                            <div className="aviso-region">
                                <label style={{minWidth: '25%', width:'60px'}}>Region</label>
                                <span style={{width: '75%'}}>Santiago</span>
                            </div>
                            <div className="aviso-region">
                                <label style={{minWidth: '25%', width:'60px'}}>Comuna</label>
                                <span style={{width: '75%'}}>Valdvia</span>
                            </div>
                        </div>
                    </div>
                </div>
            </Col>
        )
    }
}

Advertisement.propTypes = {
    advertisement: PropTypes.shape({
        titulo: PropTypes.string,
        fecha_publicacion: PropTypes.string,
        imagenes: PropTypes.array,
        tipo_aviso: PropTypes.shape({
            key: PropTypes.number,
            value: PropTypes.string
        }),
    }),
    archivo: PropTypes.string
};