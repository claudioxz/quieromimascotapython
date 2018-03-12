import React, {Component} from 'react';
import {Panel} from 'react-bootstrap';
import  PropTypes from 'prop-types'

import CategoriesContainer from './categories-panel';
import RegionContainer from './region-panel';
import Advertisement from '../components/Advertisement';

const GenericPanel = props=>(
    <Panel>
        <Panel.Heading>
            <Panel.Title componentClass="h3">{props.title}</Panel.Title>
        </Panel.Heading>
        <Panel.Body>
            {props.children}
        </Panel.Body>
    </Panel>
);


const LastAdvertisementContainer = props=>(
    props.lastAdvertisements.map((advertisement, index) => {
        let key = `ad_${index}`;
        return (
            <Advertisement key={key} advertisement={advertisement}/>
        )
    })
);

LastAdvertisementContainer.propTypes = {
    lastAdvertisements: PropTypes.array
};


export const LastAdvertisement = props=> (
    <GenericPanel title="Ultimos avisos">
        <LastAdvertisementContainer lastAdvertisements={props.lastAdvertisements}/>
    </GenericPanel>
);

export const AdvertisementByCategories = ()=> (
    <GenericPanel title="Aviso por categoria">
        <CategoriesContainer/>
    </GenericPanel>
);

export const AdvertisementByRegion = props=> (
    <GenericPanel title="Avisos por region">
        <RegionContainer regiones={props.regiones}/>
    </GenericPanel>
);