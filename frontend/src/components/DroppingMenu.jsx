import React, { useState } from 'react';
import { useSpring, animated } from 'react-spring';
import "./menu_styles.css";
import "./menu_point.css";

function DroppingMenu({ label, children }) {
  const [isHovered, setHovered] = useState(false);

  const handleMouseEnter = () => {
    setHovered(true);
  };

  const handleMouseLeave = () => {
    setHovered(false);
  };

  const menuSpring = useSpring({
    opacity: isHovered ? 1 : 0,
    transform: `scale(${isHovered ? 1 : 0})`,
    config: { duration: 300 },
  });

  return (
    <div
      className='menu_p'
      onMouseEnter={handleMouseEnter}
      onMouseLeave={handleMouseLeave}
    >
      {label}
      <animated.div
        className={`childmenu ${isHovered ? "active" : ""}`}
        style={menuSpring}
      >
        {children}
      </animated.div>
    </div>
  );
}

export default DroppingMenu;
