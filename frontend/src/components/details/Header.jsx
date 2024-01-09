import React from 'react';
import '../menu/top_block.css';


const Header = ({textHeader, currentDatetime}) => {

  return (
    <>
    <p className='main_header'> {textHeader}</p>
    <span className='now_date'> по состоянию на {currentDatetime}</span>
    </>
  );
};

export default Header;
