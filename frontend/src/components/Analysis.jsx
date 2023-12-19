import React, { useState } from 'react';
import { useLocation } from 'react-router-dom';
import { useSpring, animated } from 'react-spring';
import DroppingMenu from './DroppingMenu'; 
import "./menu_styles.css"
import "./parent.css"


function GetAnalysis() {
  const location = useLocation();
  const userData = location.state?.userData;
  const [isHovered, setHovered] = useState(false);

  const handleMouseEnter = () => {
    setHovered(true);
  };

  const handleMouseLeave = () => {
    setHovered(true);
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
        <li className='menu_p'>TEST</li>
        <li className='menu_p'>TEST1</li>
        <li className='menu_p'>TEST2</li>
      </ul>

      </animated.nav>
    </div>
  );
}

export default GetAnalysis;
