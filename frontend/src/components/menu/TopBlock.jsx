import React, { useState } from 'react';
import { useSpring, animated } from 'react-spring';
import MenuUnit from './MenuUnit';
import './top_block.css';


const arrivedpoint = 'Поступившие';
const outpoint = 'Выписанные';
const deadpoint = 'Умершие';
const oarpoint = 'ОАР и ОРИТ';
const refusingpoint = 'Отказано';
const hosppoint = 'Госпитализировано';

const TopBlock = () => {
  const [isHovered, setHovered] = useState(false);

  const handleToggleHover = () => {
    setHovered(!isHovered);
  };

  const props = useSpring({
    from: { opacity: 0 },
    to: { opacity: 1 },
    config: { duration: 700 },
  });

  const dropdownProps = useSpring({
    height: isHovered ? 'auto' : 0,
    opacity: isHovered ? 1 : 0,
    config: { tension: 300, friction: 30 },
  });

  const textContent = 'Оперативная сводка ГКБ им. Демихова';
  const currentDatetime = new Date().toLocaleDateString('ru-RU');

  return (
    <animated.div
      className='top_block'
      style={props}
      onMouseEnter={handleToggleHover}
      onMouseLeave={handleToggleHover}
    >
      <p className='main_header'>{textContent}</p>
      <span className='now_date'>{currentDatetime}</span>

      {/* Dropdown */}
      <animated.div className='dropdown' style={dropdownProps}>
        {/* Add your dropdown content here */}
        <MenuUnit point={arrivedpoint}/>
        <MenuUnit point={refusingpoint}/>
        <MenuUnit point={hosppoint}/>
        <MenuUnit point={outpoint}/>
        <MenuUnit point={deadpoint}/>
        <MenuUnit point={oarpoint}/>
        {/* <MenuUnit point={}/> */}
      </animated.div>
    </animated.div>
  );
};

export default TopBlock;
