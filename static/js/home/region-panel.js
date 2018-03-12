/**
 * Created by claudio on 03-03-18.
 */
import React, {Component} from 'react';
import PropTypes from 'prop-types';


const RegionList = props => (
    props.regiones.map((region, index)=>{
        let key = `reg_${index}`;
        return (
            <li key={key}>
                <a className="link">
                    <span className="icon-region">{region.numero}</span>
                    {region.nombre}
                </a>
            </li>
        );
    })
);

RegionList.propTypes = {
    regiones: PropTypes.array.isRequired,
    region: PropTypes.shape({
        nombre: PropTypes.string,
        numero: PropTypes.number
    })
};

const RegionContainer = props => (
    <ul className="col-lg-12 region-list" >
        <RegionList regiones={props.regiones}/>
    </ul>
);

export default RegionContainer;
