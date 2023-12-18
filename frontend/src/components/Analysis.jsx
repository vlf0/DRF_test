import React, { useState } from 'react';
import { useLocation } from 'react-router-dom';
import "./menu_styles.css"
  

function GetAnalysis() {
  const location = useLocation();
  const userData = location.state?.userData;
  const [isOpen, setOpen] = useState(false);
  const handleButtonClick = () => {
    // Handle button click logic
    console.log('Button clicked!');
    // You can update state or perform any other actions here
  };

  return (
    <div className="dashboard">

    {/* <header className='header'> */}
      <button className='menu-button' onClick={() => setOpen(!isOpen)}>НАВИГАЦИЯ</button>
      <nav className={`menu ${isOpen ? "active" : ""}`}>
        <ul className='menu_list'>
            <li className='menu_item'>ПАО</li>
            <li className='menu_item'>ПО</li>
            <li className='menu_item'>Администрация</li>
            <li className='menu_item'>IT</li>
            <li className='menu_item'>Контроль качества</li>
            <li className='menu_item'>Лабораотрия</li>
        </ul>
      </nav>
    {/* </header> */}

    </div>
  );
}


export default GetAnalysis;