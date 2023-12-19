import React, { useState } from 'react';
import { useLocation } from 'react-router-dom';
import { useSpring, animated } from 'react-spring';
import DroppingMenu from './DroppingMenu'; 
import "./menu_styles.css"
import "./parent.css"
import "./menu_point.css"


function GetAnalysis() {
  const location = useLocation();
  const userData = location.state?.userData;
  const [isHovered, setHovered] = useState(false);

  const handleMouseEnter = () => {
    setHovered(true);
  };

  const handleMouseLeave = () => {
    setHovered(false);
  };

  const buttonSpring = useSpring({
    opacity: isHovered ? 0.8 : 1,
    config: { duration: 300 },
  });

  const menuSpring = useSpring({
    opacity: isHovered ? 1 : 0,
    transform: `scale(${isHovered ? 1 : 0})`,
    config: { duration: 300 },
  });

  const handleButtonClick = () => {
    // Handle the button click logic, e.g., send POST request
    console.log('Button inside DroppingMenu clicked!');
    // Add your logic to send POST request here
  };

  return (
    <div className="dashboard">
      <button
        className='menu-button'
        onMouseEnter={handleMouseEnter}
        onMouseLeave={handleMouseLeave}
        style={buttonSpring}
      >
        НАВИГАЦИЯ
      </button>
      <animated.nav
        className={`menu ${isHovered ? "active" : ""}`}
        onMouseEnter={handleMouseEnter}
        onMouseLeave={handleMouseLeave} // Close the menu when leaving the button
        style={menuSpring}
      > 
        <ul className='menu_list'>
         {[
           { label: 'поступившие', buttons: ['текущие сутки', 'прошедшие сутки'] },
           { label: 'выбывшие', buttons: ['текущие сутки', 'прошедшие сутки'] },
           { label: 'TEST2', buttons: ['Отчет 1', 'отчет 2'] },
         ].map(({ label, buttons }) => (
           <DroppingMenu key={label} label={label}>
             {buttons.map((buttonLabel) => (
               <button key={buttonLabel} className='api_buttons' onClick={handleButtonClick}>
                 {buttonLabel}
               </button>
             ))}
           </DroppingMenu>
         ))}
        </ul>
      </animated.nav>
    </div>
  );
}

export default GetAnalysis;
