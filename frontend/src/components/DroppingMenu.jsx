import React, { useState } from 'react';
import { useSpring, animated } from 'react-spring';
// import MenuPoint from './MenuPoint';
import "./menu_styles.css";
import "./menu_point.css";

function DroppingMenu() {
  const [isHovered, setHovered] = useState(false);

  const handleMouseEnter = () => {
    setHovered(true);
  };

  const handleMouseLeave = () => {
    setHovered(false);
  };

  const menuPointSpring = useSpring({
    opacity: isHovered ? 1 : 0,
    transform: `scale(${isHovered ? 1 : 0})`,
    config: { duration: 300 },
  });

  return (
    <animated.nav 
    className={`submenu ${isHovered ? "active" : ""}`}
    
    >
      <ul className='submenu_list'>
        <li className='menu_p'>TEST</li>
        <li className='menu_p'>TEST1</li>
        <li className='menu_p'>TEST2</li>
      </ul>
    </animated.nav>
  );
}

export default DroppingMenu;
