/**
 * Created by claudio on 03-03-18.
 */
import {ButtonGroup} from 'react-bootstrap';
import React, {Component} from 'react';

const CategoriesList = ()=>{
    const categories = [
        "Mascota encontrada",
        "Mascota desaparecida",
        "Dar en adopcion",
        "Adoptar una mascota",
    ];
    return (
        categories.map((val, index) =>{
            let key = `${index}_cat`;
            return <a key={key} className="btn btn-primary">{val}</a>;
        })
    );
};

class CategoriesContainer extends Component{

    constructor(props){
        super(props);
    }

    render(){
        return (
            <ButtonGroup id="btng-cat">
                <CategoriesList />
            </ButtonGroup>
        );
    }
    updateDimensions() {
        let w = window.innerWidth;
        let div = document.getElementById('btng-cat');
        div.className="btn-group-justified";
        if (w <= 700) {
            div.className="btn-group cat_index";
        }
    }

    componentDidMount(){
        this.updateDimensions();
        window.addEventListener("resize", this.updateDimensions);
    }
    componentWillUnmount(){
        window.removeEventListener("resize", this.updateDimensions);
    }
}

export default CategoriesContainer;