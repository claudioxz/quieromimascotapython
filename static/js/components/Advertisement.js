import React, {Component} from 'react'
import PropTypes  from 'prop-types';
import {Col, Well, Label} from 'react-bootstrap';
import {getDayName} from "../utils";
import capitalize from "react-bootstrap/es/utils/capitalize";

export default class Advertisement extends Component{

    getHora(){
        let {fecha_publicacion} = this.props.advertisement;

        let date = new Date(fecha_publicacion);
        let dateNow = new Date(Date.now());

        let result = dateNow.getDate() - date.getDate();
        let message;
        let horaMinuto = `${date.getHours()}:0${date.getMonth()}`;
        switch (result){
            case 0:
                message = `Hoy a las ${horaMinuto}`;
                break;
            case -1:
                message = `Ayer a las ${horaMinuto}`;
                break;
            default:
                let dayName = capitalize(getDayName(date, 'es'));
                message = `${dayName} ${date.getDay()} a las ${horaMinuto}`;
                break;
        }

        return message;
    }

    render(){
        let {advertisement} = this.props;
        let hora = this.getHora();
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
                            <Label bsStyle="success">{hora}</Label>
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
                                <span style={{width: '75%'}}>Los rios</span>
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