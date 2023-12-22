import React from 'react';
import './menu_unit.css';

const MenuUnit = ({point}) => {

    return (
        <button className='menu_point'>
            {point}
        </button>        
    );
}

export default MenuUnit;